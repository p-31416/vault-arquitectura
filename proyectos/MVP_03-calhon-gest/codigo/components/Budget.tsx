import React, { useState } from 'react';
import type { FeeCalculationResult, MarketData, MediciónResult, ServiceOptions, SavedBudget } from '../types';
import BudgetChart from './BudgetChart';
import { saveBudget } from '../utils/storage';

declare global {
  interface Window {
    jspdf: any;
  }
}

interface BudgetProps {
  feeData: FeeCalculationResult;
  medicionData: MediciónResult | null;
  marketData: MarketData | null;
  loading: boolean;
  squareMeters: number;
  services: ServiceOptions;
}

const formatARS = (value: number) =>
  new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS', maximumFractionDigits: 0 }).format(value);

const Budget: React.FC<BudgetProps> = ({ feeData, medicionData, marketData, loading, squareMeters, services }) => {
  const [managementName, setManagementName] = useState('');
  const [saveSuccess, setSaveSuccess] = useState(false);

  const today = new Date().toLocaleDateString('es-AR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });

  if (loading) {
    return (
      <div className="bg-white rounded-2xl shadow-2xl shadow-slate-300/30 p-6 md:p-8 text-center">
        <p className="text-slate-500 animate-pulse">Cargando datos del mercado...</p>
      </div>
    );
  }

  if (!marketData) {
    return (
      <div className="bg-white rounded-2xl shadow-2xl shadow-slate-300/30 p-6 md:p-8 text-center">
        <p className="text-red-500">No se pudieron cargar los datos del mercado.</p>
      </div>
    );
  }

  const totalFromDolar = feeData.totalFee * marketData.dolarBlue.venta;
  const totalFromGold = feeData.totalGoldFee * marketData.gold24k.precioPorGramo;
  const averagePrice = (totalFromDolar + totalFromGold) / 2;

  const getTotalConServicios = () => {
    let total = averagePrice;
    if (medicionData) total += medicionData.total;
    return total;
  };

  const handleSaveBudget = () => {
    if (!managementName.trim() || !marketData) return;

    const newBudget: SavedBudget = {
      id: `${new Date().getTime()}-${squareMeters}`,
      managementName: managementName.trim(),
      squareMeters,
      services,
      feeData,
      medicionData,
      marketData,
      averagePrice,
      totalARS: getTotalConServicios(),
      savedAt: new Date().toISOString(),
    };

    saveBudget(newBudget);
    setManagementName('');
    setSaveSuccess(true);
    setTimeout(() => setSaveSuccess(false), 3000);
  };

  const handleExportPDF = () => {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    doc.setFontSize(22);
    doc.setFont('helvetica', 'bold');
    doc.text('Presupuesto de Honorarios', 105, 20, { align: 'center' });

    doc.setFontSize(12);
    doc.setFont('helvetica', 'normal');
    doc.text(`Nombre de la Gestión: ${managementName || 'No especificado'}`, 14, 40);
    doc.text(`Fecha: ${today}`, 14, 48);
    doc.text(`Superficie: ${squareMeters.toFixed(0)} m²`, 14, 56);

    doc.line(14, 62, 196, 62);

    doc.setFontSize(16);
    doc.setFont('helvetica', 'bold');
    doc.text('Análisis de Costos', 14, 72);

    doc.setFontSize(12);
    doc.setFont('helvetica', 'normal');
    doc.text('Gestión (USD -> ARS):', 14, 82);
    doc.setFont('helvetica', 'bold');
    doc.text(formatARS(totalFromDolar), 80, 82);

    doc.setFont('helvetica', 'normal');
    doc.text('Gestión (Oro -> ARS):', 14, 92);
    doc.setFont('helvetica', 'bold');
    doc.text(formatARS(totalFromGold), 80, 92);

    if (medicionData) {
      doc.setFont('helvetica', 'normal');
      doc.text('Medición / Replanteo (CPAU):', 14, 102);
      doc.setFont('helvetica', 'bold');
      doc.text(formatARS(medicionData.total), 80, 102);
    }

    doc.line(14, 110, 196, 110);

    doc.setFontSize(18);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(16, 185, 129);
    doc.text('Costo Total Estimado', 105, 122, { align: 'center' });

    doc.setFontSize(26);
    doc.text(formatARS(getTotalConServicios()), 105, 132, { align: 'center' });
    doc.setTextColor(0, 0, 0);

    doc.setFontSize(10);
    doc.setTextColor(150);
    doc.text('Estimación referencial — no constituye una oferta formal.', 105, 150, { align: 'center' });

    const fileName = `presupuesto_${(managementName || 'proyecto').replace(/\s+/g, '_')}.pdf`;
    doc.save(fileName);
  };

  return (
    <div className="bg-white rounded-2xl shadow-2xl shadow-slate-300/30 overflow-hidden">
      <div className="p-6 md:p-8">
        <div className="text-center">
          <h1 className="text-2xl md:text-3xl font-bold text-slate-800">Presupuesto Final</h1>
          <p className="text-slate-500 mt-1 text-sm">Resumen de costos para presentar al cliente</p>
        </div>

        <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label htmlFor="management-name" className="block text-sm font-medium text-slate-700">
              Nombre de la Gestión
            </label>
            <input
              type="text"
              id="management-name"
              value={managementName}
              onChange={(e) => setManagementName(e.target.value)}
              placeholder="Ej: Vivienda Unifamiliar"
              className="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md shadow-sm text-slate-900 placeholder-slate-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            />
          </div>
          <div className="bg-slate-50 p-3 rounded-lg text-center">
            <p className="text-xs text-slate-500">Fecha</p>
            <p className="font-semibold text-slate-700">{today}</p>
          </div>
          <div className="bg-slate-50 p-3 rounded-lg text-center">
            <p className="text-xs text-slate-500">Superficie</p>
            <p className="font-semibold text-slate-700">{squareMeters.toFixed(0)} m²</p>
          </div>
        </div>

        <div className="mt-6 space-y-3">
          <h3 className="text-md font-bold text-slate-700">Desglose de Servicios</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div className="bg-slate-50 p-4 rounded-xl">
              <p className="text-sm text-slate-500">Tramitación y Gestión (base)</p>
              <p className="text-xl font-bold text-slate-800">{formatARS(averagePrice)}</p>
              <p className="text-xs text-slate-400">USD {feeData.totalFee.toFixed(2)} × {formatARS(marketData.dolarBlue.venta)} | {feeData.totalGoldFee.toFixed(3)} gr × {formatARS(marketData.gold24k.precioPorGramo)}</p>
            </div>
            {medicionData && (
              <div className="bg-slate-50 p-4 rounded-xl border-l-4 border-indigo-400">
                <p className="text-sm text-slate-500">Medición / Replanteo (CPAU)</p>
                <p className="text-xl font-bold text-indigo-700">{formatARS(medicionData.total)}</p>
                <p className="text-xs text-slate-400">{medicionData.formula}</p>
              </div>
            )}
          </div>
        </div>
      </div>

      <div className="bg-slate-50 p-6 md:p-8 border-t border-slate-200">
        <h2 className="text-lg font-bold text-slate-700 mb-4 text-center">
          Análisis Comparativo
        </h2>
        <div className="h-72 mb-6">
          <BudgetChart
            dolarValue={totalFromDolar}
            goldValue={totalFromGold}
            averageValue={averagePrice}
          />
        </div>
        <div className="bg-emerald-50 border-2 border-emerald-500 rounded-lg p-5 text-center">
          <p className="text-md font-semibold text-emerald-800">Costo Base</p>
          <p className="text-3xl font-extrabold text-emerald-600">{formatARS(averagePrice)}</p>
        </div>
        {medicionData && (
          <div className="mt-3 text-center">
            <p className="text-sm text-slate-500">
              + Medición/Replanteo: {formatARS(medicionData.total)}
            </p>
            <p className="text-lg font-bold text-slate-800">
              Total: {formatARS(getTotalConServicios())}
            </p>
          </div>
        )}

        <div className="mt-6 text-center space-y-3">
          <div className="flex justify-center items-center flex-wrap gap-4">
            <button
              onClick={handleSaveBudget}
              disabled={!managementName.trim()}
              className="inline-flex items-center px-5 py-2.5 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-emerald-600 hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500 transition-transform hover:scale-105 disabled:bg-slate-400 disabled:cursor-not-allowed"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                <path d="M7.707 10.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V6a1 1 0 10-2 0v5.586L7.707 10.293zM3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" />
              </svg>
              Guardar Presupuesto
            </button>
            <button
              onClick={handleExportPDF}
              className="inline-flex items-center px-5 py-2.5 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-transform hover:scale-105"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V7.414A2 2 0 0015.414 6L12 2.586A2 2 0 0010.586 2H6zm5 6a1 1 0 10-2 0v3.586l-1.293-1.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V8z" clipRule="evenodd" />
              </svg>
              Exportar a PDF
            </button>
          </div>
          {saveSuccess && (
            <p className="text-center text-green-600 font-semibold">¡Presupuesto guardado con éxito!</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Budget;

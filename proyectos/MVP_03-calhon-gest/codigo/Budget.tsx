import React, { useState } from 'react';
// FIX: Corrected import paths for root directory
import type { FeeCalculationResult, MarketData } from './types';
import BudgetChart from './components/BudgetChart';

declare global {
  interface Window {
    jspdf: any;
  }
}

interface BudgetProps {
  feeData: FeeCalculationResult;
  marketData: MarketData | null;
  loading: boolean;
  squareMeters: number;
}

const formatCurrency = (value: number) => {
    return new Intl.NumberFormat('es-AR', {
        style: 'currency',
        currency: 'ARS',
    }).format(value);
}

const Budget: React.FC<BudgetProps> = ({ feeData, marketData, loading, squareMeters }) => {
    const [managementName, setManagementName] = useState('');

    const today = new Date().toLocaleDateString('es-AR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });

    if (loading) {
        return (
            <div className="bg-white rounded-2xl shadow-2xl shadow-slate-300/30 p-8 md:p-10 text-center">
                <p className="text-slate-500 animate-pulse">Cargando datos del mercado...</p>
            </div>
        );
    }
  
    if (!marketData) {
        return (
            <div className="bg-white rounded-2xl shadow-2xl shadow-slate-300/30 p-8 md:p-10 text-center">
                <p className="text-red-500">No se pudieron cargar los datos del mercado. Por favor, intente de nuevo más tarde.</p>
            </div>
        );
    }

    const totalInPesosFromDolar = feeData.totalFee * marketData.dolarBlue.venta;
    const totalInPesosFromGold = feeData.totalGoldFee * marketData.gold.precio;
    const averagePrice = (totalInPesosFromDolar + totalInPesosFromGold) / 2;

    const handleExportPDF = () => {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();
        
        // Title
        doc.setFontSize(22);
        doc.setFont('helvetica', 'bold');
        doc.text('Presupuesto de Honorarios', 105, 20, { align: 'center' });

        // Project Details
        doc.setFontSize(12);
        doc.setFont('helvetica', 'normal');
        doc.text(`Nombre de la Gestión: ${managementName || 'No especificado'}`, 14, 40);
        doc.text(`Fecha: ${today}`, 14, 48);
        doc.text(`Superficie Cotizada: ${squareMeters.toFixed(0)} m²`, 14, 56);
        
        doc.line(14, 62, 196, 62); // separator

        // Cost Analysis
        doc.setFontSize(16);
        doc.setFont('helvetica', 'bold');
        doc.text('Análisis de Costos', 14, 72);

        doc.setFontSize(12);
        doc.setFont('helvetica', 'normal');
        doc.text(`Costo por Conversión Dólar:`, 14, 82);
        doc.setFont('helvetica', 'bold');
        doc.text(formatCurrency(totalInPesosFromDolar), 80, 82);

        doc.setFont('helvetica', 'normal');
        doc.text(`Costo por Conversión Oro:`, 14, 92);
        doc.setFont('helvetica', 'bold');
        doc.text(formatCurrency(totalInPesosFromGold), 80, 92);

        doc.line(14, 102, 196, 102); // separator

        // Final Price
        doc.setFontSize(18);
        doc.setFont('helvetica', 'bold');
        doc.setTextColor(16, 185, 129); // Emerald color
        doc.text('Costo Final Sugerido (Promedio)', 105, 115, { align: 'center' });
        
        doc.setFontSize(26);
        doc.text(formatCurrency(averagePrice), 105, 125, { align: 'center' });
        doc.setTextColor(0, 0, 0);

        // Footer
        doc.setFontSize(10);
        doc.setTextColor(150);
        doc.text('Este documento es una estimación basada en los datos del mercado al momento de su generación.', 105, 147, { align: 'center' });

        const fileName = `presupuesto_${(managementName || 'proyecto').replace(/\s+/g, '_')}.pdf`;
        doc.save(fileName);
    };

    return (
        <div className="bg-white rounded-2xl shadow-2xl shadow-slate-300/30 overflow-hidden">
            <div className="p-8 md:p-10">
                <div className="text-center">
                    <h1 className="text-3xl md:text-4xl font-bold text-slate-800">
                        Presupuesto Final
                    </h1>
                    <p className="text-slate-500 mt-2">
                        Resumen de costos para presentar al cliente.
                    </p>
                </div>

                <div className="mt-10 grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                    <div className="md:col-span-1">
                        <label htmlFor="management-name" className="block text-sm font-medium text-slate-700">
                            Nombre de la Gestión
                        </label>
                        <input
                            type="text"
                            id="management-name"
                            value={managementName}
                            onChange={(e) => setManagementName(e.target.value)}
                            placeholder="Ej: Vivienda Unifamiliar Smith"
                            className="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md shadow-sm placeholder-slate-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        />
                    </div>
                    <div className="text-center md:text-right bg-slate-50 p-3 rounded-lg">
                        <p className="text-sm text-slate-500">Fecha del Presupuesto</p>
                        <p className="font-semibold text-slate-700">{today}</p>
                    </div>
                    <div className="text-center md:text-right bg-slate-50 p-3 rounded-lg">
                        <p className="text-sm text-slate-500">Superficie Cotizada</p>
                        <p className="font-semibold text-slate-700">{squareMeters.toFixed(0)} m²</p>
                    </div>
                </div>
            </div>

            <div className="p-8 md:p-10 border-t border-slate-200">
                <h2 className="text-xl font-bold text-slate-700 mb-4 text-center">
                    Análisis Comparativo de Costos
                </h2>
                <div className="h-72 mb-8">
                    <BudgetChart 
                        dolarValue={totalInPesosFromDolar}
                        goldValue={totalInPesosFromGold}
                        averageValue={averagePrice}
                    />
                </div>
                 <div className="bg-emerald-50 border-2 border-emerald-500 rounded-lg p-6 text-center">
                    <p className="text-lg font-semibold text-emerald-800">Costo Final Sugerido (Promedio)</p>
                    <p className="text-4xl font-extrabold text-emerald-600 mt-2">
                        {formatCurrency(averagePrice)}
                    </p>
                </div>

                <div className="mt-8 text-center">
                    <button
                        onClick={handleExportPDF}
                        className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-transform transform hover:scale-105"
                    >
                         <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-3" viewBox="0 0 20 20" fill="currentColor">
                            <path fillRule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clipRule="evenodd" />
                        </svg>
                        Exportar a PDF
                    </button>
                </div>
            </div>
        </div>
    );
};

export default Budget;
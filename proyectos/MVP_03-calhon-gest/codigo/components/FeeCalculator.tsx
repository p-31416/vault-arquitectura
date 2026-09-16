import React, { useState } from 'react';
import { MIN_SQM, MAX_SQM } from '../constants';
import type { FeeCalculationResult, ServiceOptions, MediciónResult } from '../types';
import FeeChart from './FeeChart';

interface FeeCalculatorProps {
  squareMeters: number;
  onSquareMetersChange: (value: number) => void;
  feeData: FeeCalculationResult;
  services: ServiceOptions;
  onServicesChange: (services: ServiceOptions) => void;
  medicionData: MediciónResult | null;
}

const formatARS = (value: number) =>
  new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS', maximumFractionDigits: 0 }).format(value);

const FeeCalculator: React.FC<FeeCalculatorProps> = ({
  squareMeters, onSquareMetersChange, feeData,
  services, onServicesChange, medicionData,
}) => {
  const [inputValue, setInputValue] = useState(String(squareMeters));
  const { pricePerSqm, totalFee, goldPricePerSqm, totalGoldFee } = feeData;

  const handleSliderChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const v = Number(e.target.value);
    onSquareMetersChange(v);
    setInputValue(String(v));
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const raw = e.target.value.replace(/[^0-9]/g, '');
    setInputValue(raw);
    const num = parseInt(raw, 10);
    if (!isNaN(num) && num >= MIN_SQM && num <= MAX_SQM) {
      onSquareMetersChange(num);
    }
  };

  const handleInputBlur = () => {
    const num = parseInt(inputValue, 10);
    if (isNaN(num) || num < MIN_SQM) {
      onSquareMetersChange(MIN_SQM);
      setInputValue(String(MIN_SQM));
    } else if (num > MAX_SQM) {
      onSquareMetersChange(MAX_SQM);
      setInputValue(String(MAX_SQM));
    } else {
      onSquareMetersChange(num);
      setInputValue(String(num));
    }
  };

  const toggleService = (key: keyof ServiceOptions) => {
    onServicesChange({ ...services, [key]: !services[key] });
  };

  const sliderProgress = ((squareMeters - MIN_SQM) / (MAX_SQM - MIN_SQM)) * 100;

  return (
    <div className="bg-white rounded-2xl shadow-2xl shadow-slate-300/30 overflow-hidden">
      <div className="p-6 md:p-8">
        <div className="text-center">
          <h1 className="text-2xl md:text-3xl font-bold text-slate-800">Calculadora de Honorarios</h1>
          <p className="text-slate-500 mt-1 text-sm">Gestión municipal residencial</p>
        </div>

        <div className="mt-6">
          <label className="block text-sm font-semibold text-slate-700 mb-2">Superficie (m²)</label>
          <div className="flex items-center gap-3">
            <input
              type="range"
              min={MIN_SQM}
              max={MAX_SQM}
              value={squareMeters}
              onChange={handleSliderChange}
              className="flex-1 h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer"
              style={{ background: `linear-gradient(to right, #4f46e5 ${sliderProgress}%, #e2e8f0 ${sliderProgress}%)` }}
            />
            <input
              type="text"
              inputMode="numeric"
              value={inputValue}
              onChange={handleInputChange}
              onBlur={handleInputBlur}
              className="w-20 text-center text-lg font-bold text-indigo-600 bg-slate-100 rounded-lg border border-slate-200 px-2 py-1 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />
            <span className="text-sm text-slate-500">m²</span>
          </div>
          <div className="flex justify-between text-xs text-slate-500 mt-1">
            <span>{MIN_SQM} m²</span>
            <span>{MAX_SQM} m²</span>
          </div>
        </div>

        <div className="mt-6">
          <h3 className="text-sm font-semibold text-slate-700 mb-2">Servicios adicionales</h3>
          <div className="space-y-2">
            <label className="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" checked={services.medicion} onChange={() => toggleService('medicion')} className="rounded border-slate-300 text-indigo-600 focus:ring-indigo-500" />
              <span className="text-sm text-slate-600">Medición / Replanteo (CPAU)</span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer opacity-50">
              <input type="checkbox" checked={services.digitalizacion} disabled className="rounded border-slate-300" />
              <span className="text-sm text-slate-500">Digitalización <span className="text-xs text-amber-500">(próximamente)</span></span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer opacity-50">
              <input type="checkbox" checked={services.adaptacionExterna} disabled className="rounded border-slate-300" />
              <span className="text-sm text-slate-500">Adaptación proyecto externo <span className="text-xs text-amber-500">(próximamente)</span></span>
            </label>
          </div>
        </div>

        <div className="mt-6">
          <h2 className="text-lg font-bold text-slate-700 mb-3 text-center">Análisis de Precio por m²</h2>
          <div className="h-56">
            <FeeChart currentSqm={squareMeters} currentPrice={pricePerSqm} currentGoldPrice={goldPricePerSqm} />
          </div>
        </div>
      </div>

      <div className="bg-slate-50 p-6 md:p-8 border-t border-slate-200">
        <h2 className="text-xl font-bold text-slate-800 mb-4 text-center">Desglose</h2>
        <div className="space-y-3">
          <div className="bg-white p-3 rounded-lg shadow-sm">
            <p className="text-xs text-slate-500">Gestión (USD/m²)</p>
            <p className="text-lg font-semibold text-slate-800">${pricePerSqm.toFixed(2)}</p>
            <p className="text-xs text-slate-400">Total: ${totalFee.toFixed(2)} USD</p>
          </div>
          <div className="bg-white p-3 rounded-lg shadow-sm">
            <p className="text-xs text-slate-500">Gestión (Oro/m²)</p>
            <p className="text-lg font-semibold text-amber-700">{goldPricePerSqm.toFixed(4)} gr</p>
            <p className="text-xs text-slate-400">Total: {totalGoldFee.toFixed(3)} gramos</p>
          </div>
          {medicionData && (
            <div className="bg-white p-3 rounded-lg shadow-sm border-l-4 border-indigo-400">
              <p className="text-xs text-slate-500">Medición / Replanteo (CPAU)</p>
              <p className="text-lg font-semibold text-indigo-700">{formatARS(medicionData.total)}</p>
              <p className="text-xs text-slate-400">{medicionData.formula}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default FeeCalculator;

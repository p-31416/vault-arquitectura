import React from 'react';
// FIX: Corrected import paths for root directory
import { MIN_SQM, MAX_SQM } from './constants';
import type { FeeCalculationResult } from './types';
import FeeChart from './components/FeeChart';

const BuildingIcon: React.FC<{className: string}> = ({ className }) => (
  <svg xmlns="http://www.w3.org/2000/svg" className={className} viewBox="0 0 24 24" fill="currentColor">
    <path d="M20.992 9.71a1 1 0 0 0-1.127-1.25l-6.15 1.757-3.414-3.414a1 1 0 0 0-1.414 0L3.414 12.276a1 1 0 0 0 0 1.414l5.473 5.473a1 1 0 0 0 1.414 0l5.473-5.473 1.757-6.15a1 1 0 0 0 .573-1.83Zm-15.578 4L10 9.123l3.414 3.414-5.473 5.473-4.573-4.573Z" />
    <path d="M21 13a1 1 0 0 0-1 1v2.879l-1-1V15a1 1 0 1 0-2 0v1.879l-1-1V17a1 1 0 1 0-2 0v1.879l-1-1V19a1 1 0 1 0-2 0v1h6a1 1 0 0 0 1-1v-6a1 1 0 0 0-1-1Z" />
  </svg>
);

const PriceTagIcon: React.FC<{className: string}> = ({ className }) => (
  <svg xmlns="http://www.w3.org/2000/svg" className={className} viewBox="0 0 24 24" fill="currentColor">
    <path fillRule="evenodd" d="M4 4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v2.586l5.707 5.707a2 2 0 0 1 0 2.828l-6 6a2 2 0 0 1-2.828 0L4 14.828V4Zm2 2v8.828l6.293 6.293 6-6L12.828 9.414A1 1 0 0 0 12.121 9H8V6H6Z" clipRule="evenodd" />
    <path d="M8 8a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z" />
  </svg>
);

const GoldBarIcon: React.FC<{ className: string }> = ({ className }) => (
    <svg xmlns="http://www.w3.org/2000/svg" className={className} viewBox="0 0 24 24" fill="currentColor">
        <path d="M3 8a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V8Zm2 7h14V9H5v6Z" />
        <path d="M4 10.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5H4.75A.75.75 0 0 1 4 10.25Zm0 3.5a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5H4.75A.75.75 0 0 1 4 13.75Z" />
    </svg>
);

interface FeeCalculatorProps {
    squareMeters: number;
    onSquareMetersChange: (value: number) => void;
    feeData: FeeCalculationResult;
}

const FeeCalculator: React.FC<FeeCalculatorProps> = ({ squareMeters, onSquareMetersChange, feeData }) => {
  const { pricePerSqm, totalFee, goldPricePerSqm, totalGoldFee } = feeData;

  const handleSliderChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    onSquareMetersChange(Number(e.target.value));
  };

  const sliderProgress = ((squareMeters - MIN_SQM) / (MAX_SQM - MIN_SQM)) * 100;

  return (
    <div className="bg-white rounded-2xl shadow-2xl shadow-slate-300/30 overflow-hidden">
      <div className="p-8 md:p-10">
        <div className="text-center">
            <h1 className="text-3xl md:text-4xl font-bold text-slate-800">
                Calculadora de Honorarios
            </h1>
            <p className="text-slate-500 mt-2">
                Estime los costos de gestión municipal de su proyecto.
            </p>
        </div>
        
        <div className="mt-10">
            <label htmlFor="sqm-slider" className="block text-lg font-semibold text-slate-700 mb-2">
                Metros Cuadrados (m²)
            </label>
            <div className="flex items-center justify-center bg-slate-100 rounded-lg p-4">
                <span className="text-3xl font-extrabold text-indigo-600 w-32 text-center">
                    {squareMeters.toFixed(0)} <span className="text-lg font-medium text-slate-500">m²</span>
                </span>
            </div>
        </div>

        <div className="mt-6">
          <input
            id="sqm-slider"
            type="range"
            min={MIN_SQM}
            max={MAX_SQM}
            value={squareMeters}
            onChange={handleSliderChange}
            className="w-full h-3 bg-slate-200 rounded-lg appearance-none cursor-pointer range-lg"
            style={{ 
              background: `linear-gradient(to right, #4f46e5 ${sliderProgress}%, #e2e8f0 ${sliderProgress}%)`
            }}
          />
          <div className="flex justify-between text-xs text-slate-500 mt-2">
            <span>{MIN_SQM} m²</span>
            <span>{MAX_SQM} m²</span>
          </div>
        </div>

        <div className="mt-10">
            <h2 className="text-xl font-bold text-slate-700 mb-4 text-center">
                Análisis de Precio por m²
            </h2>
            <div className="h-64">
                <FeeChart currentSqm={squareMeters} currentPrice={pricePerSqm} currentGoldPrice={goldPricePerSqm} />
            </div>
        </div>
      </div>

      <div className="bg-slate-50 p-8 md:p-10 border-t border-slate-200">
        <h2 className="text-2xl font-bold text-slate-800 mb-6 text-center">Resultados de la Estimación</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="flex flex-col space-y-6">
                <div className="flex items-center p-4 bg-white rounded-lg shadow-sm">
                    <PriceTagIcon className="h-8 w-8 text-indigo-500 mr-4"/>
                    <div>
                        <p className="text-sm text-slate-500">Precio por m² (USD)</p>
                        <p className="text-2xl font-semibold text-slate-800">
                           ${pricePerSqm.toFixed(2)}
                        </p>
                    </div>
                </div>
                 <div className="flex items-center p-4 bg-white rounded-lg shadow-sm">
                    <GoldBarIcon className="h-8 w-8 text-amber-500 mr-4"/>
                    <div>
                        <p className="text-sm text-slate-500">Precio por m² (Oro)</p>
                        <p className="text-2xl font-semibold text-slate-800">
                           {goldPricePerSqm.toFixed(4)} <span className="text-sm font-normal">gr</span>
                        </p>
                    </div>
                </div>
            </div>
            
            <div className="flex items-center justify-center p-6 bg-indigo-600 text-white rounded-lg shadow-lg shadow-indigo-200">
                 <div className="flex items-center">
                    <BuildingIcon className="h-10 w-10 text-white/80 mr-5"/>
                    <div>
                        <p className="text-md text-indigo-200">Costo Total (USD)</p>
                        <p className="text-3xl font-bold">
                           ${totalFee.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                        </p>
                         <p className="text-md text-amber-200 mt-2">Costo Total (Oro)</p>
                        <p className="text-2xl font-bold text-amber-300">
                           {totalGoldFee.toFixed(3)}
                           <span className="text-base font-medium ml-1">gramos</span>
                        </p>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>
  );
};

export default FeeCalculator;
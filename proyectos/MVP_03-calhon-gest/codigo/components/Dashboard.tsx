import React, { useState, useEffect } from 'react';
import type { MarketData } from '../types';
import HistoryChart from './HistoryChart';
import { getGoldSpotARS } from '../services/marketApi';

const formatARS = (value: number) =>
  new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS', maximumFractionDigits: 0 }).format(value);

const Dashboard: React.FC<{
  marketData: MarketData | null;
  loading: boolean;
  localPremium: number;
  onLocalPremiumChange: (v: number) => void;
}> = ({ marketData, loading, localPremium, onLocalPremiumChange }) => {
  const [spotInfo, setSpotInfo] = useState<{ spotUSD: number; spotARS: number } | null>(null);
  const [premiumInput, setPremiumInput] = useState(String(localPremium));

  useEffect(() => {
    getGoldSpotARS()
      .then(setSpotInfo)
      .catch(() => {});
  }, []);

  useEffect(() => {
    setPremiumInput(String(localPremium));
  }, [localPremium]);

  const handlePremiumBlur = () => {
    const num = parseFloat(premiumInput.replace(/[^0-9.]/g, ''));
    if (num >= 0 && num <= 100) onLocalPremiumChange(num);
    setPremiumInput(String(localPremium));
  };

  const renderContent = () => {
    if (loading) {
      return (
        <div className="flex justify-center items-center h-full min-h-[340px]">
          <p className="text-slate-500 animate-pulse">Cargando datos del mercado...</p>
        </div>
      );
    }

    if (!marketData) {
      return (
        <div className="flex justify-center items-center h-full min-h-[340px]">
          <p className="text-red-500">Error al cargar datos del mercado.</p>
        </div>
      );
    }

    return (
      <>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-slate-50 p-5 rounded-xl border-l-4 border-blue-500">
            <p className="text-xs text-slate-500 uppercase tracking-wide">Dólar Blue (Venta)</p>
            <p className="text-2xl font-bold text-slate-800">{formatARS(marketData.dolarBlue.venta)}</p>
            <p className="text-xs text-slate-400">Compra: {formatARS(marketData.dolarBlue.compra)}</p>
          </div>
          <div className="bg-slate-50 p-5 rounded-xl border-l-4 border-emerald-500">
            <p className="text-xs text-slate-500 uppercase tracking-wide">Dólar Oficial (Venta)</p>
            <p className="text-2xl font-bold text-slate-800">{formatARS(marketData.dolarOficial.venta)}</p>
            <p className="text-xs text-slate-400">Compra: {formatARS(marketData.dolarOficial.compra)}</p>
          </div>
          <div className="bg-slate-50 p-5 rounded-xl border-l-4 border-amber-500">
            <p className="text-xs text-slate-500 uppercase tracking-wide">Oro 24K (ARS/gramo)</p>
            <p className="text-2xl font-bold text-slate-800">{formatARS(marketData.gold24k.precioPorGramo)}</p>
            <div className="mt-2 space-y-1">
              {spotInfo && (
                <p className="text-xs text-slate-400">
                  Spot internacional: {formatARS(Math.round(spotInfo.spotARS))}
                </p>
              )}
              <label className="text-xs text-slate-400 flex items-center gap-1">
                Ajuste local:
                <input
                  type="text"
                  inputMode="decimal"
                  value={premiumInput}
                  onChange={(e) => setPremiumInput(e.target.value)}
                  onBlur={handlePremiumBlur}
                  className="w-12 text-xs bg-white border border-slate-300 rounded px-1 py-0.5 text-right"
                />
                <span>%</span>
              </label>
            </div>
          </div>
        </div>
        <div className="mt-8">
          <h3 className="text-lg font-bold text-slate-700 mb-4">
            Historial de Precios
            <span className="text-sm font-normal text-slate-400 ml-2">(datos reales guardados día a día)</span>
          </h3>
          <div className="h-64 bg-slate-50 rounded-xl p-4">
            <HistoryChart
              dolarBlueHistory={marketData.dolarBlueHistory}
              dolarOficialHistory={marketData.dolarOficialHistory}
              goldHistory={marketData.goldHistory}
            />
          </div>
        </div>
        <p className="text-xs text-slate-400 mt-4 text-right">
          Última actualización: {new Date(marketData.lastUpdate).toLocaleString('es-AR')}
        </p>
      </>
    );
  };

  return (
    <div className="bg-white rounded-2xl shadow-2xl shadow-slate-300/30 p-6 md:p-8">
      <div className="text-center mb-6">
        <h2 className="text-2xl font-bold text-slate-800">Dashboard de Mercado</h2>
        <p className="text-slate-500 mt-1 text-sm">Datos reales · actualización cada 1h</p>
      </div>
      {renderContent()}
    </div>
  );
};

export default Dashboard;

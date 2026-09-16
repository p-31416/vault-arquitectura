import React, { useState, useEffect, useMemo, useCallback } from 'react';
import FeeCalculator from './components/FeeCalculator';
import Dashboard from './components/Dashboard';
import Budget from './components/Budget';
import Header from './components/Header';
import SavedBudgets from './components/SavedBudgets';
import { calculateFee, calcularMedicion } from './utils/feeCalculator';
import { getArgentinianMarketData } from './services/marketApi';
import { MIN_SQM, MARKET_REFRESH_INTERVAL } from './constants';
import type { MarketData, FeeCalculationResult, ServiceOptions, MediciónResult } from './types';

const DEFAULT_LOCAL_PREMIUM = 10;

const App: React.FC = () => {
  const [squareMeters, setSquareMeters] = useState<number>(MIN_SQM);
  const [marketData, setMarketData] = useState<MarketData | null>(null);
  const [loadingMarketData, setLoadingMarketData] = useState<boolean>(true);
  const [activeTab, setActiveTab] = useState<'calculator' | 'saved'>('calculator');
  const [localPremium, setLocalPremium] = useState<number>(DEFAULT_LOCAL_PREMIUM);

  const [services, setServices] = useState<ServiceOptions>({
    medicion: false,
    digitalizacion: false,
    adaptacionExterna: false,
  });

  const fetchData = useCallback(async () => {
    try {
      setLoadingMarketData(true);
      const data = await getArgentinianMarketData(localPremium);
      setMarketData(data);
    } catch (error) {
      console.error('Failed to fetch market data:', error);
      setMarketData(null);
    } finally {
      setLoadingMarketData(false);
    }
  }, [localPremium]);

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, MARKET_REFRESH_INTERVAL);
    return () => clearInterval(interval);
  }, [fetchData]);

  const feeData: FeeCalculationResult = useMemo(() => {
    return calculateFee(squareMeters);
  }, [squareMeters]);

  const medicionData: MediciónResult | null = useMemo(() => {
    if (!services.medicion) return null;
    return calcularMedicion(squareMeters);
  }, [squareMeters, services.medicion]);

  return (
    <div className="bg-slate-50 min-h-screen font-sans">
      <Header />
      <main className="container mx-auto p-4 md:p-8">
        <div className="mb-8 flex justify-center space-x-4">
          <TabButton tab="calculator" activeTab={activeTab} onTabChange={setActiveTab}>Calculadora</TabButton>
          <TabButton tab="saved" activeTab={activeTab} onTabChange={setActiveTab}>Presupuestos Guardados</TabButton>
        </div>

        {activeTab === 'calculator' && (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-start">
            <div className="lg:col-span-1">
              <FeeCalculator
                squareMeters={squareMeters}
                onSquareMetersChange={setSquareMeters}
                feeData={feeData}
                services={services}
                onServicesChange={setServices}
                medicionData={medicionData}
              />
            </div>
            <div className="lg:col-span-2 flex flex-col gap-8">
              <Dashboard
                marketData={marketData}
                loading={loadingMarketData}
                localPremium={localPremium}
                onLocalPremiumChange={setLocalPremium}
              />
              <Budget
                feeData={feeData}
                medicionData={medicionData}
                marketData={marketData}
                loading={loadingMarketData}
                squareMeters={squareMeters}
                services={services}
              />
            </div>
          </div>
        )}

        {activeTab === 'saved' && <SavedBudgets />}
      </main>
      <footer className="text-center py-6 text-slate-400 text-xs">
        <p>Esta es una herramienta de estimación. Los valores son referenciales y no constituyen una oferta formal.</p>
        <p>Copyright © {new Date().getFullYear()}</p>
      </footer>
    </div>
  );
};

interface TabButtonProps {
  tab: 'calculator' | 'saved';
  activeTab: 'calculator' | 'saved';
  onTabChange: (tab: 'calculator' | 'saved') => void;
  children: React.ReactNode;
}

const TabButton: React.FC<TabButtonProps> = ({ tab, activeTab, onTabChange, children }) => (
  <button
    onClick={() => onTabChange(tab)}
    className={`px-4 py-2 text-sm font-medium rounded-md transition-colors ${
      activeTab === tab
        ? 'bg-indigo-600 text-white shadow'
        : 'text-slate-600 hover:bg-slate-200'
    }`}
    aria-current={activeTab === tab ? 'page' : undefined}
  >
    {children}
  </button>
);

export default App;

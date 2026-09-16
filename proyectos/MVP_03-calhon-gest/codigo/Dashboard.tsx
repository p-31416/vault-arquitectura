// FIX: Implemented the Dashboard component to display market data and charts, resolving the module error in App.tsx.
import React from 'react';
// FIX: Corrected import paths for root directory
import type { FeeCalculationResult, MarketData } from './types';
import HistoryChart from './components/HistoryChart';

const DollarIcon: React.FC<{className: string}> = ({ className }) => (
    <svg xmlns="http://www.w3.org/2000/svg" className={className} viewBox="0 0 24 24" fill="currentColor">
        <path d="M11.35 6.33a1 1 0 0 0-1.23.23L5.26 12.7a1 1 0 0 0 .87 1.5h2.37a1 1 0 0 1 0 2H6.13a1 1 0 0 0-.87 1.5l4.86 6.14a1 1 0 0 0 1.23.23l4.86-6.14a1 1 0 0 0-.87-1.5h-2.37a1 1 0 0 1 0-2h2.37a1 1 0 0 0 .87-1.5L12.58 6.56a1 1 0 0 0-1.23-.23ZM12 8.78l2.44 3.08H9.56L12 8.78Zm0 9.54-2.44-3.08h4.88L12 18.32Z" />
    </svg>
);

const GoldIcon: React.FC<{ className: string }> = ({ className }) => (
    <svg xmlns="http://www.w3.org/2000/svg" className={className} viewBox="0 0 24 24" fill="currentColor">
        <path fillRule="evenodd" d="M2.25 5.625A3.375 3.375 0 0 1 5.625 2.25h12.75c1.86 0 3.375 1.515 3.375 3.375v12.75A3.375 3.375 0 0 1 18.375 21.75H5.625A3.375 3.375 0 0 1 2.25 18.375V5.625Zm3.375-.75a.75.75 0 0 0-.75.75v12.75c0 .414.336.75.75.75h12.75a.75.75 0 0 0 .75-.75V5.625a.75.75 0 0 0-.75-.75H5.625Z" clipRule="evenodd" />
        <path d="M6 15a.75.75 0 0 1 .75-.75h10.5a.75.75 0 0 1 0 1.5H6.75A.75.75 0 0 1 6 15Z" />
    </svg>
);

interface DashboardProps {
    feeData: FeeCalculationResult;
    marketData: MarketData | null;
    loading: boolean;
}

const Dashboard: React.FC<DashboardProps> = ({ feeData, marketData, loading }) => {
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
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div className="bg-slate-50 p-6 rounded-xl flex items-center">
                        <DollarIcon className="h-10 w-10 text-blue-500 mr-5" />
                        <div>
                            <p className="text-sm text-slate-500">Dólar Blue (Venta)</p>
                            <p className="text-2xl font-bold text-slate-800">
                                {new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS' }).format(marketData.dolarBlue.venta)}
                            </p>
                        </div>
                    </div>
                    <div className="bg-slate-50 p-6 rounded-xl flex items-center">
                        <GoldIcon className="h-10 w-10 text-amber-500 mr-5" />
                        <div>
                            <p className="text-sm text-slate-500">Oro (por gramo)</p>
                            <p className="text-2xl font-bold text-slate-800">
                                {new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS' }).format(marketData.gold.precio)}
                            </p>
                        </div>
                    </div>
                </div>
                <div className="mt-8">
                    <h3 className="text-lg font-bold text-slate-700 mb-4">
                        Historial de Precios (Últimos 30 días)
                    </h3>
                    <div className="h-64 bg-slate-50 rounded-xl p-4">
                        <HistoryChart dolarHistory={marketData.dolarHistory} goldHistory={marketData.goldHistory} />
                    </div>
                </div>
            </>
        );
    };

    return (
        <div className="bg-white rounded-2xl shadow-2xl shadow-slate-300/30 p-8 md:p-10">
            <div className="text-center mb-8">
                <h2 className="text-3xl font-bold text-slate-800">Dashboard de Mercado</h2>
                <p className="text-slate-500 mt-2">Valores de referencia para el cálculo.</p>
            </div>
            {renderContent()}
        </div>
    );
};

export default Dashboard;
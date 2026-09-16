import React, { useState, useEffect } from 'react';
import type { SavedBudget } from '../types';
import { getSavedBudgets, deleteBudget } from '../utils/storage';

const formatARS = (value: number) =>
  new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS', maximumFractionDigits: 0 }).format(value);

const NoBudgets: React.FC = () => (
  <div className="text-center py-16 bg-white rounded-2xl shadow-2xl shadow-slate-300/30">
    <svg className="mx-auto h-12 w-12 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
      <path vectorEffect="non-scaling-stroke" strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 13h6m-3-3v6m-9 1V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z" />
    </svg>
    <h3 className="mt-2 text-sm font-medium text-slate-900">No hay presupuestos</h3>
    <p className="mt-1 text-sm text-slate-500">Comienza guardando un presupuesto desde la calculadora.</p>
  </div>
);

const SavedBudgets: React.FC = () => {
  const [budgets, setBudgets] = useState<SavedBudget[]>([]);

  useEffect(() => {
    setBudgets(getSavedBudgets());
  }, []);

  const handleDelete = (id: string) => {
    if (window.confirm('¿Eliminar este presupuesto?')) {
      const updated = deleteBudget(id);
      setBudgets(updated);
    }
  };

  if (budgets.length === 0) {
    return <NoBudgets />;
  }

  return (
    <div className="bg-white rounded-2xl shadow-2xl shadow-slate-300/30 p-6 md:p-8">
      <div className="text-center mb-6">
        <h2 className="text-3xl font-bold text-slate-800">Presupuestos Guardados</h2>
        <p className="text-slate-500 mt-1">Tus presupuestos guardados</p>
      </div>
      <ul className="space-y-3">
        {budgets.map((budget) => (
          <li key={budget.id} className="bg-slate-50 p-4 rounded-lg flex items-center justify-between hover:shadow-md transition-shadow">
            <div className="flex-1">
              <p className="font-bold text-lg text-indigo-700">{budget.managementName}</p>
              <div className="text-sm text-slate-500 mt-1 flex flex-wrap gap-x-4 gap-y-1">
                <span>{new Date(budget.savedAt).toLocaleDateString('es-AR')}</span>
                <span>{budget.squareMeters} m²</span>
                {budget.services?.medicion && <span className="text-indigo-500">+ Medición</span>}
                <span className="font-semibold text-emerald-600">
                  Total: {formatARS(budget.totalARS || budget.averagePrice)}
                </span>
              </div>
            </div>
            <button
              onClick={() => handleDelete(budget.id)}
              className="p-2 text-slate-400 hover:text-red-600 hover:bg-red-100 rounded-full transition-colors"
              aria-label="Eliminar presupuesto"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clipRule="evenodd" />
              </svg>
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SavedBudgets;

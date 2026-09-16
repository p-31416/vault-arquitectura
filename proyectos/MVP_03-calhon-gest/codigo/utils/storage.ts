
import type { SavedBudget } from '../types';

const STORAGE_KEY = 'architect_budgets_v1';

export const getSavedBudgets = (): SavedBudget[] => {
  try {
    const budgetsJSON = localStorage.getItem(STORAGE_KEY);
    if (!budgetsJSON) return [];
    const budgets = JSON.parse(budgetsJSON) as SavedBudget[];
    return budgets.sort((a, b) => new Date(b.savedAt).getTime() - new Date(a.savedAt).getTime());
  } catch (error) {
    console.error("Failed to retrieve budgets from localStorage:", error);
    localStorage.removeItem(STORAGE_KEY);
    return [];
  }
};

export const saveBudget = (budget: SavedBudget): SavedBudget[] => {
  try {
    const budgets = getSavedBudgets();
    const existingIndex = budgets.findIndex(b => b.id === budget.id);
    if (existingIndex > -1) {
        budgets[existingIndex] = budget;
    } else {
        budgets.unshift(budget);
    }
    localStorage.setItem(STORAGE_KEY, JSON.stringify(budgets));
    return getSavedBudgets();
  } catch (error) {
    console.error("Failed to save budget to localStorage:", error);
    return getSavedBudgets();
  }
};

export const deleteBudget = (budgetId: string): SavedBudget[] => {
  try {
    let budgets = getSavedBudgets();
    budgets = budgets.filter(b => b.id !== budgetId);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(budgets));
    return budgets;
  } catch (error) {
    console.error("Failed to delete budget from localStorage:", error);
    return getSavedBudgets();
  }
};

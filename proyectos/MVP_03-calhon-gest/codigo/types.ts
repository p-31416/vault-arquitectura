export interface FeeCalculationResult {
  pricePerSqm: number;
  totalFee: number;
  goldPricePerSqm: number;
  totalGoldFee: number;
}

export interface MediciónResult {
  total: number;
  formula: string;
}

export interface ServiceOptions {
  medicion: boolean;
  digitalizacion: boolean;
  adaptacionExterna: boolean;
}

export interface MarketData {
  dolarBlue: { venta: number; compra: number };
  dolarOficial: { venta: number; compra: number };
  gold24k: {
    precioPorGramo: number;
    precioPorOnza: number;
  };
  lastUpdate: string;
  dolarBlueHistory: { date: string; value: number }[];
  dolarOficialHistory: { date: string; value: number }[];
  goldHistory: { date: string; value: number }[];
}

export interface SavedBudget {
  id: string;
  managementName: string;
  squareMeters: number;
  services: ServiceOptions;
  feeData: FeeCalculationResult;
  medicionData: MediciónResult | null;
  marketData: MarketData;
  averagePrice: number;
  totalARS: number;
  savedAt: string;
}

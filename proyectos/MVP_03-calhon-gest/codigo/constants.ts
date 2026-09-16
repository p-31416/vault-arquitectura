export const MIN_SQM = 50;
export const MAX_SQM = 300;

export const PRICE_AT_MIN_SQM = 25;
export const PRICE_AT_MAX_SQM = 70 / 9;

export const GOLD_TOTAL_FEE_POINTS = [
  { sqm: 50, totalFee: 9.5 },
  { sqm: 100, totalFee: 11.0 },
  { sqm: 200, totalFee: 14.0 },
  { sqm: 300, totalFee: 16.5 },
];

export const CPAU_K = 623849763.77;

export const MEDICION_MUY_COMPARTIMENTADA = {
  hasta50: (S: number) => 0.000004 * CPAU_K * S + 0.0003 * CPAU_K,
  de51a500: (S: number) => 0.000006 * CPAU_K * S + 0.0003 * CPAU_K,
  de501a2500: (S: number) => 0.000003 * CPAU_K * S + 0.0018 * CPAU_K,
  mas2500: (S: number) => 0.0000015 * CPAU_K * S + 0.00555 * CPAU_K,
};

export const MARKET_REFRESH_INTERVAL = 60 * 60 * 1000;

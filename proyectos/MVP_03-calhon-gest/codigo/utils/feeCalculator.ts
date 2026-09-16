import { FeeCalculationResult, MediciónResult } from '../types';
import {
  MIN_SQM,
  MAX_SQM,
  PRICE_AT_MIN_SQM,
  PRICE_AT_MAX_SQM,
  GOLD_TOTAL_FEE_POINTS,
  MEDICION_MUY_COMPARTIMENTADA,
} from '../constants';

export const calculateFee = (sqm: number): FeeCalculationResult => {
  const clampedSqm = Math.max(MIN_SQM, Math.min(sqm, MAX_SQM));

  const totalFeeAtMin = MIN_SQM * PRICE_AT_MIN_SQM;
  const totalFeeAtMax = MAX_SQM * PRICE_AT_MAX_SQM;
  const slope = (totalFeeAtMax - totalFeeAtMin) / (MAX_SQM - MIN_SQM);
  const yIntercept = totalFeeAtMin - slope * MIN_SQM;

  const totalFee = slope * clampedSqm + yIntercept;
  const pricePerSqm = totalFee / clampedSqm;

  let totalGoldFee = 0;
  let p1 = GOLD_TOTAL_FEE_POINTS[0];
  let p2 = GOLD_TOTAL_FEE_POINTS[1];

  for (let i = 0; i < GOLD_TOTAL_FEE_POINTS.length - 1; i++) {
    if (clampedSqm >= GOLD_TOTAL_FEE_POINTS[i].sqm && clampedSqm <= GOLD_TOTAL_FEE_POINTS[i + 1].sqm) {
      p1 = GOLD_TOTAL_FEE_POINTS[i];
      p2 = GOLD_TOTAL_FEE_POINTS[i + 1];
      break;
    }
  }

  const goldSlope = (p2.totalFee - p1.totalFee) / (p2.sqm - p1.sqm);
  const goldYIntercept = p1.totalFee - goldSlope * p1.sqm;
  totalGoldFee = goldSlope * clampedSqm + goldYIntercept;
  const goldPricePerSqm = totalGoldFee / clampedSqm;

  return { pricePerSqm, totalFee, goldPricePerSqm, totalGoldFee };
};

export const calcularMedicion = (sqm: number): MediciónResult => {
  const clampedSqm = Math.max(1, sqm);

  let total: number;
  let formula: string;

  if (clampedSqm <= 50) {
    total = MEDICION_MUY_COMPARTIMENTADA.hasta50(clampedSqm);
    formula = '0.000004 × K × S + 0.0003 × K';
  } else if (clampedSqm <= 500) {
    total = MEDICION_MUY_COMPARTIMENTADA.de51a500(clampedSqm);
    formula = '0.000006 × K × S + 0.0003 × K';
  } else if (clampedSqm <= 2500) {
    total = MEDICION_MUY_COMPARTIMENTADA.de501a2500(clampedSqm);
    formula = '0.000003 × K × S + 0.0018 × K';
  } else {
    total = MEDICION_MUY_COMPARTIMENTADA.mas2500(clampedSqm);
    formula = '0.0000015 × K × S + 0.00555 × K';
  }

  return { total: Math.round(total), formula };
};

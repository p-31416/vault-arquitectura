import type { MarketData } from '../types';

const HISTORY_DAYS = 30;
const SNAPSHOTS_KEY = 'market_snapshots';
const ONZA_EN_GRAMOS = 31.1035;

const BLUELYTICS_URL = 'https://api.bluelytics.com.ar/v2/latest';
const GOLD_API_URL = 'https://api.gold-api.com/price/XAU';

interface SnapshotEntry {
  date: string;
  dolarBlue: number;
  dolarOficial: number;
  goldARS: number;
}

const getSavedSnapshots = (): SnapshotEntry[] => {
  try {
    const raw = localStorage.getItem(SNAPSHOTS_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
};

const saveSnapshot = (entry: SnapshotEntry) => {
  try {
    const snapshots = getSavedSnapshots();
    const idx = snapshots.findIndex((s) => s.date === entry.date);
    if (idx >= 0) {
      snapshots[idx] = entry;
    } else {
      snapshots.push(entry);
    }
    snapshots.sort((a, b) => a.date.localeCompare(b.date));
    const max = HISTORY_DAYS * 2;
    if (snapshots.length > max) snapshots.splice(0, snapshots.length - max);
    localStorage.setItem(SNAPSHOTS_KEY, JSON.stringify(snapshots));
  } catch {
    /* localStorage maybe full */
  }
};

export const buildHistoryFromSnapshots = <T extends 'dolarBlue' | 'dolarOficial' | 'goldARS'>(
  key: T,
): { date: string; value: number }[] => {
  const snapshots = getSavedSnapshots();
  return [...snapshots]
    .sort((a, b) => a.date.localeCompare(b.date))
    .filter((s) => s[key])
    .map((s) => ({ date: s.date, value: s[key] as number }));
};

const fetchBluelytics = async () => {
  const resp = await fetch(BLUELYTICS_URL);
  if (!resp.ok) throw new Error(`Bluelytics error: ${resp.status}`);
  return resp.json();
};

const fetchGoldUSD = async () => {
  const resp = await fetch(GOLD_API_URL);
  if (!resp.ok) throw new Error(`Gold API error: ${resp.status}`);
  return resp.json();
};

export const getArgentinianMarketData = async (
  localPremiumPct: number,
): Promise<MarketData> => {
  const [bluelytics, goldData] = await Promise.all([
    fetchBluelytics(),
    fetchGoldUSD(),
  ]);

  const dolarOficialVenta = bluelytics.oficial.value_sell;
  const dolarOficialCompra = bluelytics.oficial.value_buy;
  const dolarBlueVenta = bluelytics.blue.value_sell;
  const dolarBlueCompra = bluelytics.blue.value_buy;

  const goldUSDperOz = goldData.price;
  const goldSpotARS = (goldUSDperOz / ONZA_EN_GRAMOS) * dolarOficialVenta;
  const goldFinalARS = Math.round(goldSpotARS * (1 + localPremiumPct / 100) * 100) / 100;

  const today = new Date().toISOString().split('T')[0];
  saveSnapshot({ date: today, dolarBlue: dolarBlueVenta, dolarOficial: dolarOficialVenta, goldARS: goldFinalARS });

  return {
    dolarBlue: { venta: dolarBlueVenta, compra: dolarBlueCompra },
    dolarOficial: { venta: dolarOficialVenta, compra: dolarOficialCompra },
    gold24k: {
      precioPorGramo: goldFinalARS,
      precioPorOnza: Math.round(goldFinalARS * ONZA_EN_GRAMOS * 100) / 100,
    },
    lastUpdate: bluelytics.last_update || new Date().toISOString(),
    dolarBlueHistory: buildHistoryFromSnapshots('dolarBlue'),
    dolarOficialHistory: buildHistoryFromSnapshots('dolarOficial'),
    goldHistory: buildHistoryFromSnapshots('goldARS'),
  };
};

export const getGoldSpotARS = async (): Promise<{ spotUSD: number; spotARS: number }> => {
  const [bluelytics, goldData] = await Promise.all([
    fetchBluelytics(),
    fetchGoldUSD(),
  ]);
  const spotUSD = goldData.price / ONZA_EN_GRAMOS;
  const spotARS = spotUSD * bluelytics.oficial.value_sell;
  return { spotUSD, spotARS };
};

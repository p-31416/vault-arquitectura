import React, { useEffect, useRef, useMemo } from 'react';
import { calculateFee } from '../utils/feeCalculator';
import { MIN_SQM, MAX_SQM } from '../constants';

declare global {
  interface Window {
    Chart: any;
  }
}

interface ChartDataPoint {
  x: number;
  yUsd: number;
  yGold: number;
}

interface FeeChartProps {
  currentSqm: number;
  currentPrice: number;
  currentGoldPrice: number;
}

const FeeChart: React.FC<FeeChartProps> = ({ currentSqm, currentPrice, currentGoldPrice }) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const chartRef = useRef<any>(null);

  const chartData = useMemo(() => {
    const data: ChartDataPoint[] = [];
    const steps = 30;
    const stepSize = (MAX_SQM - MIN_SQM) / steps;
    
    for (let i = 0; i <= steps; i++) {
      const sqm = MIN_SQM + (i * stepSize);
      const { pricePerSqm, goldPricePerSqm } = calculateFee(sqm);
      data.push({ x: sqm, yUsd: pricePerSqm, yGold: goldPricePerSqm });
    }
    return data;
  }, []);

  useEffect(() => {
    if (!canvasRef.current || !window.Chart) {
      return;
    }

    if (!chartRef.current) {
        const ctx = canvasRef.current.getContext('2d');
        if (!ctx) return;
        
        chartRef.current = new window.Chart(ctx, {
            type: 'line',
            data: { datasets: [] },
            options: {
              responsive: true,
              maintainAspectRatio: false,
              plugins: {
                legend: { display: false },
                tooltip: {
                  mode: 'index',
                  intersect: false,
                  callbacks: {
                    title: (tooltipItems: any) => `${tooltipItems[0].raw.x.toFixed(0)} m²`,
                    label: (context: any) => {
                      let label = context.dataset.label || '';
                      if (label) {
                          label = label.replace('Curva de Precio ', '');
                          label += ': ';
                      }
                      if (context.parsed.y !== null) {
                          const isUsd = context.dataset.yAxisID === 'yUsd';
                          const value = context.parsed.y;
                          label += isUsd 
                              ? `$${value.toFixed(2)} /m²` 
                              : `${value.toFixed(4)} gr/m²`;
                      }
                      return label;
                    },
                  },
                },
              },
              scales: {
                x: {
                  type: 'linear',
                  title: { display: true, text: 'Metros Cuadrados (m²)', color: '#64748b' },
                  grid: { display: false },
                  ticks: { color: '#94a3b8' },
                },
                yUsd: {
                  type: 'linear',
                  position: 'left',
                  title: { display: true, text: 'Precio por m² (USD)', color: '#4f46e5' },
                  grid: { color: '#f1f5f9' },
                  ticks: {
                    color: '#6366f1',
                    callback: (value: any) => `$${Number(value).toFixed(0)}`,
                  },
                },
                yGold: {
                  type: 'linear',
                  position: 'right',
                  title: { display: true, text: 'Precio por m² (Oro)', color: '#ca8a04' },
                  grid: { drawOnChartArea: false },
                  ticks: {
                    color: '#f59e0b',
                    callback: (value: any) => `${Number(value).toFixed(3)}gr`,
                  },
                },
              },
              interaction: { mode: 'index', intersect: false },
            },
        });
    }

    chartRef.current.data.datasets = [
        {
            label: 'Curva de Precio USD',
            data: chartData.map(p => ({ x: p.x, y: p.yUsd })),
            borderColor: '#818cf8',
            yAxisID: 'yUsd',
            borderWidth: 2,
            pointRadius: 0,
            tension: 0.4,
            fill: { target: 'origin', above: 'rgba(79, 70, 229, 0.05)' },
        },
        {
            label: 'Curva de Precio Oro',
            data: chartData.map(p => ({ x: p.x, y: p.yGold })),
            borderColor: '#fbbf24',
            yAxisID: 'yGold',
            borderWidth: 2,
            pointRadius: 0,
            tension: 0.4,
        },
        {
            label: 'Selección Actual USD',
            data: [{ x: currentSqm, y: currentPrice }],
            backgroundColor: '#4f46e5',
            borderColor: '#ffffff',
            borderWidth: 2,
            pointRadius: 6,
            pointHoverRadius: 8,
            type: 'bubble',
            yAxisID: 'yUsd',
        },
        {
            label: 'Selección Actual Oro',
            data: [{ x: currentSqm, y: currentGoldPrice }],
            backgroundColor: '#f59e0b',
            borderColor: '#ffffff',
            borderWidth: 2,
            pointRadius: 6,
            pointHoverRadius: 8,
            type: 'bubble',
            yAxisID: 'yGold',
        },
    ];
    
    chartRef.current.update();

  }, [chartData, currentSqm, currentPrice, currentGoldPrice]);

  return <canvas ref={canvasRef} role="img" aria-label="Gráfico de curva de precios por metro cuadrado en USD y Oro"></canvas>;
};

export default FeeChart;

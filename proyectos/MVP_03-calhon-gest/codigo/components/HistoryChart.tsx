import React, { useEffect, useRef } from 'react';

declare global {
  interface Window {
    Chart: any;
  }
}

interface HistoryDataPoint {
  date: string;
  value: number;
}

interface HistoryChartProps {
  dolarBlueHistory: HistoryDataPoint[];
  dolarOficialHistory: HistoryDataPoint[];
  goldHistory: HistoryDataPoint[];
}

const getPointRadius = (len: number) => {
  if (len <= 5) return 5;
  if (len <= 15) return 2;
  return 0;
};

const HistoryChart: React.FC<HistoryChartProps> = ({ dolarBlueHistory, dolarOficialHistory, goldHistory }) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const chartRef = useRef<any>(null);

  useEffect(() => {
    if (!canvasRef.current || !window.Chart) return;
    if (!dolarBlueHistory.length && !dolarOficialHistory.length && !goldHistory.length) return;

    const ctx = canvasRef.current.getContext('2d');
    if (!ctx) return;

    if (chartRef.current) {
      chartRef.current.destroy();
    }

    const pointRadius = getPointRadius(dolarBlueHistory.length);

    const datasets: any[] = [];

    if (dolarBlueHistory.length) {
      datasets.push({
        label: 'Dólar Blue (Venta)',
        data: dolarBlueHistory.map(d => d.value),
        borderColor: 'rgba(59, 130, 246, 0.8)',
        backgroundColor: 'rgba(59, 130, 246, 0.1)',
        yAxisID: 'yARS',
        tension: 0.3,
        pointRadius,
        fill: false,
      });
    }

    if (dolarOficialHistory.length) {
      datasets.push({
        label: 'Dólar Oficial (Venta)',
        data: dolarOficialHistory.map(d => d.value),
        borderColor: 'rgba(16, 185, 129, 0.8)',
        backgroundColor: 'rgba(16, 185, 129, 0.1)',
        yAxisID: 'yARS',
        tension: 0.3,
        pointRadius,
        fill: false,
        borderDash: [5, 5],
      });
    }

    if (goldHistory.length) {
      datasets.push({
        label: 'Oro 24K (gr)',
        data: goldHistory.map(d => d.value),
        borderColor: 'rgba(245, 158, 11, 0.8)',
        backgroundColor: 'rgba(245, 158, 11, 0.1)',
        yAxisID: 'yGold',
        tension: 0.3,
        pointRadius,
        fill: false,
      });
    }

    const labels = dolarBlueHistory.length
      ? dolarBlueHistory.map(d => new Date(d.date).toLocaleDateString('es-AR', { day: '2-digit', month: '2-digit' }))
      : dolarOficialHistory.length
        ? dolarOficialHistory.map(d => new Date(d.date).toLocaleDateString('es-AR', { day: '2-digit', month: '2-digit' }))
        : goldHistory.map(d => new Date(d.date).toLocaleDateString('es-AR', { day: '2-digit', month: '2-digit' }));

    chartRef.current = new window.Chart(ctx, {
      type: 'line',
      data: { labels, datasets },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: { mode: 'index', intersect: false },
        plugins: {
          legend: { position: 'bottom' },
          tooltip: {
            callbacks: {
              label: function (context: any) {
                let label = context.dataset.label || '';
                if (label) label += ': ';
                if (context.parsed.y !== null) {
                  label += new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS' }).format(context.parsed.y);
                }
                return label;
              },
            },
          },
        },
        scales: {
          x: {
            grid: { display: false },
            ticks: { maxTicksLimit: 8, autoSkip: true },
          },
          yARS: {
            type: 'linear',
            position: 'left',
            title: { display: true, text: 'ARS', color: '#64748b' },
            grid: { color: '#f1f5f9' },
            min: 1400,
            max: 1600,
            ticks: {
              callback: (value: any) => `$${Number(value).toFixed(0)}`,
            },
          },
          yGold: {
            type: 'linear',
            position: 'right',
            title: { display: true, text: 'Oro (ARS por gr)', color: 'rgba(245, 158, 11, 1)' },
            grid: { drawOnChartArea: false },
            ticks: {
              callback: (value: any) => `$${Number(value / 1000).toFixed(0)}k`,
            },
          },
        },
      },
    });

    return () => {
      if (chartRef.current) {
        chartRef.current.destroy();
      }
    };
  }, [dolarBlueHistory, dolarOficialHistory, goldHistory]);

  return <canvas ref={canvasRef} role="img" aria-label="Gráfico de historial de precios"></canvas>;
};

export default HistoryChart;

import React, { useEffect, useRef } from 'react';

declare global {
  interface Window {
    Chart: any;
  }
}

interface BudgetChartProps {
  dolarValue: number;
  goldValue: number;
  averageValue: number;
}

// Define the utility function outside the component to ensure it's available.
const formatCurrency = (value: number) => new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS', maximumFractionDigits: 0 }).format(value);

const BudgetChart: React.FC<BudgetChartProps> = ({ dolarValue, goldValue, averageValue }) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const chartRef = useRef<any>(null);

  useEffect(() => {
    if (!canvasRef.current || !window.Chart) {
      return;
    }

    const ctx = canvasRef.current.getContext('2d');
    if (!ctx) return;

    if (chartRef.current) {
        chartRef.current.destroy();
    }
    
    const minValue = Math.min(dolarValue, goldValue);
    const diffValue = Math.abs(dolarValue - goldValue);
    const dolarIsMin = dolarValue <= goldValue;

    const labels = {
      min: dolarIsMin ? 'Costo Dólar' : 'Costo Oro',
      diff: dolarIsMin ? 'Diferencia a Oro' : 'Diferencia a Dólar',
    };
    
    const colors = {
      min: dolarIsMin ? 'rgba(79, 70, 229, 0.8)' : 'rgba(245, 158, 11, 0.8)',
      diff: dolarIsMin ? 'rgba(245, 158, 11, 0.8)' : 'rgba(79, 70, 229, 0.8)',
    };
    
    const borderColors = {
      min: dolarIsMin ? 'rgb(79, 70, 229)' : 'rgb(245, 158, 11)',
      diff: dolarIsMin ? 'rgb(245, 158, 11)' : 'rgb(79, 70, 229)',
    };

    const averageLinePlugin = {
      id: 'averageLine',
      afterDatasetsDraw: (chart: any) => {
        const { ctx, chartArea: { top, bottom }, scales: { x } } = chart;
        const xValue = x.getPixelForValue(averageValue);

        ctx.save();
        ctx.beginPath();
        ctx.moveTo(xValue, top);
        ctx.lineTo(xValue, bottom);
        ctx.lineWidth = 3;
        ctx.strokeStyle = 'rgba(239, 68, 68, 1)'; // Solid Red
        ctx.stroke();

        ctx.font = 'bold 12px sans-serif';
        ctx.fillStyle = 'rgba(239, 68, 68, 1)';
        ctx.textAlign = 'center';
        ctx.fillText('Promedio', xValue, top - 8);
        ctx.restore();
      },
    };
        
    chartRef.current = new window.Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Análisis Comparativo'],
            datasets: [
              {
                  label: labels.min,
                  data: [minValue],
                  backgroundColor: colors.min,
                  borderColor: borderColors.min,
                  borderWidth: 1,
              },
              {
                  label: labels.diff,
                  data: [diffValue],
                  backgroundColor: colors.diff,
                  borderColor: borderColors.diff,
                  borderWidth: 1,
              }
            ]
        },
        plugins: [averageLinePlugin],
        options: {
            indexAxis: 'y', // This makes the bar chart horizontal
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: true,
                    position: 'bottom',
                },
                tooltip: {
                    callbacks: {
                        label: function(context: any) {
                            const datasetLabel = context.dataset.label || '';
                            const value = context.parsed.x; // Use .x for horizontal chart
                            if (datasetLabel.startsWith('Diferencia')) {
                                return `${datasetLabel}: ${formatCurrency(value)}`;
                            }
                            return `${datasetLabel}: ${formatCurrency(value)}`;
                        },
                        footer: function(tooltipItems: any) {
                            const total = tooltipItems.reduce((sum: number, item: any) => sum + item.parsed.x, 0);
                            return `Valor Máximo: ${formatCurrency(total)}`;
                        }
                    }
                }
            },
            scales: {
                x: { // Value axis is now X
                    stacked: true,
                    suggestedMin: minValue * 0.98, // Start axis near the data for better visibility
                    title: {
                        display: true,
                        text: 'Costo Total en Pesos (ARS)',
                        color: '#64748b'
                    },
                    ticks: {
                        color: '#94a3b8',
                        callback: function(value: any) {
                             return formatCurrency(Number(value));
                        }
                    }
                },
                y: { // Category axis is now Y
                    stacked: true,
                    ticks: { display: false },
                    grid: { display: false }
                }
            }
        },
    });

    return () => {
        if(chartRef.current) {
            chartRef.current.destroy();
        }
    };
  }, [dolarValue, goldValue, averageValue]);

  return <canvas ref={canvasRef} role="img" aria-label="Gráfico de barras apiladas comparando los costos finales del presupuesto"></canvas>;
};

export default BudgetChart;
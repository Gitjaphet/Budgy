// Chart.js est chargé en amont via CDN (extra_js de resume.html).
// Cette fonction est appelée après chaque swap HTMX pour réinitialiser les graphiques.

window.initResumeCharts = function () {
    const catLabelsEl = document.getElementById('chart-cat-labels');
    const catDataEl = document.getElementById('chart-cat-data');
    const evoLabelsEl = document.getElementById('chart-evo-labels');
    const evoDataEl = document.getElementById('chart-evo-data');

    if (!catLabelsEl || !evoLabelsEl) return;

    const catLabels = JSON.parse(catLabelsEl.textContent);
    const catData = JSON.parse(catDataEl.textContent);
    const evoLabels = JSON.parse(evoLabelsEl.textContent);
    const evoData = JSON.parse(evoDataEl.textContent);

    const palette = ['#4f46e5', '#7c6ff0', '#a78bfa', '#c4b5fd', '#818cf8', '#c7d2fe'];

    const catCanvas = document.getElementById('chart-categories');
    if (catCanvas) {
        if (catCanvas._chartInstance) catCanvas._chartInstance.destroy();
        catCanvas._chartInstance = new Chart(catCanvas, {
            type: 'doughnut',
            data: {
                labels: catLabels,
                datasets: [{
                    data: catData,
                    backgroundColor: palette,
                    borderWidth: 0,
                }],
            },
            options: {
                responsive: true,
                cutout: '65%',
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { font: { family: 'Josefin Sans' }, padding: 16, usePointStyle: true },
                    },
                },
            },
        });
    }

    const evoCanvas = document.getElementById('chart-evolution');
    if (evoCanvas) {
        if (evoCanvas._chartInstance) evoCanvas._chartInstance.destroy();
        evoCanvas._chartInstance = new Chart(evoCanvas, {
            type: 'bar',
            data: {
                labels: evoLabels,
                datasets: [{
                    data: evoData,
                    backgroundColor: '#4f46e5',
                    borderRadius: 8,
                    maxBarThickness: 36,
                }],
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false } },
                scales: {
                    x: { grid: { display: false } },
                    y: { grid: { color: '#ececf5' }, beginAtZero: true },
                },
            },
        });
    }
};

document.addEventListener('DOMContentLoaded', () => {
    if (typeof Chart !== 'undefined') window.initResumeCharts();
});

// Réinitialise les graphiques après une navigation HTMX
document.addEventListener('htmx:afterSettle', () => {
    if (typeof Chart !== 'undefined' && document.getElementById('chart-categories')) {
        window.initResumeCharts();
    }
});
document.addEventListener("DOMContentLoaded", function() {
    // Fetch chart data and render chart
    fetch('/chart-data')
        .then(response => response.json())
        .then(data => {
            const categories = data.map(item => item[0]);
            const amounts = data.map(item => item[1]);

            const ctx = document.getElementById('expenseChart').getContext('2d');
            new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: categories,
                    datasets: [{
                        label: 'Expenses by Category',
                        data: amounts,
                        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF']
                    }]
                }
            });
        });
});
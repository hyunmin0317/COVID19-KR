function drawChart() {
    var data_week = new google.visualization.DataTable();
    data_week.addColumn('string', '날짜');
    data_week.addColumn('number', '확진자');
    data_week.addColumn({type:'number', role:'annotation'})
    data_week.addRows(week_data);
    var chart = new google.visualization.ColumnChart(document.getElementById('chart_week'));
    chart.draw(data_week, options);

    var data_year = new google.visualization.DataTable();
    data_year.addColumn('date', '날짜');
    data_year.addColumn('number', '확진자');
    data_year.addRows(year_data);
    var charts = new google.visualization.LineChart(document.getElementById('chart_year'));
    charts.draw(data_year, options);

    window.addEventListener('resize', drawChart, false)
}

var options = {
    colors: ['#F15F5F'],
    vAxis: {
        minValue: 0
    },
    width: '100%',
    height: 400,
};

google.charts.load('current', {'packages':['corechart', 'bar']});
google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawChart);

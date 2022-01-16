
// -------------------------------------------------------------------------------------------------------------------------------------------
// Dashboard 5 : Chart Init Js
// -------------------------------------------------------------------------------------------------------------------------------------------
$(function () {
    "use strict";
  
     // Stacked Bar Chart -------> BAR CHART
    var options_stacked = {
      series: [
        {
          name: "Maintenance Curative",
          data: [29, 37, 15, 48, 16],
        },
      ],
      chart: {
        fontFamily: '"Nunito Sans", sans-serif',
        type: "bar",
        height: 350,
        stacked: true,
        toolbar: {
          show: false,
        },
      },
      grid: {
        borderColor: "transparent",
      },
      colors: ["#6993ff", "#4fc3f7"],
      plotOptions: {
        bar: {
          horizontal: true,
        },
      },
      stroke: {
        width: 1,
        colors: ["#fff"],
      },
      xaxis: {
        categories: ['CVCD', 'Plomberie', 'Sprinklage','CFO', 'CFA'],
        labels: {
          formatter: function (val) {
            return val ;
          },
          style: {
            colors: [
              "#a1aab2",
              "#a1aab2",
              "#a1aab2",
              "#a1aab2",
              "#a1aab2",
              "#a1aab2",
              "#a1aab2",
            ],
          },
        },
      },
      tooltip: {
        y: {
          formatter: function (val) {
            return val ;
          },
        },
        theme: "dark",
      },
      fill: {
        opacity: 1,
      },
      legend: {
        position: "top",
        horizontalAlign: "left",
        offsetX: 40,
        labels: {
          colors: ["#a1aab2"],
        },
      },
    };
  
    var chart_bar_stacked = new ApexCharts(
      document.querySelector("#chart-bar-stacked"),
      options_stacked
    );
    chart_bar_stacked.render();
  
    // -----------------------------------------------------------------------
    // Etat Charts
    // -----------------------------------------------------------------------
  
    var option_Sales = {
      series: [49, 45, 22, 29],
      labels: ["Résolu", "En cours", "Enregistré", "En charge"],
      chart: {
        type: "donut",
        height: 270,
        fontFamily: '"Nunito Sans",sans-serif',
      },
      dataLabels: {
        enabled: false,
      },
      fill: {
        opacity: 1,
      },
      plotOptions: {
        pie: {
          expandOnClick: true,
          startAngle: 40,
          donut: {
            size: "70",
            labels: {
              show: true,
              name: {
                show: true,
                offsetY: -10,
                fontSize: "30px",
                fontFamily: "Arial",
                fontWeight: 500,
                color: "#a1aab2",
              },
              value: {
                show: true,
                fontSize: "18px",
                fontFamily: "Arial",
                fontWeight: 400,
                color: "#a1aab2",
              },
              total: {
                show: true,
                label: "Interventions",
                fontSize: "20px",
                fontFamily: "Arial",
                fontWeight: 500,
                color: "#a1aab2",
              },
            },
          },
        },
      },
      colors: ["#53e69d", "#f0ad4e", "#7d7d7d", "#7bcef3"],
      tooltip: {
        show: true,
        theme: "dark",
        fillSeriesColor: false,
      },
      legend: {
        show: false,
      },
      responsive: [
        {
          breakpoint: 426,
          options: {
            chart: {
              height: 250,
              width: 250,
              offsetX: -20,
            },
          },
        },
      ],
    };
  
    var chart_pie_donut = new ApexCharts(
      document.querySelector("#etat"),
      option_Sales
    );
    chart_pie_donut.render();
  
    // -----------------------------------------------------------------------
  });
  
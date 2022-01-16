
// -------------------------------------------------------------------------------------------------------------------------------------------
// Dashboard 5 : Chart Init Js
// -------------------------------------------------------------------------------------------------------------------------------------------
$(function () {
    "use strict";

    var options= {
        series: [{
            name: 'Intervention  Préventive Journaliére ',
            data: [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
          },
          {
            name: 'Intervention Préventive Hebdomadaire',
            data: [0,0,4,0,0,0,0,0,0,4,0,0,0,0,0,0,4,0,0,0,0,0,0,4,0,0,0,0,0,0,4]
          },
          {
            name: 'Intervention Préventive Mensuelle',
            data: [0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
          },
          {
            name: 'Intervention Préventive Trimestrielle',
            data: [0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
          },
          {
            name: 'Intervention Semestrielle',
            data: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,0]
          },
          {
            name: 'Intervention Annuelle',
            data: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,0,0,0,0,0,0,0,0,0]
          },
        ],
      chart: {
        fontFamily: '"Nunito Sans", sans-serif',
        type: "heatmap",
        height: 350,
      },
      plotOptions: {
        heatmap: {
          shadeIntensity: 0.5,
          radius: 0,
          useFillColorAsStroke: false,
          colorScale: {
            ranges: [{
                from: 0,
                to: 0.3,
                name: 'RAS',
                color: '#C0C0C0'
              },
                {
                from: 1,
                to: 2,
                name: 'Journalier',
                color: '#00A100'
              },
              {
                from: 3,
                to: 4,
                name: 'Hebdomadaire',
                color: '#128FD9'
              },
              {
                from: 5,
                to: 6,
                name: 'Mensuel',
                color: '#FFB200'
              },
              {
                from: 7,
                to: 8,
                name: 'Trimestriel',
                color: '#800000'
              },
              {
                from: 9,
                to: 10,
                name: 'Semestriel',
                color: '#800080'
              },
              {
                from: 11,
                to: 12,
                name: 'Annuel',
                color: '#FF0000'
              }
            ]
          }
        }
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        width: 1
      },
      legend: {
        show: true,
      },
      tooltip: {
        enabled: false,
      },
      yaxis: {
        labels: {
            maxWidth: 300,
        },
        },
    };
  
    var chart_heatmap = new ApexCharts(
      document.querySelector("#chart-heatmap"),
      options
    );
    chart_heatmap.render();
  
  });
  
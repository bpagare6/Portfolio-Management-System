var options1 = {
  series: [{ data: [25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54] }],
  fill: { colors: ["#5b73e8"] },
  chart: { type: "bar", width: 70, height: 40, sparkline: { enabled: !0 } },
  plotOptions: { bar: { columnWidth: "50%" } },
  labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
  xaxis: { crosshairs: { width: 1 } },
  tooltip: {
    fixed: { enabled: !1 },
    x: { show: !1 },
    y: {
      title: {
        formatter: function (e) {
          return "";
        },
      },
    },
    marker: { show: !1 },
  },
},
  chart1 = new ApexCharts(
    document.querySelector("#total-investment-chart"),
    options1
  );
chart1.render();
var options1 = {
  series: [{ data: [25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54] }],
  fill: { colors: ["#50a5f1"] },
  chart: { type: "bar", width: 70, height: 40, sparkline: { enabled: !0 } },
  plotOptions: { bar: { columnWidth: "50%" } },
  labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
  xaxis: { crosshairs: { width: 1 } },
  tooltip: {
    fixed: { enabled: !1 },
    x: { show: !1 },
    y: {
      title: {
        formatter: function (e) {
          return "";
        },
      },
    },
    marker: { show: !1 },
  },
},
  chart2 = new ApexCharts(
    document.querySelector("#current-value-chart"),
    options1
  );
chart2.render();
var options1 = {
  series: [{ data: [25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54] }],
  fill: { colors: ["#34c38f"] },
  chart: { type: "bar", width: 70, height: 40, sparkline: { enabled: !0 } },
  plotOptions: { bar: { columnWidth: "50%" } },
  labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
  xaxis: { crosshairs: { width: 1 } },
  tooltip: {
    fixed: { enabled: !1 },
    x: { show: !1 },
    y: {
      title: {
        formatter: function (e) {
          return "";
        },
      },
    },
    marker: { show: !1 },
  },
},
  chart3 = new ApexCharts(document.querySelector("#pnl-chart"), options1);
chart3.render();
var options2 = {
  series: [{ data: [25, 66, 41, 89, 63, 25, 44, 12, 36, 9, 54] }],
  fill: { colors: ["#f1b44c"] },
  chart: { type: "bar", width: 70, height: 40, sparkline: { enabled: !0 } },
  plotOptions: { bar: { columnWidth: "50%" } },
  labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
  xaxis: { crosshairs: { width: 1 } },
  tooltip: {
    fixed: { enabled: !1 },
    x: { show: !1 },
    y: {
      title: {
        formatter: function (e) {
          return "";
        },
      },
    },
    marker: { show: !1 },
  },
},
  chart2 = new ApexCharts(document.querySelector("#growth-chart"), options2);
chart2.render();
//dataset 1
var data = [
 {
    "EventId": "eef..105",
    "Breakpoint": 34,
    "Stepinto": 0,
    "Positionindex": 0
  },
  {
    "EventId": "e60..f11",
    "Breakpoint": 0,
    "Stepinto": 35,
    "Positionindex": 1

  },
  {
    "EventId": "9c2..dd9",
    "Breakpoint": 0,
    "Stepinto": 35,
    "Positionindex": 6
  },
  {
    "EventId": "8ff..63a",
    "Breakpoint": 0,
    "Stepinto": 38,
    "Positionindex": 8
  },
  {
    "EventId": "1fa..8b0",
    "Breakpoint": 0,
    "Stepinto": 40,
    "Positionindex": 8
  },
  {
    "EventId": "185..0e2",
    "Breakpoint": 0,
    "Stepinto": 42,
    "Positionindex": 9
  },
  {
  "EventId": "eb9..047",
  "Breakpoint": 0,
  "Stepinto": 70,
  "Positionindex": 10
}
];

//dataset 2
var data1 = [
{
      "EventId": "0de..cd2",
      "Breakpoint": 36,
      "Stepinto": 0,
      "Positionindex": 0
    },
    {
      "EventId": "419..c2e",
      "Breakpoint": 0,
      "Stepinto": 38,
      "Positionindex": 1

    },
    {
      "EventId": "236..e8b",
      "Breakpoint": 0,
      "Stepinto": 57,
      "Positionindex": 2
    },
    {
      "EventId": "f09..c74",
      "Breakpoint": 0,
      "Stepinto": 58,
      "Positionindex": 3
    },
    {
      "EventId": "576..52b",
      "Breakpoint": 0,
      "Stepinto": 59,
      "Positionindex": 4
    },
    {
      "EventId": "7e6..304",
      "Breakpoint": 0,
      "Stepinto": 60,
      "Positionindex": 5
    },
    {
    "EventId": "064..037",
    "Breakpoint": 0,
    "Stepinto": 62,
    "Positionindex": 6
    },
    {
    "EventId": "0a4..896",
    "Breakpoint": 0,
    "Stepinto": 62,
    "Positionindex": 35
    },
    {
  "EventId": "ff6..9e2",
  "Breakpoint": 0,
  "Stepinto": 66,
  "Positionindex": 36
  }
];

//dataset 3
var data2 = [
{
      "EventId": "f59..2cd",
      "Breakpoint": 0,
      "Stepinto": 14,
      "Positionindex": 7
    },
    {
      "EventId": "01b..47f",
      "Breakpoint": 0,
      "Stepinto": 15,
      "Positionindex": 8

    },
    {
      "EventId": "fb6..d64",
      "Breakpoint": 0,
      "Stepinto": 20,
      "Positionindex": 9
    },
    {
      "EventId": "ce2..55f",
      "Breakpoint": 0,
      "Stepinto": 24,
      "Positionindex": 10
    },
    {
      "EventId": "ec4..b66",
      "Breakpoint": 0,
      "Stepinto": 37,
      "Positionindex": 11
    },
    {
      "EventId": "df8..b96",
      "Breakpoint": 0,
      "Stepinto": 38,
      "Positionindex": 12
    },
    {
    "EventId": "403..61c",
    "Breakpoint": 0,
    "Stepinto": 39,
    "Positionindex": 13
    },
    {
    "EventId": "776..96c",
    "Breakpoint": 0,
    "Stepinto": 25,
    "Positionindex": 14
    },
    {
  "EventId": "686..89f",
  "Breakpoint": 0,
  "Stepinto": 42,
  "Positionindex": 15
  }
];

var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x0 = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var x1 = d3.scale.ordinal();

var y = d3.scale.linear()
    .range([height, 0]);

var color = d3.scale.ordinal()
    .range(["#ff8c00", "#8a89a6", "#a05d56"]);

var xAxis = d3.svg.axis()
    .scale(x0)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .tickFormat(d3.format(".2s"));

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var ageNames = d3.keys(data[0]).filter(function(key) { return key !== "EventId"; });

data.forEach(function(d) {
    d.ages = ageNames.map(function(name) { return {name: name, value: +d[name]}; });
    });

  x0.domain(data.map(function(d) { return d.EventId; }));
  x1.domain(ageNames).rangeRoundBands([0, x0.rangeBand()]);
  y.domain([0, d3.max(data, function(d) { return d3.max(d.ages, function(d) { return d.value; }); })]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("text")
    .attr("text-anchor", "middle")
    .attr("x", width-500)
    .attr("y", height + margin.top + 10)
    .text("Sequence of Events");

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Line of Code");

//Update input data
function update(datas) {

  var u = svg.selectAll(".groups")
    .data(datas)
    .enter().append("g")
    .attr("class", "groups")
    .attr("transform", function(d) { return "translate(" + x0(d.EventId) + ",0)"; });

  u.selectAll("rect")
      .data(function(d) { return d.ages; })
      .enter().append("rect")
      .attr("width", x1.rangeBand())
      .attr("x", function(d) { return x1(d.name); })
      .attr("y", function(d) { return y(d.value); })
      .attr("height", function(d) { return height - y(d.value); })
      .style("fill", function(d) { return color(d.name); });
}
update(data)

//Adding legends
var legend = svg.selectAll(".legend")
      .data(ageNames.slice().reverse())
      .enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

legend.append("rect")
      .attr("x", width +15 )
      .attr("width", 20)
      .attr("height", 18)
      .style("fill", color);

legend.append("text")
      .attr("x", width+10 )
      .attr("y", 9)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function(d) { return d; });

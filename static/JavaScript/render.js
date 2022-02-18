var lineChart = echarts.init(document.getElementById('lines'), 'white', {renderer: 'canvas'});

var slider = document.getElementById('slider');

document.getElementById('slider').onchange =  function changeDate(){
    fetchworldMapData(worldmap);
    fetchchinaMapData(chinamap);
}

document.getElementById('mapselecter').onchange = function changeCountry(){
    fetchworldMapData(worldmap);
    fetchchinaMapData(chinamap);
}

$(
    function () {
        fetchworldMapData(worldmap);
        fetchchinaMapData(chinamap);
        fetchlineData(lineChart)
        $.ajax({
            type: "GET",
            url: "/wordcloud",
            dataType: "json",
            success: function (result) {
                wordchart.setOption(result);
            }
        });
        $.ajax({
            type: "GET",
            url: "/weiboCloud",
            dataType: "json",
            success: function (result) {
                weibochart.setOption(result);
            }
        });
    }
);


function fetchlineData(chart) {
    $.ajax({
        type: "GET",
        url: "/lines",
        dataType: "json",
        success: function (result) {
            chart.setOption(result);
        }
    });
}



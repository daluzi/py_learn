 var chart = AmCharts.makeChart( "chartdiv", {
    "type": "serial",
    "theme": "none",
    "dataProvider": [ {
    "country": "重庆",
    "visits": 0
    }, {
    "country": "青岛",
    "visits": 0
    }, {
    "country": "西藏",
    "visits": 0
    }, {
    "country": "上海",
    "visits": 0
    }, {
    "country": "北京",
    "visits": 0
    }, {
    "country": "昆明",
    "visits": 0
    }, {
    "country": "厦门",
    "visits": 0
    }, {
    "country": "长沙",
    "visits": 0
    }, {
    "country": "成都",
    "visits": 0
    }, {
    "country": "青海",
    "visits": 0
    }, {
    "country": "内蒙",
    "visits": 0
    }, {
    "country": "武汉",
    "visits": 0
    }],
    "valueAxes": [ {
    "gridColor": "black",
    "gridAlpha": 0.2,
    "dashLength": 0
    } ],
    "gridAboveGraphs": true,
    "startDuration": 1,
    "graphs": [ {
    "balloonText": "[[category]]: <b>[[value]]</b>",
    "fillAlphas": 0.8,
    "lineAlpha": 0.2,
    "type": "column",
    "valueField": "visits"
    } ],
    "chartCursor": {
    "categoryBalloonEnabled": false,
    "cursorAlpha": 0,
    "zoomable": false
    },
    "categoryField": "country",
    "categoryAxis": {
    "gridPosition": "start",
    "gridAlpha": 0,
    "tickPosition": "start",
    "tickLength": 20
    },
    "export": {
    "enabled": true
    }

    } );

function hyfb(dbfare) {
    var chart = AmCharts.makeChart( "chartdiv", {
    "type": "serial",
    "theme": "none",
    "dataProvider": [ {
    "country": "重庆",
    "visits": dbfare[0]
    }, {
    "country": "青岛",
    "visits": dbfare[1]
    }, {
    "country": "西藏",
    "visits": dbfare[2]
    }, {
    "country": "上海",
    "visits": dbfare[3]
    }, {
    "country": "北京",
    "visits": dbfare[4]
    }, {
    "country": "昆明",
    "visits": dbfare[5]
    }, {
    "country": "厦门",
    "visits": dbfare[6]
    }, {
    "country": "长沙",
    "visits": dbfare[7]
    }, {
    "country": "成都",
    "visits": dbfare[8]
    }, {
    "country": "青海",
    "visits": dbfare[9]
    }, {
    "country": "内蒙",
    "visits": dbfare[10]
    }, {
    "country": "武汉",
    "visits": dbfare[11]
    }],
    "valueAxes": [ {
    "gridColor": "black",
    "gridAlpha": 0.2,
    "dashLength": 0
    } ],
    "gridAboveGraphs": true,
    "startDuration": 1,
    "graphs": [ {
    "balloonText": "[[category]]: <b>[[value]]</b>",
    "fillAlphas": 0.8,
    "lineAlpha": 0.2,
    "type": "column",
    "valueField": "visits"
    } ],
    "chartCursor": {
    "categoryBalloonEnabled": false,
    "cursorAlpha": 0,
    "zoomable": false
    },
    "categoryField": "country",
    "categoryAxis": {
    "gridPosition": "start",
    "gridAlpha": 0,
    "tickPosition": "start",
    "tickLength": 20
    },
    "export": {
    "enabled": true
    }

    } );
console.log(chart.dataProvider);
}
function Ajax(type, url, data, success, failed){
    // 创建ajax对象
    var xhr = null;
    if(window.XMLHttpRequest){
        xhr = new XMLHttpRequest();
    } else {
        xhr = new ActiveXObject('Microsoft.XMLHTTP')
    }
 
    var type = type.toUpperCase();
    // 用于清除缓存
    var random = Math.random();
 
    if(typeof data == 'object'){
        var str = '';
        for(var key in data){
            str += key+'='+data[key]+'&';
        }
        data = str.replace(/&$/, '');
    }
 
    if(type == 'GET'){
        if(data){
            xhr.open('GET', url + '?' + data, true);
        } else {
            xhr.open('GET', url + '?t=' + random, true);
        }
        xhr.send();
 
    } else if(type == 'POST'){
        xhr.open('POST', url, true);
        // 如果需要像 html 表单那样 POST 数据，请使用 setRequestHeader() 来添加 http 头。
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.send(data);
        console.log(data);
    }
 
    // 处理返回数据
    xhr.onreadystatechange = function(){
        if(xhr.readyState == 4){
            if(xhr.status == 200){
                success(xhr.responseText);
            } else {
                if(failed){
                    failed(xhr.status);
                }
            }
        }
    }
}

var from_ = document.querySelector("#from_"),
    costs = document.querySelector("#costs"),
    days = document.querySelector("#days");
var clickto = document.querySelector("#clickto");
var tovalue = document.querySelector("#to_");
// 测试调用
clickto.onclick =function() {
    fromvalue = from_.value;
    costsvalue = costs.value;
    daysvalue = days.value;
    var a = [],
        w = [];
    var sendData = {startName:fromvalue,budget:costsvalue,days:daysvalue};
    Ajax('post', 'https://gojay.xin/Journey/api/recommend', sendData, function(data){
        console.log(JSON.parse(data).body);
        var db = JSON.parse(data).body;
        var dbfare = [];
        for(let i = 0; i < db.length;i++) {
            if (db[i].budgetEnough) {
                a.push(db[i].summerScore);
                w.push(db[i].winterScore);
            }
            dbfare.push(db[i].fare);
            // chart.dataProvider[i].visits = db[i].fare;
        }
        hyfb(dbfare);
        // console.log(a);
        var amax = Math.max.apply(Math,a);
        var wmax = Math.max.apply(Math,w);
        for(let i = 0; i < db.length;i++) {
            if (db[i].summerScore == amax) {
                sb = db[i].countryName;
            }
            if (db[i].winterScore == wmax) {
                wb = db[i].countryName;
            }
        }
        // console.log(sb);
        tovalue.value = sb+"(冬季最佳："+wb+")";
        // console.log(tovalue);
        searchByStationName2();
        getDistance();
    }, function(error){
        console.log(error);
    });
}
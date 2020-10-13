/*jslint browser: true*/
/*global $*/
// 这时来自本地的数据做的json接口数据
// $(document).ready(function () {
//   $.get('/tabledata', function (data) {
//     $('#exam').DataTable({
//       data: data.data,
//       paging: true,
//       dom: 'frtipB',
//       columns: [
//         {"data": "A", "title": "用户单位名称"},
//         {"data": "B", "title": "台区名称"},
//         {"data": "C", "title": "线路名称<br> (变压器停电表) </br>"},
//         {"data": "D", "title": "线路名称<br>（基准表）</br>"},
//         {"data": "E", "title": "用户名称"},
//         {"data": "F", "title": "停电时时间"},

//       ]
//     });
//   });
// });



$(document).ready(function () {
  $.get('/basicabledt/', function (data) {
    $('#exam').DataTable({
      data: data.data,
      paging: true,
      dom: 'frtipB',
      columns: [
        {"data": "A", "title": "变压器名称"},
        {"data": "B", "title": "线路名称"},
//        {"data": "C", "title": "线路ID"},
//        {"data": "D", "title": "线路名称"},

      ]
    });
  });
});


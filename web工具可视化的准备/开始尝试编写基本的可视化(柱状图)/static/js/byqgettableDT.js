


$(document).ready(function () {
  $.get('/byqabledt/', function (data) {
    $('#exam').DataTable({
      data: data.data,
      paging: true,
      dom: 'frtipB',
      columns: [
        {"data": "A", "title": "用户所在区县单位"},
        {"data": "B", "title": "用户单位名称"},
        {"data": "C", "title": "台区名称"},
        {"data": "D", "title": "线路名称"},
        {"data": "E", "title": "用户名称"},
        {"data": "F", "title": "停电时间"},

      ]
    });
  });
});


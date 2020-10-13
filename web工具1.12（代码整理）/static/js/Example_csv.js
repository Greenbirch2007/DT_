$(function() {
    $("#btn").click(function(){
        $(".table2excel").table2excel({
            exclude: ".noExl",
            name: "Excel Document Name",
            filename: "Datatable",
            exclude_img: true,
            exclude_links: true,
            exclude_inputs: true
        });
    });

});
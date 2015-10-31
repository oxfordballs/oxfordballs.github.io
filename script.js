function renderDate(data, type, full) {
    return moment(data, "DD/MM/YYYY").format("LL");
}

$(document).ready(function() {
    $.fn.dataTable.moment('DD/MM/YY');

    $('#balls').DataTable({
        "paging": false,
        "bInfo": false,
        "bFilter": false,
        "aoColumnDefs": [{
            "aTargets": [1],
            "mData": "date",
            "mRender": renderDate
        }],
        "order": [
            [1, "asc"]
        ]

    });
});

var $select = $('#plane-selector');
var $report_btn = $('#get-report-btn');
var list = [];

$select.chosen({
    width: '100%',
    no_results_text: 'Совпадений не обнаружено',
    search_contains: true,
    placeholder_text_single: 'Выберите или введите параметр для поиска',
    allow_single_deselect: true
});

$(document).ready(function() {
    $.ajax({
        url: '/all',
        type: 'POST',
        success: function (response) {
            list = JSON.parse(response);
            $.each( list['name'], function(i, value) {
                var $item = '<option value="'+ i +'">'+ value +' #'+ list['serial'][i] +'</option>';
                $select.append($item);
            });
            $select.trigger('chosen:updated');
        }
    });
});

$report_btn.on('click', function() {
    var id = $select.val();
    if (id) {
        $.ajax({
            url: '/report',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                'name': list['name'][id],
                'serial': list['serial'][id]
            }),
            success: function () {
            }
        });
    }
});
function save_result(test_id, result_key, result_value) {
    $.post( "/saveresult/save/"+ test_id + "/" + encodeURI(result_key) + "/" + encodeURI(result_value) + "/");
}
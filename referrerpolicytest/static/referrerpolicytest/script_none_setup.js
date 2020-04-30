function referrerpolicytest_none_httptohttp_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/none_httptohttp_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_none_httptohttps_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/none_httptohttps_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_none_httpstohttp_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/none_httpstohttp_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_none_httpstohttps_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/none_httpstohttps_check/" + test_id + "?querystring=exists"
   });
}

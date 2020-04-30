function referrerpolicytest_strictorigin_httptohttp_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/strictorigin_httptohttp_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_strictorigin_httptohttps_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/strictorigin_httptohttps_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_strictorigin_httpstohttp_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/strictorigin_httpstohttp_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_strictorigin_httpstohttps_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/strictorigin_httpstohttps_check/" + test_id + "?querystring=exists"
   });
}

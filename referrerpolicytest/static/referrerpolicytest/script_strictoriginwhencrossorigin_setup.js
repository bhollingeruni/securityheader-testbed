function referrerpolicytest_strictoriginwhencrossorigin_sameorigin_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/strictoriginwhencrossorigin_sameorigin_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_strictoriginwhencrossorigin_crossorigin_httptohttp_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/strictoriginwhencrossorigin_crossorigin_httptohttp_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_strictoriginwhencrossorigin_crossorigin_httptohttps_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/strictoriginwhencrossorigin_crossorigin_httptohttps_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_strictoriginwhencrossorigin_crossorigin_httpstohttp_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/strictoriginwhencrossorigin_crossorigin_httpstohttp_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_strictoriginwhencrossorigin_crossorigin_httpstohttps_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/strictoriginwhencrossorigin_crossorigin_httpstohttps_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_unsafeurl_sameorigin_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/unsafeurl_sameorigin_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_unsafeurl_crossorigin_httptohttp_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/unsafeurl_crossorigin_httptohttp_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_unsafeurl_crossorigin_httptohttps_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/unsafeurl_crossorigin_httptohttps_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_unsafeurl_crossorigin_httpstohttp_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/unsafeurl_crossorigin_httpstohttp_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_unsafeurl_crossorigin_httpstohttps_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/unsafeurl_crossorigin_httpstohttps_check/" + test_id + "?querystring=exists"
   });
}
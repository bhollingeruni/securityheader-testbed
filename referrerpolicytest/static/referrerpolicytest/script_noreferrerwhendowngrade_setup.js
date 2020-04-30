function referrerpolicytest_noreferrerwhendowngrade_httptohttp_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/noreferrerwhendowngrade_httptohttp_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_noreferrerwhendowngrade_httptohttps_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/noreferrerwhendowngrade_httptohttps_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_noreferrerwhendowngrade_httpstohttp_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/noreferrerwhendowngrade_httpstohttp_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_noreferrerwhendowngrade_httpstohttps_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/noreferrerwhendowngrade_httpstohttps_check/" + test_id + "?querystring=exists"
   });
}

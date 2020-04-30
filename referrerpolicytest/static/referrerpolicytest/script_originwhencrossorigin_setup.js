function referrerpolicytest_originwhencrossorigin_sameorigin_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/originwhencrossorigin_sameorigin_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_originwhencrossorigin_crossorigin_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/originwhencrossorigin_crossorigin_check/" + test_id + "?querystring=exists"
   });
}
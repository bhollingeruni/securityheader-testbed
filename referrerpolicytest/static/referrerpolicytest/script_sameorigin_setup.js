function referrerpolicytest_sameorigin_sameorigin_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/sameorigin_sameorigin_check/" + test_id + "?querystring=exists"
   });
}
function referrerpolicytest_sameorigin_crossorigin_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/sameorigin_crossorigin_check/" + test_id + "?querystring=exists"
   });
}
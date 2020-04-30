function referrerpolicytest_origin_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/origin_check/http" + test_id + "?querystring=exists"
   });
}
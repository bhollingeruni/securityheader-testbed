function referrerpolicytest_noreferrer_check(test_id) {
   return $.ajax({
      url: "/referrerpolicytest/noreferrer_check/" + test_id + "?querystring=exists"
   });
}
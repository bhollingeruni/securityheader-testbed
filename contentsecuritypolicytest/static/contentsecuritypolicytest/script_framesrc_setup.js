function contentsecuritypolicytest_framesrc_check(test_id, value) {
   return $.ajax({
      url: "/contentsecuritypolicytest/framesrc_check/" + test_id + "/" + value
   });
}
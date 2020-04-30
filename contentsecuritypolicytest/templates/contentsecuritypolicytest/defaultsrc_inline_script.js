var request = new XMLHttpRequest();
request.addEventListener("load", function(){});
request.open("GET", "/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/scriptsrc_inline_{{ value }}");
request.send();
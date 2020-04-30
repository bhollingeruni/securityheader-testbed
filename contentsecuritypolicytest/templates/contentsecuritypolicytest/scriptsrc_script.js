var request = new XMLHttpRequest();
request.addEventListener("load", function(){});
request.open("GET", "/contentsecuritypolicytest/scriptsrc_check/{{ test_id }}/{{ value }}");
request.send();
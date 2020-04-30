var request = new XMLHttpRequest();
request.addEventListener("load", function(){});
request.open("GET", "/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/url_{{ value }}_script_url");
request.send();
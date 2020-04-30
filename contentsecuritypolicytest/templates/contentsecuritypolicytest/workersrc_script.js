var request = new XMLHttpRequest();
request.addEventListener("load", function(){});
request.open("GET", "/contentsecuritypolicytest/workersrc_check/{{ test_id }}/{{ value }}/");
request.send();
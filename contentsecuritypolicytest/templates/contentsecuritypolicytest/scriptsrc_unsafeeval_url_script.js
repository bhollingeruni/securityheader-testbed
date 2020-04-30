eval("var request = new XMLHttpRequest();" +
    "    request.addEventListener(\"load\", function(){});" +
    "    request.open(\"GET\", \"/contentsecuritypolicytest/scriptsrc_check/{{ test_id }}/{{ value }}_eval_url\");" +
    "    request.send();"
);
Function("var request = new XMLHttpRequest();" +
    "    request.addEventListener(\"load\", function(){});" +
    "    request.open(\"GET\", \"/contentsecuritypolicytest/scriptsrc_check/{{ test_id }}/{{ value }}_function_url\");" +
    "    request.send();"
)();
setTimeout("var request = new XMLHttpRequest();" +
    "    request.addEventListener(\"load\", function(){});" +
    "    request.open(\"GET\", \"/contentsecuritypolicytest/scriptsrc_check/{{ test_id }}/{{ value }}_settimeout_uncallable_url\");" +
    "    request.send();",
    250
);
setTimeout(function() {
        var request = new XMLHttpRequest();
        request.addEventListener("load", function(){});
        request.open("GET", "/contentsecuritypolicytest/scriptsrc_check/{{ test_id }}/{{ value }}_settimeout_callable_url");
        request.send();
    },
    500
);
var interval_id_uncallable_inline = setInterval(
    "clearInterval(interval_id_uncallable_inline);" +
    "    var request = new XMLHttpRequest();" +
    "    request.addEventListener(\"load\", function(){});" +
    "    request.open(\"GET\", \"/contentsecuritypolicytest/scriptsrc_check/{{ test_id }}/{{ value }}_setinterval_uncallable_url\");" +
    "    request.send();",
    750
);
var interval_id_callable_inline = setInterval(function(){
    clearInterval(interval_id_callable_inline);
    var request = new XMLHttpRequest();
    request.addEventListener("load", function(){});
    request.open("GET", "/contentsecuritypolicytest/scriptsrc_check/{{ test_id }}/{{ value }}_setinterval_callable_url");
    request.send();
}, 1000
);
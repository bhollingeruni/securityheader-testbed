eval("var request = new XMLHttpRequest();" +
    "    request.addEventListener(\"load\", function(){});" +
    "    request.open(\"GET\", \"/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/unsafeeval_url_eval_{{ value }}\");" +
    "    request.send();"
);
Function("var request = new XMLHttpRequest();" +
    "    request.addEventListener(\"load\", function(){});" +
    "    request.open(\"GET\", \"/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/unsafeeval_url_function_{{ value }}\");" +
    "    request.send();"
)();
setTimeout("var request = new XMLHttpRequest();" +
    "    request.addEventListener(\"load\", function(){});" +
    "    request.open(\"GET\", \"/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/unsafeeval_url_settimeout_uncallable_{{ value }}\");" +
    "    request.send();",
    250
);
setTimeout(function() {
        var request = new XMLHttpRequest();
        request.addEventListener("load", function(){});
        request.open("GET", "/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/unsafeeval_url_settimeout_callable_{{ value }}");
        request.send();
    },
    500
);
var interval_id_uncallable_inline = setInterval(
    "clearInterval(interval_id_uncallable_inline);" +
    "    var request = new XMLHttpRequest();" +
    "    request.addEventListener(\"load\", function(){});" +
    "    request.open(\"GET\", \"/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/unsafeeval_url_setinterval_uncallable_{{ value }}\");" +
    "    request.send();",
    750
);
var interval_id_callable_inline = setInterval(function(){
    clearInterval(interval_id_callable_inline);
    var request = new XMLHttpRequest();
    request.addEventListener("load", function(){});
    request.open("GET", "/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/unsafeeval_url_setinterval_callable_{{ value }}");
    request.send();
}, 1000
);
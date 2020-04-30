// check if eval() executes
eval('var request = new XMLHttpRequest();\n' +
    '    request.addEventListener("load", function(){});\n' +
    '    request.open("GET", "/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/unsafeeval_eval_{{ value }}/");\n' +
    '    request.send();'
);

// check if Function() executes
Function('var request = new XMLHttpRequest();\n' +
    '    request.addEventListener("load", function(){});\n' +
    '    request.open("GET", "/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/unsafeeval_function_{{ value }}/");\n' +
    '    request.send();'
)();

// check if setTimeout() executes if it has a first argument that is not callable
setTimeout('var request = new XMLHttpRequest();\n' +
    '    request.addEventListener("load", function(){});\n' +
    '    request.open("GET", "/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/unsafeeval_settimeout_uncallable_{{ value }}/");\n' +
    '    request.send();',
    250
);

// check if setTimeout() executes if it has a first argument that is callable
setTimeout(function() {
        var request = new XMLHttpRequest();
        request.addEventListener("load", function(){});
        request.open("GET", "/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/unsafeeval_settimeout_callable_{{ value }}/");
        request.send();
    },
    500
);

// check if setInterval() executes if it has a first argument that is not callable
var interval_id_uncallable = setInterval(
    'clearInterval(interval_id_uncallable);\n' +
    '    var request = new XMLHttpRequest();\n' +
    '    request.addEventListener("load", function(){});\n' +
    '    request.open("GET", "/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/unsafeeval_setinterval_uncallable_{{ value }}/");\n' +
    '    request.send();',
    750
);

// check if setInterval() executes if it has a first argument that is callable
var interval_id_callable = setInterval(function(){
    clearInterval(interval_id_callable);
    var request = new XMLHttpRequest();
    request.addEventListener("load", function(){});
    request.open("GET", "/contentsecuritypolicytest/defaultsrc_check/{{ test_id }}/unsafeeval_setinterval_callable_{{ value }}/");
    request.send();
}, 1000
);
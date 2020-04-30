// check if eval() executes
eval('var request = new XMLHttpRequest();\n' +
    '    request.addEventListener("load", function(){});\n' +
    '    request.open("GET", "/contentsecuritypolicytest/scriptsrc_check/{{ test_id }}/{{ value }}_eval_inline");\n' +
    '    request.send();'
);

// check if Function() executes
Function('var request = new XMLHttpRequest();\n' +
    '    request.addEventListener("load", function(){});\n' +
    '    request.open("GET", "/contentsecuritypolicytest/scriptsrc_check/{{ test_id }}/{{ value }}_function_inline");\n' +
    '    request.send();'
)();

// check if setTimeout() executes if it has a first argument that is not callable
setTimeout('var request = new XMLHttpRequest();\n' +
    '    request.addEventListener("load", function(){});\n' +
    '    request.open("GET", "/contentsecuritypolicytest/scriptsrc_check/{{ test_id }}/{{ value }}_settimeout_uncallable_inline");\n' +
    '    request.send();',
    250
);

// check if setTimeout() executes if it has a first argument that is callable
setTimeout(function() {
        var request = new XMLHttpRequest();
        request.addEventListener("load", function(){});
        request.open("GET", "/contentsecuritypolicytest/scriptsrc_check/{{ test_id }}/{{ value }}_settimeout_callable_inline");
        request.send();
    },
    500
);

// check if setInterval() executes if it has a first argument that is not callable
var interval_id_uncallable_inline = setInterval(
    'clearInterval(interval_id_uncallable_inline);\n' +
    '    var request = new XMLHttpRequest();\n' +
    '    request.addEventListener("load", function(){});\n' +
    '    request.open("GET", "/contentsecuritypolicytest/scriptsrc_check/{{ test_id }}/{{ value }}_setinterval_uncallable_inline");\n' +
    '    request.send();',
    750
);

// check if setInterval() executes if it has a first argument that is callable
var interval_id_callable_inline = setInterval(function(){
    clearInterval(interval_id_callable_inline);
    var request = new XMLHttpRequest();
    request.addEventListener("load", function(){});
    request.open("GET", "/contentsecuritypolicytest/scriptsrc_check/{{ test_id }}/{{ value }}_setinterval_callable_inline");
    request.send();
}, 1000
);
// non-parser-inserted script (allowed by strict-dynamic)
var non_parser_inserted_script = document.createElement('script');
non_parser_inserted_script.src = '/contentsecuritypolicytest/defaultsrc_strictdynamic_inserted_script/{{ test_id }}/{{ value }}_nonparserinserted_inline';
document.head.appendChild(non_parser_inserted_script);

// parser-inserted script (not allowed by strict-dynamic)
document.write('<scr' + 'ipt src="/contentsecuritypolicytest/defaultsrc_strictdynamic_inserted_script/{{ test_id }}/{{ value }}_parserinserted_inline"></scr' + 'ipt>');
var non_parser_inserted_script = document.createElement("script");
non_parser_inserted_script.src = "/contentsecuritypolicytest/defaultsrc_strictdynamic_inserted_script/{{ test_id }}/{{ value }}_nonparserinserted_url";
document.head.appendChild(non_parser_inserted_script);
document.write("<scr" + "ipt src=\"/contentsecuritypolicytest/defaultsrc_strictdynamic_inserted_script/{{ test_id }}/{{ value }}_parserinserted_url\"></scr" + "ipt>");
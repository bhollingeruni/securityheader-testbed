import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

TEST_DEFINITIONS_CSP_DEFAULTSRC_STYLESRC = [
# CSP -----------------------------------------------------------------------------------------------------------------
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_none_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_none_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_none_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_none_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_none_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_none_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_none_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_none_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_none_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_none_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_none_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_none_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },



    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_self_link_element_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_self_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_self_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_self_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_self_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_self_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_self_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_self_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_self_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_self_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_self_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_self_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },



    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_http_link_element_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_http_link_element_external_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_http_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_http_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_http_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_http_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_http_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_http_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_http_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_http_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_http_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_http_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },



    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_https_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_https_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_https_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_https_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_https_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_https_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_https_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_https_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_https_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_https_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_https_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_https_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_link_element_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_valid_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_scheme_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_domain_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_host_invalid_port_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_inline_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_valid_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_nonce_invalid_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_inline_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_valid_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha256_invalid_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_inline_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_valid_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha384_invalid_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_inline_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_valid_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_attribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_js_setattribute_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_sha512_invalid_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_link_element_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_link_header_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_inline_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_import_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_attribute_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_js_setattribute_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeinline_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },


    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_link_element_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_link_element_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_link_header_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_link_header_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_inline_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_import_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_import_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_attribute_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_js_setattribute_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_js_style_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_js_eval_insertrule_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_setup",
        "name": "contentsecuritypolicy_defaultsrc_stylesrc_unsafeeval_js_eval_csstext_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    ]
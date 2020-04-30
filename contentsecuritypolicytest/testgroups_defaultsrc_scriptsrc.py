import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

TEST_DEFINITIONS_CSP_DEFAULTSRC_SCRIPTSRC = [
# CSP -----------------------------------------------------------------------------------------------------------------
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_none_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_none_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_none_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_none_external_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    
    # self -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_self_script_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_self_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_self_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_self_external_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    
    # http -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_http_script_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_http_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_http_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_http_external_script_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },
    
    # https -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_https_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_https_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_https_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_https_external_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    
    # host_valid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_host_valid_script_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_host_valid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_host_valid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_host_valid_external_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },

    # host_invalid_scheme -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_scheme_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_host_invalid_scheme_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_scheme_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },

    # host_invalid_domain -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_domain_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_host_invalid_domain_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_domain_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },

    # host_invalid_port -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_port_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_host_invalid_port_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_host_invalid_port_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },

    # nonce_valid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_valid_script_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_nonce_valid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_valid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_valid_external_script_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },

    # nonce_invalid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_invalid_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_nonce_invalid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_invalid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_nonce_invalid_external_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },

    # sha256_valid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_valid_script_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_sha256_valid_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_valid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_valid_external_script_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },

    # sha256_invalid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_invalid_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_sha256_invalid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_invalid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha256_invalid_external_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },

    # sha384_valid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_valid_script_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_sha384_valid_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_valid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_valid_external_script_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },

    # sha384_invalid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_invalid_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_sha384_invalid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_invalid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha384_invalid_external_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },

    # sha512_valid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_valid_script_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_sha512_valid_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_valid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_valid_external_script_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },

    # sha512_invalid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_invalid_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_sha512_invalid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_invalid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_sha512_invalid_external_script_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },
    
    # unsafeinline -------------------------------------------------------------------------------------------------------------
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_unsafeinline_script_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_unsafeinline_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "check_successful" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_unsafeinline_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "check_successful" }
    },

    # strictdynamic -------------------------------------------------------------------------------------------------------------

    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_host_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_host_parserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_host_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_host_nonparserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_host_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_host_parserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_host_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_host_nonparserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_host_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_host_parserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_host_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_host_nonparserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_scheme_parserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_scheme_nonparserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_scheme_parserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_scheme_nonparserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_scheme_parserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_scheme_nonparserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_self_parserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_self_nonparserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_self_parserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_self_nonparserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_self_parserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_self_nonparserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_unsafeinline_parserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_unsafeinline_nonparserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_unsafeinline_parserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_unsafeinline_nonparserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_unsafeinline_parserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_unsafeinline_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_unsafeinline_nonparserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_hash_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_hash_valid_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_hash_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_strictdynamic_hash_valid_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_hash_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_hash_valid_url_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_hash_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_hash_invalid_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_hash_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_inline_strictdynamic_hash_invalid_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_hash_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_hash_invalid_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
       
        
        
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_strictdynamic_nonce_valid_parserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_strictdynamic_nonce_valid_nonparserinserted_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_strictdynamic_nonce_valid_parserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_strictdynamic_nonce_valid_nonparserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_strictdynamic_nonce_valid_parserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_nonce_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_strictdynamic_nonce_valid_nonparserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
       
        
        
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_strictdynamic_nonce_invalid_parserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_strictdynamic_nonce_invalid_nonparserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_strictdynamic_nonce_invalid_parserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_strictdynamic_nonce_invalid_nonparserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_strictdynamic_nonce_invalid_parserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_nonce_invalid_setup",
        "name": "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_strictdynamic_nonce_invalid_nonparserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    }
]
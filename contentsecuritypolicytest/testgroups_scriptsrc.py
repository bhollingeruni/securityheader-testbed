import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

TEST_DEFINITIONS_CSP_SCRIPTSRC = [
# CSP -----------------------------------------------------------------------------------------------------------------
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_none_setup",
        "name": "contentsecuritypolicy_scriptsrc_none_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_none_setup",
        "name": "contentsecuritypolicy_scriptsrc_none_inline_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_none_setup",
        "name": "contentsecuritypolicy_scriptsrc_none_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_none_setup",
        "name": "contentsecuritypolicy_scriptsrc_none_external_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    
    # self -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_self_setup",
        "name": "contentsecuritypolicy_scriptsrc_self_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_self_setup",
        "name": "contentsecuritypolicy_scriptsrc_self_inline_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_self_setup",
        "name": "contentsecuritypolicy_scriptsrc_self_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_self_setup",
        "name": "contentsecuritypolicy_scriptsrc_self_external_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    
    # http -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_http_setup",
        "name": "contentsecuritypolicy_scriptsrc_http_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_http_setup",
        "name": "contentsecuritypolicy_scriptsrc_http_inline_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_http_setup",
        "name": "contentsecuritypolicy_scriptsrc_http_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_http_setup",
        "name": "contentsecuritypolicy_scriptsrc_http_external_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },
    
    # https -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_https_setup",
        "name": "contentsecuritypolicy_scriptsrc_https_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_https_setup",
        "name": "contentsecuritypolicy_scriptsrc_https_inline_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_https_setup",
        "name": "contentsecuritypolicy_scriptsrc_https_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_https_setup",
        "name": "contentsecuritypolicy_scriptsrc_https_external_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    
    # host_valid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_host_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_host_valid_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_host_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_host_valid_inline_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_host_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_host_valid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_host_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_host_valid_external_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },

    # host_invalid_scheme -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_scriptsrc_host_invalid_scheme_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_scriptsrc_host_invalid_scheme_inline_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_scriptsrc_host_invalid_scheme_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },

    # host_invalid_domain -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_scriptsrc_host_invalid_domain_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_scriptsrc_host_invalid_domain_inline_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_scriptsrc_host_invalid_domain_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },

    # host_invalid_port -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_scriptsrc_host_invalid_port_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_scriptsrc_host_invalid_port_inline_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_scriptsrc_host_invalid_port_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },

    # nonce_valid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_nonce_valid_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_nonce_valid_inline_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_nonce_valid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_nonce_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_nonce_valid_external_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },

    # nonce_invalid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_nonce_invalid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_nonce_invalid_inline_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_nonce_invalid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_nonce_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_nonce_invalid_external_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },

    # sha256_valid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha256_valid_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha256_valid_inline_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha256_valid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha256_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha256_valid_external_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },

    # sha256_invalid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha256_invalid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha256_invalid_inline_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha256_invalid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha256_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha256_invalid_external_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },

    # sha384_valid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha384_valid_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha384_valid_inline_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha384_valid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha384_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha384_valid_external_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },

    # sha384_invalid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha384_invalid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha384_invalid_inline_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha384_invalid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha384_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha384_invalid_external_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },

    # sha512_valid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha512_valid_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha512_valid_inline_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha512_valid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha512_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha512_valid_external_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },

    # sha512_invalid -------------------------------------------------------------------------------------------------------------
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha512_invalid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha512_invalid_inline_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha512_invalid_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_sha512_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_sha512_invalid_external_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },
    
    # unsafeinline -------------------------------------------------------------------------------------------------------------
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_scriptsrc_unsafeinline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_scriptsrc_unsafeinline_inline_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed" },
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_unsafeinline_setup",
        "name": "contentsecuritypolicy_scriptsrc_unsafeinline_url_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    },

    # strictdynamic -------------------------------------------------------------------------------------------------------------

    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_host_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_host_parserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_host_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_host_nonparserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_host_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_host_parserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_host_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_host_nonparserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_host_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_host_parserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_host_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_host_nonparserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_scheme_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_scheme_parserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_scheme_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_scheme_nonparserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_scheme_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_scheme_parserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_scheme_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_scheme_nonparserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_scheme_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_scheme_parserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_scheme_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_scheme_nonparserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_self_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_self_parserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_self_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_self_nonparserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_self_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_self_parserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_self_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_self_nonparserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_self_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_self_parserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_self_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_self_nonparserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_unsafeinline_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_unsafeinline_parserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_unsafeinline_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_unsafeinline_nonparserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_unsafeinline_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_unsafeinline_parserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_unsafeinline_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_unsafeinline_nonparserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_unsafeinline_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_unsafeinline_parserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_unsafeinline_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_unsafeinline_nonparserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_hash_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_hash_valid_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_hash_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_hash_valid_inline_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "script_executed"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_hash_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_hash_valid_url_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "script_executed"},
        "fail": {}
    },
       
        
        
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_valid_parserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_valid_nonparserinserted_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "script_executed"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_valid_parserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_valid_nonparserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_valid_parserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_valid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_valid_nonparserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
       
        
        
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_invalid_parserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_invalid_nonparserinserted_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_invalid_parserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_invalid_nonparserinserted_inline_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_invalid_parserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_scriptsrc",
        "setup": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_invalid_setup",
        "name": "contentsecuritypolicy_scriptsrc_strictdynamic_nonce_invalid_nonparserinserted_url_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "script_executed"}
    }
]
import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

TEST_DEFINITIONS_CSP_DEFAULTSRC_FRAMESRC = [
# CSP -----------------------------------------------------------------------------------------------------------------
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_none_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_none_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_none_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_self_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_self_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_self_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_http_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_http_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_http_external_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_https_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_https_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_https_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_host_valid_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_host_valid_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_host_valid_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_host_invalid_scheme_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_host_invalid_scheme_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_host_invalid_domain_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_host_invalid_domain_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_host_invalid_port_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_defaultsrc",
        "setup": "contentsecuritypolicy_defaultsrc_framesrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_defaultsrc_framesrc_host_invalid_port_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    ]
import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

TEST_DEFINITIONS_CSP_FRAMEANCESTORS = [
# CSP -----------------------------------------------------------------------------------------------------------------
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_frameancestors",
        "setup": "contentsecuritypolicy_frameancestors_self_setup",
        "name": "contentsecuritypolicy_frameancestors_self_outer_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_frameancestors",
        "setup": "contentsecuritypolicy_frameancestors_self_setup",
        "name": "contentsecuritypolicy_frameancestors_self_inner_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_frameancestors",
        "setup": "contentsecuritypolicy_frameancestors_host_valid_setup",
        "name": "contentsecuritypolicy_frameancestors_host_valid_outer_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_frameancestors",
        "setup": "contentsecuritypolicy_frameancestors_host_valid_setup",
        "name": "contentsecuritypolicy_frameancestors_host_valid_inner_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_frameancestors",
        "setup": "contentsecuritypolicy_frameancestors_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_frameancestors_host_invalid_scheme_outer_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_frameancestors",
        "setup": "contentsecuritypolicy_frameancestors_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_frameancestors_host_invalid_scheme_inner_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_frameancestors",
        "setup": "contentsecuritypolicy_frameancestors_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_frameancestors_host_invalid_domain_outer_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_frameancestors",
        "setup": "contentsecuritypolicy_frameancestors_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_frameancestors_host_invalid_domain_inner_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_frameancestors",
        "setup": "contentsecuritypolicy_frameancestors_host_invalid_port_setup",
        "name": "contentsecuritypolicy_frameancestors_host_invalid_port_outer_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_frameancestors",
        "setup": "contentsecuritypolicy_frameancestors_host_invalid_port_setup",
        "name": "contentsecuritypolicy_frameancestors_host_invalid_port_inner_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "frame_loaded"}
    },
    ]
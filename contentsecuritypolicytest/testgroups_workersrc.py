import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

TEST_DEFINITIONS_CSP_WORKERSRC = [
# CSP -----------------------------------------------------------------------------------------------------------------
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_none_setup",
        "name": "contentsecuritypolicy_workersrc_none_worker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_none_setup",
        "name": "contentsecuritypolicy_workersrc_none_sharedworker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_none_setup",
        "name": "contentsecuritypolicy_workersrc_none_registeredworker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_self_setup",
        "name": "contentsecuritypolicy_workersrc_self_worker_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_self_setup",
        "name": "contentsecuritypolicy_workersrc_self_sharedworker_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_self_setup",
        "name": "contentsecuritypolicy_workersrc_self_registeredworker_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"},
        "fail": {}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_http_setup",
        "name": "contentsecuritypolicy_workersrc_http_worker_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_http_setup",
        "name": "contentsecuritypolicy_workersrc_http_sharedworker_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_http_setup",
        "name": "contentsecuritypolicy_workersrc_http_registeredworker_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"},
        "fail": {}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_https_setup",
        "name": "contentsecuritypolicy_workersrc_https_worker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_https_setup",
        "name": "contentsecuritypolicy_workersrc_https_sharedworker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_https_setup",
        "name": "contentsecuritypolicy_workersrc_https_registeredworker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_host_valid_setup",
        "name": "contentsecuritypolicy_workersrc_host_valid_worker_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_host_valid_setup",
        "name": "contentsecuritypolicy_workersrc_host_valid_sharedworker_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_host_valid_setup",
        "name": "contentsecuritypolicy_workersrc_host_valid_registeredworker_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"},
        "fail": {}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_workersrc_host_invalid_scheme_worker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_workersrc_host_invalid_scheme_sharedworker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_workersrc_host_invalid_scheme_registeredworker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_workersrc_host_invalid_domain_worker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_workersrc_host_invalid_domain_sharedworker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_workersrc_host_invalid_domain_registeredworker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_workersrc_host_invalid_port_worker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_workersrc_host_invalid_port_sharedworker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_workersrc",
        "setup": "contentsecuritypolicy_workersrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_workersrc_host_invalid_port_registeredworker_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "worker_request_received"}
    }
    ]
import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

TEST_DEFINITIONS_CSP_CONNECTSRC = [
# CSP -----------------------------------------------------------------------------------------------------------------
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_none_setup",
        "name": "contentsecuritypolicy_connectsrc_none_ping_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_none_setup",
        "name": "contentsecuritypolicy_connectsrc_none_xhr_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_none_setup",
        "name": "contentsecuritypolicy_connectsrc_none_websocket_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_none_setup",
        "name": "contentsecuritypolicy_connectsrc_none_eventsource_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_none_setup",
        "name": "contentsecuritypolicy_connectsrc_none_beacon_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_none_setup",
        "name": "contentsecuritypolicy_connectsrc_none_ping_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_none_setup",
        "name": "contentsecuritypolicy_connectsrc_none_xhr_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_none_setup",
        "name": "contentsecuritypolicy_connectsrc_none_websocket_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_none_setup",
        "name": "contentsecuritypolicy_connectsrc_none_eventsource_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_none_setup",
        "name": "contentsecuritypolicy_connectsrc_none_beacon_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_self_setup",
        "name": "contentsecuritypolicy_connectsrc_self_ping_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_self_setup",
        "name": "contentsecuritypolicy_connectsrc_self_xhr_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_self_setup",
        "name": "contentsecuritypolicy_connectsrc_self_websocket_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_self_setup",
        "name": "contentsecuritypolicy_connectsrc_self_eventsource_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_self_setup",
        "name": "contentsecuritypolicy_connectsrc_self_beacon_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_self_setup",
        "name": "contentsecuritypolicy_connectsrc_self_ping_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_self_setup",
        "name": "contentsecuritypolicy_connectsrc_self_xhr_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_self_setup",
        "name": "contentsecuritypolicy_connectsrc_self_websocket_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_self_setup",
        "name": "contentsecuritypolicy_connectsrc_self_eventsource_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_self_setup",
        "name": "contentsecuritypolicy_connectsrc_self_beacon_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_http_setup",
        "name": "contentsecuritypolicy_connectsrc_http_ping_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_http_setup",
        "name": "contentsecuritypolicy_connectsrc_http_xhr_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_http_setup",
        "name": "contentsecuritypolicy_connectsrc_http_websocket_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_http_setup",
        "name": "contentsecuritypolicy_connectsrc_http_eventsource_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_http_setup",
        "name": "contentsecuritypolicy_connectsrc_http_beacon_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_http_setup",
        "name": "contentsecuritypolicy_connectsrc_http_ping_external_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_http_setup",
        "name": "contentsecuritypolicy_connectsrc_http_xhr_external_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_http_setup",
        "name": "contentsecuritypolicy_connectsrc_http_websocket_external_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_http_setup",
        "name": "contentsecuritypolicy_connectsrc_http_eventsource_external_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_http_setup",
        "name": "contentsecuritypolicy_connectsrc_http_beacon_external_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_ws_setup",
        "name": "contentsecuritypolicy_connectsrc_ws_ping_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_ws_setup",
        "name": "contentsecuritypolicy_connectsrc_ws_xhr_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_ws_setup",
        "name": "contentsecuritypolicy_connectsrc_ws_websocket_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_ws_setup",
        "name": "contentsecuritypolicy_connectsrc_ws_eventsource_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_ws_setup",
        "name": "contentsecuritypolicy_connectsrc_ws_beacon_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_ws_setup",
        "name": "contentsecuritypolicy_connectsrc_ws_ping_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_ws_setup",
        "name": "contentsecuritypolicy_connectsrc_ws_xhr_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_ws_setup",
        "name": "contentsecuritypolicy_connectsrc_ws_websocket_external_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_ws_setup",
        "name": "contentsecuritypolicy_connectsrc_ws_eventsource_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_ws_setup",
        "name": "contentsecuritypolicy_connectsrc_ws_beacon_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_https_setup",
        "name": "contentsecuritypolicy_connectsrc_https_ping_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_https_setup",
        "name": "contentsecuritypolicy_connectsrc_https_xhr_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_https_setup",
        "name": "contentsecuritypolicy_connectsrc_https_websocket_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_https_setup",
        "name": "contentsecuritypolicy_connectsrc_https_eventsource_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_https_setup",
        "name": "contentsecuritypolicy_connectsrc_https_beacon_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_https_setup",
        "name": "contentsecuritypolicy_connectsrc_https_ping_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_https_setup",
        "name": "contentsecuritypolicy_connectsrc_https_xhr_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_https_setup",
        "name": "contentsecuritypolicy_connectsrc_https_websocket_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_https_setup",
        "name": "contentsecuritypolicy_connectsrc_https_eventsource_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_https_setup",
        "name": "contentsecuritypolicy_connectsrc_https_beacon_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_wss_setup",
        "name": "contentsecuritypolicy_connectsrc_wss_ping_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_wss_setup",
        "name": "contentsecuritypolicy_connectsrc_wss_xhr_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_wss_setup",
        "name": "contentsecuritypolicy_connectsrc_wss_websocket_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_wss_setup",
        "name": "contentsecuritypolicy_connectsrc_wss_eventsource_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_wss_setup",
        "name": "contentsecuritypolicy_connectsrc_wss_beacon_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_wss_setup",
        "name": "contentsecuritypolicy_connectsrc_wss_ping_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_wss_setup",
        "name": "contentsecuritypolicy_connectsrc_wss_xhr_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_wss_setup",
        "name": "contentsecuritypolicy_connectsrc_wss_websocket_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_wss_setup",
        "name": "contentsecuritypolicy_connectsrc_wss_eventsource_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_wss_setup",
        "name": "contentsecuritypolicy_connectsrc_wss_beacon_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_valid_setup",
        "name": "contentsecuritypolicy_connectsrc_host_valid_ping_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_valid_setup",
        "name": "contentsecuritypolicy_connectsrc_host_valid_xhr_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_valid_setup",
        "name": "contentsecuritypolicy_connectsrc_host_valid_websocket_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_valid_setup",
        "name": "contentsecuritypolicy_connectsrc_host_valid_eventsource_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_valid_setup",
        "name": "contentsecuritypolicy_connectsrc_host_valid_beacon_current_check",
        "success": {"operator": OPERATOR_EQUALS, "value": "check_successful"},
        "fail": {}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_valid_setup",
        "name": "contentsecuritypolicy_connectsrc_host_valid_ping_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_valid_setup",
        "name": "contentsecuritypolicy_connectsrc_host_valid_xhr_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_valid_setup",
        "name": "contentsecuritypolicy_connectsrc_host_valid_websocket_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_valid_setup",
        "name": "contentsecuritypolicy_connectsrc_host_valid_eventsource_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_valid_setup",
        "name": "contentsecuritypolicy_connectsrc_host_valid_beacon_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_scheme_ping_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_scheme_xhr_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_scheme_websocket_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_scheme_eventsource_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_scheme_beacon_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_scheme_ping_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_scheme_xhr_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_scheme_websocket_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_scheme_eventsource_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_scheme_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_scheme_beacon_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_domain_ping_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_domain_xhr_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_domain_websocket_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_domain_eventsource_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_domain_beacon_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_domain_ping_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_domain_xhr_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_domain_websocket_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_domain_eventsource_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_domain_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_domain_beacon_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    
    
    
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_port_ping_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_port_xhr_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_port_websocket_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_port_eventsource_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_port_beacon_current_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_port_ping_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_port_xhr_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_port_websocket_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_port_eventsource_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    {
        "group": "contentsecuritypolicy",
        "subgroup": "contentsecuritypolicy_connectsrc",
        "setup": "contentsecuritypolicy_connectsrc_host_invalid_port_setup",
        "name": "contentsecuritypolicy_connectsrc_host_invalid_port_beacon_external_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "check_successful"}
    },
    ]
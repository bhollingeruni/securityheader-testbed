import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

# maps test groups to their subgroups. Used in structuring the result set
TEST_GROUPS_CORS = {"cors": [
    "cors_simple",
    "cors_complex"
]}

TEST_DEFINITIONS_CORS = [
# SIMPLE SAMEORIGIN -----------------------------------------------------------------------------------------------------------------
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_default_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_origin_null_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_origin_all_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_origin_valid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_origin_scheme_invalid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_origin_domain_invalid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_origin_port_invalid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_exposeheader_valid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "header_accessed"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_exposeheader_invalid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "header_accessed"},
        "fail": {}
    },

# SIMPLE CROSSORIGIN -----------------------------------------------------------------------------------------------------------------
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_default_external_resource",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "resource_received" }
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_origin_null_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_not_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_origin_all_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_origin_valid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_origin_scheme_invalid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_not_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_origin_domain_invalid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_not_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_origin_port_invalid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_not_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_exposeheader_valid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "header_accessed"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_simple",
        "setup": "cors_simple_setup",
        "name": "cors_simple_exposeheader_invalid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "header_not_accessed"},
        "fail": {}
    },

# COMPLEX SAMEORIGIN -----------------------------------------------------------------------------------------------------------------
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_default_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_origin_null_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_origin_all_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_origin_valid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_origin_scheme_invalid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_origin_domain_invalid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_origin_port_invalid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_exposeheader_valid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "header_accessed"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_exposeheader_invalid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "header_accessed"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_credentials_all_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_credentials_all_complex_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "auth_header_correct_value"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_credentials_origin_valid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_credentials_origin_valid_complex_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "auth_header_correct_value"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_credentials_origin_invalid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_credentials_origin_invalid_complex_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "auth_header_correct_value"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_allowheaders_valid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_allowheaders_valid_complex_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "requesttestheader_header_correct_value"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_allowheaders_invalid_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_allowheaders_invalid_complex_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "requesttestheader_header_correct_value"},
        "fail": {}
    },

# COMPLEX CROSSORIGIN -----------------------------------------------------------------------------------------------------------------
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_default_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_not_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_origin_null_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_not_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_origin_all_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_origin_valid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_origin_scheme_invalid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_not_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_origin_domain_invalid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_not_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_origin_port_invalid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_not_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_exposeheader_valid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "header_accessed"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_exposeheader_invalid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "header_not_accessed"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_credentials_all_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_credentials_all_external_complex_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "auth_header_correct_value"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_credentials_origin_valid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_credentials_origin_valid_external_complex_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "auth_header_correct_value"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_credentials_origin_invalid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_not_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_credentials_origin_invalid_external_complex_preflight",
        "success": { "operator": OPERATOR_EQUALS, "value": "auth_header_not_set"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_allowheaders_valid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_allowheaders_valid_external_complex_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "requesttestheader_header_correct_value"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_complex_allowheaders_invalid_external_resource",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_not_received"},
        "fail": {}
    },
    {
        "group": "cors",
        "subgroup": "cors_complex",
        "setup": "cors_complex_setup",
        "name": "cors_allowheaders_invalid_external_complex_preflight",
        "success": { "operator": OPERATOR_EQUALS, "value": "requesttestheader_header_not_set"},
        "fail": {}
    }



]
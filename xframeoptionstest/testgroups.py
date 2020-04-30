import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

# maps test groups to their subgroups. Used in structuring the result set
TEST_GROUPS_XFRAMEOPTIONS = {"xframeoptions": ["xframeoptions_none", "xframeoptions_deny", "xframeoptions_sameorigin_valid", "xframeoptions_sameorigin_invalid", "xframeoptions_allowfrom_valid", "xframeoptions_allowfrom_invalid"]}

TEST_DEFINITIONS_XFRAMEOPTIONS = [
# XFRAMEOPTIONS --------------------------------------------------------------------------------------------------------
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_none",
        "setup": "xframeoptions_none",
        "name": "xframeoptions_none_iframe_client_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "content_loaded"},
        "fail": {}
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_none",
        "setup": "xframeoptions_none",
        "name": "xframeoptions_none_embed_client_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_loaded"},
        "fail": {}
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_none",
        "setup": "xframeoptions_none",
        "name": "xframeoptions_none_object_client_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "content_loaded"},
        "fail": {}
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_deny",
        "setup": "xframeoptions_deny",
        "name": "xframeoptions_deny_iframe_client_check",
        "success": {},
        "fail": {"operator": OPERATOR_EQUALS, "value": "content_loaded" }
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_deny",
        "setup": "xframeoptions_deny",
        "name": "xframeoptions_deny_embed_client_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "resource_loaded" }
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_deny",
        "setup": "xframeoptions_deny",
        "name": "xframeoptions_deny_object_client_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "content_loaded" }
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_sameorigin_valid",
        "setup": "xframeoptions_sameorigin",
        "name": "xframeoptions_sameorigin_valid_iframe_client_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "content_loaded"},
        "fail": {}
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_sameorigin_valid",
        "setup": "xframeoptions_sameorigin",
        "name": "xframeoptions_sameorigin_valid_embed_client_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_loaded"},
        "fail": {}
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_sameorigin_valid",
        "setup": "xframeoptions_sameorigin",
        "name": "xframeoptions_sameorigin_valid_object_client_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "content_loaded"},
        "fail": {}
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_sameorigin_invalid",
        "setup": "xframeoptions_sameorigin",
        "name": "xframeoptions_sameorigin_invalid_iframe_client_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "resource_loaded" }
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_sameorigin_invalid",
        "setup": "xframeoptions_sameorigin",
        "name": "xframeoptions_sameorigin_invalid_embed_client_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "resource_loaded" }
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_sameorigin_invalid",
        "setup": "xframeoptions_sameorigin",
        "name": "xframeoptions_sameorigin_invalid_object_client_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "resource_loaded" }
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_allowfrom_valid",
        "setup": "xframeoptions_allowfrom_valid",
        "name": "xframeoptions_allowfrom_valid_iframe_client_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_loaded" },
        "fail": {}
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_allowfrom_valid",
        "setup": "xframeoptions_allowfrom_valid",
        "name": "xframeoptions_allowfrom_valid_embed_client_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_loaded"},
        "fail": {}
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_allowfrom_valid",
        "setup": "xframeoptions_allowfrom_valid",
        "name": "xframeoptions_allowfrom_valid_object_client_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "resource_loaded"},
        "fail": {}
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_allowfrom_invalid",
        "setup": "xframeoptions_allowfrom_invalid",
        "name": "xframeoptions_allowfrom_invalid_iframe_client_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "resource_loaded" }
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_allowfrom_invalid",
        "setup": "xframeoptions_allowfrom_invalid",
        "name": "xframeoptions_allowfrom_invalid_embed_client_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "resource_loaded" }
    },
    {
        "group": "xframeoptions",
        "subgroup": "xframeoptions_allowfrom_invalid",
        "setup": "xframeoptions_allowfrom_invalid",
        "name": "xframeoptions_allowfrom_invalid_object_client_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "resource_loaded" }
    },
]
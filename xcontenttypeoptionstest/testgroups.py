import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

# maps test groups to their subgroups. Used in structuring the result set
TEST_GROUPS_XCONTENTTYPEOPTIONS = {"xcontenttypeoptions": ["xcontenttypeoptions_none", "xcontenttypeoptions_nosniff"]}

TEST_DEFINITIONS_XCONTENTTYPEOPTIONS = [
# XCONTENTTYPEOPTIONS --------------------------------------------------------------------------------------------------
    {
        "group": "xcontenttypeoptions",
        "subgroup": "xcontenttypeoptions_none",
        "setup": "xcontenttypeoptions_none",
        "name": "xcontenttypeoptions_none_client_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "script_executed"},
        "fail": {}
    },
    {
        "group": "xcontenttypeoptions",
        "subgroup": "xcontenttypeoptions_nosniff",
        "setup": "xcontenttypeoptions_nosniff",
        "name": "xcontenttypeoptions_nosniff_client_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "script_executed" }
    }
]
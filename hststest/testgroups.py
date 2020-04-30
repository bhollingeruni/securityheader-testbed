import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

# maps test groups to their subgroups. Used in structuring the result set
TEST_GROUPS_HSTS = {"hsts": ["hsts_scheme", "hsts_subdomain"]}

TEST_DEFINITIONS_HSTS = [
# HSTS -----------------------------------------------------------------------------------------------------------------
    {
        "group": "hsts",
        "subgroup": "hsts_scheme",
        "setup": "hsts_setup",
        "name": "hsts_scheme_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "request_sent_over_https"},
        "fail": {}
    },
    {
        "group": "hsts",
        "subgroup": "hsts_subdomain",
        "setup": "hsts_setup",
        "name": "hsts_scheme_subdomain_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "request_sent_over_https"},
        "fail": {}
    }
]
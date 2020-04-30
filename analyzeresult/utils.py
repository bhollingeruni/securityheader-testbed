import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT
from hststest.testgroups import TEST_GROUPS_HSTS
from hststest.testgroups import TEST_DEFINITIONS_HSTS

from referrerpolicytest.testgroups import TEST_GROUPS_REFERRERPOLICY
from referrerpolicytest.testgroups import TEST_DEFINITIONS_REFERRERPOLICY
from xframeoptionstest.testgroups import TEST_GROUPS_XFRAMEOPTIONS
from xframeoptionstest.testgroups import TEST_DEFINITIONS_XFRAMEOPTIONS
from xcontenttypeoptionstest.testgroups import TEST_GROUPS_XCONTENTTYPEOPTIONS
from xcontenttypeoptionstest.testgroups import TEST_DEFINITIONS_XCONTENTTYPEOPTIONS
from corstest.testgroups import TEST_GROUPS_CORS
from corstest.testgroups import TEST_DEFINITIONS_CORS
from contentsecuritypolicytest.testgroups import TEST_GROUPS_CSP
from contentsecuritypolicytest.testgroups import TEST_DEFINITIONS_CSP
from cookietest.testgroups import TEST_GROUPS_COOKIE
from cookietest.testgroups import TEST_DEFINITIONS_COOKIE

# maps test groups to their subgroups. Used in structuring the result set
def get_all_testgroups():
    all_testgroups = {
        **TEST_GROUPS_CSP,
        **TEST_GROUPS_COOKIE,
        **TEST_GROUPS_CORS,
        **TEST_GROUPS_HSTS,
        **TEST_GROUPS_REFERRERPOLICY,
        **TEST_GROUPS_XCONTENTTYPEOPTIONS,
        **TEST_GROUPS_XFRAMEOPTIONS,
    }
    return all_testgroups

def get_all_testdefinitions():
    all_testdefinitions = TEST_DEFINITIONS_HSTS + TEST_DEFINITIONS_REFERRERPOLICY + TEST_DEFINITIONS_XFRAMEOPTIONS + TEST_DEFINITIONS_XCONTENTTYPEOPTIONS + TEST_DEFINITIONS_CORS + TEST_DEFINITIONS_CSP + TEST_DEFINITIONS_COOKIE

    return all_testdefinitions
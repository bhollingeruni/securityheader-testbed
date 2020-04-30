import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT
from contentsecuritypolicytest.testgroups_scriptsrc import TEST_DEFINITIONS_CSP_SCRIPTSRC
from contentsecuritypolicytest.testgroups_frameancestors import TEST_DEFINITIONS_CSP_FRAMEANCESTORS
from contentsecuritypolicytest.testgroups_framesrc import TEST_DEFINITIONS_CSP_FRAMESRC
from contentsecuritypolicytest.testgroups_imgsrc import TEST_DEFINITIONS_CSP_IMGSRC
from contentsecuritypolicytest.testgroups_connectsrc import TEST_DEFINITIONS_CSP_CONNECTSRC
from contentsecuritypolicytest.testgroups_stylesrc import TEST_DEFINITIONS_CSP_STYLESRC
from contentsecuritypolicytest.testgroups_workersrc import TEST_DEFINITIONS_CSP_WORKERSRC
from contentsecuritypolicytest.testgroups_defaultsrc import TEST_DEFINITIONS_CSP_DEFAULTSRC

# maps test groups to their subgroups. Used in structuring the result set
TEST_GROUPS_CSP = {"contentsecuritypolicy": [
    "contentsecuritypolicy_scriptsrc",
    "contentsecuritypolicy_frameancestors",
    "contentsecuritypolicy_framesrc",
    "contentsecuritypolicy_imgsrc",
    "contentsecuritypolicy_connectsrc",
    "contentsecuritypolicy_stylesrc",
    "contentsecuritypolicy_workersrc",
    "contentsecuritypolicy_defaultsrc",
    ]}

TEST_DEFINITIONS_CSP = [] + TEST_DEFINITIONS_CSP_SCRIPTSRC + TEST_DEFINITIONS_CSP_FRAMEANCESTORS + TEST_DEFINITIONS_CSP_FRAMESRC + TEST_DEFINITIONS_CSP_IMGSRC + TEST_DEFINITIONS_CSP_CONNECTSRC + TEST_DEFINITIONS_CSP_STYLESRC + TEST_DEFINITIONS_CSP_WORKERSRC + TEST_DEFINITIONS_CSP_DEFAULTSRC
import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

# maps test groups to their subgroups. Used in structuring the result set
TEST_GROUPS_REFERRERPOLICY = {"referrerpolicy": [
                                  "referrerpolicy_none",
                                  "referrerpolicy_noreferrer",
                                  "referrerpolicy_noreferrerwhendowngrade",
                                  "referrerpolicy_sameorigin",
                                  "referrerpolicy_origin",
                                  "referrerpolicy_strictorigin",
                                  "referrerpolicy_originwhencrossorigin",
                                  "referrerpolicy_strictoriginwhencrossorigin",
                                  "referrerpolicy_unsafeurl"
                                  ]}

TEST_DEFINITIONS_REFERRERPOLICY = [
# REFERRERPOLICY -------------------------------------------------------------------------------------------------------
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_none",
        "setup": "referrerpolicy_none_httptohttp_setup",
        "name": "referrerpolicy_none_httptohttp_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_sent"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_none",
        "setup": "referrerpolicy_none_httptohttps_setup",
        "name": "referrerpolicy_none_httptohttps_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_sent"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_none",
        "setup": "referrerpolicy_none_httpstohttp_setup",
        "name": "referrerpolicy_none_httpstohttp_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "no_referrer_sent"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_none",
        "setup": "referrerpolicy_none_httpstohttps_setup",
        "name": "referrerpolicy_none_httpstohttps_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_sent"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_noreferrer",
        "setup": "referrerpolicy_noreferrer_setup",
        "name": "referrerpolicy_noreferrer_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "no_referrer_sent"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_noreferrerwhendowngrade",
        "setup": "referrerpolicy_noreferrerwhendowngrade_httptohttp_setup",
        "name": "referrerpolicy_noreferrerwhendowngrade_httptohttp_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_sent"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_noreferrerwhendowngrade",
        "setup": "referrerpolicy_noreferrerwhendowngrade_httptohttps_setup",
        "name": "referrerpolicy_noreferrerwhendowngrade_httptohttps_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_sent"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_noreferrerwhendowngrade",
        "setup": "referrerpolicy_noreferrerwhendowngrade_httpstohttp_setup",
        "name": "referrerpolicy_noreferrerwhendowngrade_httpstohttp_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "no_referrer_sent"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_noreferrerwhendowngrade",
        "setup": "referrerpolicy_noreferrerwhendowngrade_httpstohttps_setup",
        "name": "referrerpolicy_noreferrerwhendowngrade_httpstohttps_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_sent"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_sameorigin",
        "setup": "referrerpolicy_sameorigin_sameorigin_setup",
        "name": "referrerpolicy_sameorigin_sameorigin_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_sent"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_sameorigin",
        "setup": "referrerpolicy_sameorigin_crossorigin_setup",
        "name": "referrerpolicy_sameorigin_crossorigin_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "no_referrer_sent"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_origin",
        "setup": "referrerpolicy_origin_setup",
        "name": "referrerpolicy_origin_http_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_origin",
        "setup": "referrerpolicy_origin_setup",
        "name": "referrerpolicy_origin_https_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_strictorigin",
        "setup": "referrerpolicy_strictorigin_httptohttp_setup",
        "name": "referrerpolicy_strictorigin_httptohttp_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_strictorigin",
        "setup": "referrerpolicy_strictorigin_httptohttps_setup",
        "name": "referrerpolicy_strictorigin_httptohttps_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_strictorigin",
        "setup": "referrerpolicy_strictorigin_httpstohttp_setup",
        "name": "referrerpolicy_strictorigin_httpstohttp_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "no_referrer_sent"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_strictorigin",
        "setup": "referrerpolicy_strictorigin_httpstohttps_setup",
        "name": "referrerpolicy_strictorigin_httpstohttps_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_originwhencrossorigin",
        "setup": "referrerpolicy_originwhencrossorigin_sameorigin_setup",
        "name": "referrerpolicy_originwhencrossorigin_sameorigin_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_originwhencrossorigin",
        "setup": "referrerpolicy_originwhencrossorigin_crossorigin_setup",
        "name": "referrerpolicy_originwhencrossorigin_crossorigin_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_strictoriginwhencrossorigin",
        "setup": "referrerpolicy_strictoriginwhencrossorigin_sameorigin_setup",
        "name": "referrerpolicy_strictoriginwhencrossorigin_sameorigin_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_strictoriginwhencrossorigin",
        "setup": "referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttp_setup",
        "name": "referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttp_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_strictoriginwhencrossorigin",
        "setup": "referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttps_setup",
        "name": "referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttps_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_strictoriginwhencrossorigin",
        "setup": "referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttp_setup",
        "name": "referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttp_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "no_referrer_sent"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_strictoriginwhencrossorigin",
        "setup": "referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttps_setup",
        "name": "referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttps_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_unsafeurl",
        "setup": "referrerpolicy_unsafeurl_sameorigin_setup",
        "name": "referrerpolicy_unsafeurl_sameorigin_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_unsafeurl",
        "setup": "referrerpolicy_unsafeurl_crossorigin_httptohttp_setup",
        "name": "referrerpolicy_unsafeurl_corssorigin_httptohttp_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_unsafeurl",
        "setup": "referrerpolicy_unsafeurl_crossorigin_httptohttps_setup",
        "name": "referrerpolicy_unsafeurl_corssorigin_httptohttps_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_unsafeurl",
        "setup": "referrerpolicy_unsafeurl_crossorigin_httpstohttp_setup",
        "name": "referrerpolicy_unsafeurl_corssorigin_httpstohttp_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    },
    {
        "group": "referrerpolicy",
        "subgroup": "referrerpolicy_unsafeurl",
        "setup": "referrerpolicy_unsafeurl_crossorigin_httpstohttps_setup",
        "name": "referrerpolicy_unsafeurl_corssorigin_httpstohttps_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "referrer_matches_format"},
        "fail": {}
    }
]
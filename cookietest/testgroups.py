import logging
from saveresult.models import TestResult
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

# maps test groups to their subgroups. Used in structuring the result set
TEST_GROUPS_COOKIE = {"cookie": ["cookie_httponly", "cookie_expires", "cookie_subdomain", "cookie_maxage", "cookie_domain","cookie_domainreverse", "cookie_path", "cookie_samesite", "cookie_secure"]}

TEST_DEFINITIONS_COOKIE = [
# Cookie -----------------------------------------------------------------------------------------------------------------
    {
        "group": "cookie",
        "subgroup": "cookie_httponly",
        "setup": "cookie_httponly_setup",
        "name": "cookie_httponly_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_correct" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_httponly",
        "setup": "cookie_httponly_setup",
        "name": "cookie_httponly_client_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_accessed" }
    },
    
    
    {
        "group": "cookie",
        "subgroup": "cookie_expires",
        "setup": "cookie_expires_setup",
        "name": "cookie_expires_valid_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_expires",
        "setup": "cookie_expires_setup",
        "name": "cookie_expires_invalid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },
    
    
    
    {
        "group": "cookie",
        "subgroup": "cookie_maxage",
        "setup": "cookie_maxage_setup",
        "name": "cookie_maxage_negative_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },
    {
        "group": "cookie",
        "subgroup": "cookie_maxage",
        "setup": "cookie_maxage_setup",
        "name": "cookie_maxage_zero_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },
    {
        "group": "cookie",
        "subgroup": "cookie_maxage",
        "setup": "cookie_maxage_setup",
        "name": "cookie_maxage_positive_invalid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },
    {
        "group": "cookie",
        "subgroup": "cookie_maxage",
        "setup": "cookie_maxage_setup",
        "name": "cookie_maxage_positive_valid_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    
    
    
    {
        "group": "cookie",
        "subgroup": "cookie_subdomain",
        "setup": "cookie_subdomain_setup",
        "name": "cookie_subdomain_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },
         
         
         
    {
        "group": "cookie",
        "subgroup": "cookie_path",
        "setup": "cookie_path_setup",
        "name": "cookie_path_invalid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },
    {
        "group": "cookie",
        "subgroup": "cookie_path",
        "setup": "cookie_path_setup",
        "name": "cookie_path_exact_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_path",
        "setup": "cookie_path_setup",
        "name": "cookie_path_fuzzy_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
         
         
         
    {
        "group": "cookie",
        "subgroup": "cookie_domain",
        "setup": "cookie_domain_setup",
        "name": "cookie_domain_invalid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },
    {
        "group": "cookie",
        "subgroup": "cookie_domain",
        "setup": "cookie_domain_setup",
        "name": "cookie_domain_exact_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },
    {
        "group": "cookie",
        "subgroup": "cookie_domain",
        "setup": "cookie_domain_setup",
        "name": "cookie_domain_fuzzy_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
         
         
         
    {
        "group": "cookie",
        "subgroup": "cookie_domainreverse",
        "setup": "cookie_domainreverse_setup",
        "name": "cookie_domainreverse_invalid_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },
    {
        "group": "cookie",
        "subgroup": "cookie_domainreverse",
        "setup": "cookie_domainreverse_setup",
        "name": "cookie_domainreverse_exact_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },
    {
        "group": "cookie",
        "subgroup": "cookie_domainreverse",
        "setup": "cookie_domainreverse_setup",
        "name": "cookie_domainreverse_fuzzy_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    
    
    
    {
        "group": "cookie",
        "subgroup": "cookie_secure",
        "setup": "cookie_secure_setup",
        "name": "cookie_secure_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },
    {
        "group": "cookie",
        "subgroup": "cookie_secure",
        "setup": "cookie_securehttps_setup",
        "name": "cookie_securehttps_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },



    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_none_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_none_secure_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_lax_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_strict_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_none_external_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_none_secure_external_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_lax_external_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_strict_external_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    },



    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_none_img_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_none_secure_img_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_lax_img_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_strict_img_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_none_img_external_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_none_img_secure_external_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_lax_img_external_check",
        "success": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" },
        "fail": {}
    },
    {
        "group": "cookie",
        "subgroup": "cookie_samesite",
        "setup": "cookie_samesite_setup",
        "name": "cookie_samesite_strict_img_external_check",
        "success": {},
        "fail": { "operator": OPERATOR_EQUALS, "value": "cookie_is_set" }
    }
]
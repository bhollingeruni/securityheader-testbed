from django.http import HttpResponse, JsonResponse
from saveresult.utils import save
from testsuite.settings import CURRENT_ORIGIN
from testsuite.settings import CURRENT_DOMAIN
from testsuite.settings import SUBDOMAIN_DOMAIN
from testsuite.settings import SUBDOMAIN_ORIGIN
from testsuite.settings import CURRENT_SECURE_ORIGIN

# Create your views here.
def index(request):
    return HttpResponse('Cookie test index')



#-----------------------------------------------------------------------------------------------------------------------
# Test cookie header
#-----------------------------------------------------------------------------------------------------------------------

# Sets up a test to check if the cookie header is supported
def header_setup(request, test_id):
    response = JsonResponse(status=200, data={})
    response.set_cookie('cookie_header_test', test_id)
    save(test_id, "cookie_header_setup", "test_setup")
    return response

# Checks if the cookie has been set
def header_check(request, test_id):
    cookie_value = request.COOKIES.get('cookie_header_test')

    if cookie_value is None:
        # Cookie is not set
        save(test_id, "cookie_header_check", "cookie_not_set")
        return JsonResponse(status=200, data={})

    if cookie_value != test_id:
        # Cookie is not set
        save(test_id, "cookie_header_check", "cookie_wrong_value")
        return JsonResponse(status=200, data={})

    save(test_id, "cookie_header_check", "cookie_correct")
    return JsonResponse(status=200, data={})



#-----------------------------------------------------------------------------------------------------------------------
# Test httponly attribute
#-----------------------------------------------------------------------------------------------------------------------

# Sets up the httponly test by sending a cookie with httponly=true
def httponly_setup(request, test_id):
    response = JsonResponse(status=200, data={})
    response.set_cookie('cookie_httponly_test', test_id, httponly=True)
    save(test_id, "cookie_httponly_setup", "test_setup")
    return response

# Checks if the cookie are sent to the server correctly.
# Further validation happens on the client side (@see cookietest/static/cookietest/script.js)
def httponly_check(request, test_id):
    cookie_value = request.COOKIES.get('cookie_httponly_test')

    if cookie_value is not None and cookie_value == test_id:
        # Cookie is set
        save(test_id, "cookie_httponly_check", "cookie_correct")
        return JsonResponse(status=200, data={})
    else:
        # Cookie is not set
        save(test_id, "cookie_httponly_check", "cookie_is_not_set")
        return JsonResponse(status=200, data={})



#-----------------------------------------------------------------------------------------------------------------------
# Test expires attribute
#-----------------------------------------------------------------------------------------------------------------------

# sets up the expires test by sending an expired and an unexpired cookie.
def expires_setup(request, test_id):
    response = JsonResponse(status=200, data={})
    response.set_cookie('cookie_expires_test_invalid', test_id, expires="Sun, 01 Jan 2019 00:00:01 GMT")
    response.set_cookie('cookie_expires_test_valid', test_id, expires="Sun, 01 Jan 2100 00:00:01 GMT")
    save(test_id, "cookie_expires_setup", "test_setup")
    return response


def expires_check(request, test_id):

    # Check invalid cookie
    cookie_value_invalid = request.COOKIES.get('cookie_expires_test_invalid')

    if cookie_value_invalid is not None:
        # Invalid cookie is set: failed
        save(test_id, "cookie_expires_invalid_check", "cookie_is_set")
    else:
        # Invalid Cookie is not set: passed
        save(test_id, "cookie_expires_invalid_check", "cookie_is_not_set")

    # Check valid cookie
    cookie_value_valid = request.COOKIES.get('cookie_expires_test_valid')

    if cookie_value_valid is not None:
        # Cookie is set: passed
        save(test_id, "cookie_expires_valid_check", "cookie_is_set")

    else:
        # Cookie is not set: failed
        save(test_id, "cookie_expires_valid_check", "cookie_is_not_set")

    return JsonResponse(status=200, data={})



#-----------------------------------------------------------------------------------------------------------------------
# Test maxage attribute
#-----------------------------------------------------------------------------------------------------------------------

# Sets up the maxage test by sending four cookies:
# 1. max-age set to a negative value
# 2. max-age set to 0
# 3. max-age set to a small max-age that will expire before validation
# 4. max-age set to a larg max-age that will not expire before validation
def maxage_setup(request, test_id):
    response = JsonResponse(status=200, data={})
    response.set_cookie('cookie_maxage_test_negative', test_id, max_age=-10)
    response.set_cookie('cookie_maxage_test_zero', test_id, max_age=0)
    response.set_cookie('cookie_maxage_test_positive_invalid', test_id, max_age=1)
    response.set_cookie('cookie_maxage_test_positive_valid', test_id, max_age=1000)
    save(test_id, "cookie_maxage_setup", "test_setup")
    return response

# Checks which of the cookies are sent to the server
def maxage_check(request, test_id):

    # Check cookie with negative max-age value
    cookie_value_negative = request.COOKIES.get('cookie_maxage_test_negative')

    if cookie_value_negative is not None:
        # Cookie is set: failed
        save(test_id, "cookie_maxage_negative_check", "cookie_is_set")
    else:
        # Cookie is not set: passed
        save(test_id, "cookie_maxage_negative_check", "cookie_is_not_set")

    # CHeck cookie with max-age value = 0
    cookie_value_zero = request.COOKIES.get('cookie_maxage_test_zero')

    if cookie_value_zero is not None :
        # Cookie is set: failed
        save(test_id, "cookie_maxage_zero_check", "cookie_is_set")

    else:
        # Cookie is not set: passed
        save(test_id, "cookie_maxage_zero_check", "cookie_is_not_set")

    # Check cookie with small max-age value that is expired by now
    cookie_value_positive_invalid = request.COOKIES.get('cookie_maxage_test_positive_invalid')

    if cookie_value_positive_invalid is not None:
        # Cookie is set: failed
        save(test_id, "cookie_maxage_positive_invalid_check", "cookie_is_set")
    else:
        # Cookie is set: failed
        save(test_id, "cookie_maxage_positive_invalid_check", "cookie_is_not_set")

    # Check cookie with large max-age value that is not expired by now
    cookie_value_positive_valid = request.COOKIES.get('cookie_maxage_test_positive_valid')

    if cookie_value_positive_valid is not None and cookie_value_positive_valid == test_id:
        # Cookie is set: passed
        save(test_id, "cookie_maxage_positive_valid_check", "cookie_is_set")

    else:
        # Cookie is set: passed
        save(test_id, "cookie_maxage_positive_valid_check", "cookie_is_not_set")

    return JsonResponse(status=200, data={})



#-----------------------------------------------------------------------------------------------------------------------
# Test subdomain behaviour
#-----------------------------------------------------------------------------------------------------------------------

# Sets up the subdomain test
def subdomain_setup(request, test_id):
    response = JsonResponse(status=200, data={})
    response.set_cookie('cookie_subdomain_test', test_id)
    response['Access-Control-Allow-Origin'] = '*'
    save(test_id, "cookie_subdomain_setup", "test_setup")
    return response

# Checks if the subdomain cookie is set
def subdomain_check(request, test_id):
    cookie_value = request.COOKIES.get('cookie_subdomain_test')

    if cookie_value is not None:
        # Cookie is set: failed
        save(test_id, "cookie_subdomain_check", "cookie_is_set")
    else:
        # Cookie is not set: passed
        save(test_id, "cookie_subdomain_check", "cookie_is_not_set")

    return JsonResponse(status=200, data={})



#-----------------------------------------------------------------------------------------------------------------------
# Test path attribute
#-----------------------------------------------------------------------------------------------------------------------

# Sets up the path test by sending three cookies:
# 1. path attribute set to an invalid value
# 2. path attribute set to the exact path
# 3. path attribute set to the parent of the exact path
def path_setup(request, test_id):
    response = JsonResponse(status=200, data={})
    response.set_cookie('cookie_path_test_invalid', test_id, path='/invalid/path')
    response.set_cookie('cookie_path_test_exact', test_id, path='/cookietest/path_check/'+test_id)
    response.set_cookie('cookie_path_test_fuzzy', test_id, path='/cookietest')
    save(test_id, "cookie_path_setup", "test_setup")
    return response

# Checks if the cookies are set
def path_check(request, test_id):

    # Check the cookie with the invalid path
    cookie_value_invalid = request.COOKIES.get('cookie_path_test_invalid')

    if cookie_value_invalid is not None and cookie_value_invalid == test_id:
        # Cookie is set: failed
        save(test_id, "cookie_path_invalid_check", "cookie_is_set")
    else:
        # Cookie is not set: passed
        save(test_id, "cookie_path_invalid_check", "cookie_is_not_set")

    # Check the cookie with the exact path
    cookie_value_exact = request.COOKIES.get('cookie_path_test_exact')

    if cookie_value_exact is not None and cookie_value_exact == test_id:
        # Cookie is set: passed
        save(test_id, "cookie_path_exact_check", "cookie_is_set")
    else:
        # Cookie is not set: failed
        save(test_id, "cookie_path_exact_check", "cookie_is_not_set")

    # Check the cookie with the parent path
    cookie_value_fuzzy = request.COOKIES.get('cookie_path_test_fuzzy')

    if cookie_value_fuzzy is not None or cookie_value_fuzzy == test_id:
        # Cookie is set: passed
        save(test_id, "cookie_path_fuzzy_check", "cookie_is_set")
    else:
        # Cookie is not set: failed
        save(test_id, "cookie_path_fuzzy_check", "cookie_is_not_set")

    return JsonResponse(status=200, data={})



#-----------------------------------------------------------------------------------------------------------------------
# Test domain attribute
#-----------------------------------------------------------------------------------------------------------------------

# Sets up the domain test by sending three cookies:
# 1. domain attribute set to an invalid value
# 2. domain attribute set to the exact path
# 3. domain attribute set to the parent domain of the exact value
def domain_setup(request, test_id):
    response = HttpResponse('cookie_domain_setup')
    response.set_cookie('cookie_domain_test_invalid', test_id, domain='.invaliddomain.test', samesite=None)
    response.set_cookie('cookie_domain_test_exact', test_id, domain=SUBDOMAIN_DOMAIN, samesite=None)
    response.set_cookie('cookie_domain_test_fuzzy', test_id, domain=CURRENT_DOMAIN, samesite=None)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Credentials'] = 'true'
    save(test_id, "cookie_domain_setup", "test_setup")
    return response


# Checks if the domain cookies are sent
def domain_check(request, test_id):
    # Check the cookie with the invalid domain
    cookie_value_invalid = request.COOKIES.get('cookie_domain_test_invalid')

    if cookie_value_invalid is not None and cookie_value_invalid == test_id:
        # Cookie is set: failed
        save(test_id, "cookie_domain_invalid_check", "cookie_is_set")
    else:
        # Cookie is not set: passed
        save(test_id, "cookie_domain_invalid_check", "cookie_is_not_set")

    # Check the cookie with the exact domain
    cookie_value_exact = request.COOKIES.get('cookie_domain_test_exact')

    if cookie_value_exact is not None and cookie_value_exact == test_id:
        # Cookie is set: failed
        save(test_id, "cookie_domain_exact_check", "cookie_is_set")
    else:
        # Cookie is not set: passed
        save(test_id, "cookie_domain_exact_check", "cookie_is_not_set")

    # Check the cookie with the parent domain
    cookie_value_fuzzy = request.COOKIES.get('cookie_domain_test_fuzzy')

    if cookie_value_fuzzy is not None and cookie_value_fuzzy == test_id:
        # Cookie is set
        save(test_id, "cookie_domain_fuzzy_check", "cookie_is_set")
    else:
        # Cookie is not set
        save(test_id, "cookie_domain_fuzzy_check", "cookie_is_not_set")

    return JsonResponse(status=200, data={})

# Sets up the reverse of the domain test
def domainreverse_setup(request, test_id):
    response = HttpResponse('cookie_domainreverse_setup')
    response.set_cookie('cookie_domainreverse_test_invalid', test_id, domain='.invaliddomain.test', samesite=None)
    response.set_cookie('cookie_domainreverse_test_exact', test_id, domain=SUBDOMAIN_ORIGIN, samesite=None)
    response.set_cookie('cookie_domainreverse_test_fuzzy', test_id, domain=CURRENT_DOMAIN, samesite=None)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Credentials'] = 'true'
    save(test_id, "cookie_domainreverse_setup", "test_setup")
    return response


def domainreverse_check(request, test_id):

    # Check the cookie with the invalid domain
    cookie_value_invalid = request.COOKIES.get('cookie_domainreverse_test_invalid')

    if cookie_value_invalid is not None and cookie_value_invalid == test_id:
        # Cookie is set: failed
        save(test_id, "cookie_domainreverse_invalid_check", "cookie_is_set")
    else:
        # Cookie is not set: passed
        save(test_id, "cookie_domainreverse_invalid_check", "cookie_is_not_set")


    # Check the cookie with the exact domain
    cookie_value_exact = request.COOKIES.get('cookie_domainreverse_test_exact')

    if cookie_value_exact is not None and cookie_value_exact == test_id:
        # Cookie is set: failed
        save(test_id, "cookie_domainreverse_exact_check", "cookie_is_set")
    else:
        # Cookie ist not set: passed
        save(test_id, "cookie_domainreverse_exact_check", "cookie_is_not_set")

    # Check the cookie with the parent domain
    cookie_value_fuzzy = request.COOKIES.get('cookie_domainreverse_test_fuzzy')

    if cookie_value_fuzzy is not None and cookie_value_fuzzy == test_id:
        # Cookie is set: passed
        save(test_id, "cookie_domainreverse_fuzzy_check", "cookie_is_set")
    else:
        # Cookie is not set
        save(test_id, "cookie_domainreverse_fuzzy_check", "cookie_is_not_set")

    response = JsonResponse(status=200, data={})
    response['Access-Control-Allow-Origin'] = CURRENT_ORIGIN
    response['Access-Control-Allow-Credentials'] = 'true'
    return response



#-----------------------------------------------------------------------------------------------------------------------
# Test secure attribute
#-----------------------------------------------------------------------------------------------------------------------

# Sets up the secure test by sending a secure cookie
def secure_setup(request, test_id):
    response = JsonResponse(status=200, data={})
    response.set_cookie('cookie_secure_test', test_id, secure=True)
    save(test_id, "cookie_secure_setup", "test_setup")
    return response

# Checks if the secure cookie is sent over HTTP
def secure_check(request, test_id):
    cookie_value = request.COOKIES.get('cookie_secure_test')

    if cookie_value is not None and cookie_value == test_id:
        # Cookie is set: failed
        save(test_id, "cookie_secure_check", "cookie_is_set")
    else:
        # Cookie is not set: passed
        save(test_id, "cookie_secure_check", "cookie_is_not_set")

    response = JsonResponse(status=200, data={})
    response['Access-Control-Allow-Origin'] = CURRENT_ORIGIN
    response['Access-Control-Allow-Credentials'] = 'true'
    return response


# Sets up the secure test by sending a secure cookie over HTTPS
def securehttps_setup(request, test_id):
    response = JsonResponse(status=200, data={})
    response.set_cookie('cookie_securehttps_test', test_id, secure=True)
    response['Access-Control-Allow-Origin'] = CURRENT_ORIGIN
    response['Access-Control-Allow-Credentials'] = 'true'
    save(test_id, "cookie_securehttps_setup", "test_setup")
    return response

# Checks if the secure cookie is sent over HTTP
def securehttps_check(request, test_id):
    cookie_value = request.COOKIES.get('cookie_securehttps_test')

    if cookie_value is not None and cookie_value == test_id:
        # Cookie is set: passed
        save(test_id, "cookie_securehttps_check", "cookie_is_set")
    else:
        # Cookie is not set: failed
        save(test_id, "cookie_securehttps_check", "cookie_is_not_set")

    response = JsonResponse(status=200, data={})
    response['Access-Control-Allow-Origin'] = CURRENT_ORIGIN
    response['Access-Control-Allow-Credentials'] = 'true'
    return response

# Sets up the sameSite test by sending sameSite cookies
def samesite_setup(request, test_id):
    response = JsonResponse(status=200, data={})
    response.set_cookie('cookie_samesite_none_test', test_id, samesite=None)
    response.set_cookie('cookie_samesite_none_secure_test', test_id, secure=True, samesite=None)
    response.set_cookie('cookie_samesite_lax_test', test_id, samesite="lax")
    response.set_cookie('cookie_samesite_strict_test', test_id, samesite="strict")
    response.set_cookie('cookie_samesite_none_external_test', test_id, samesite=None)
    response.set_cookie('cookie_samesite_none_secure_external_test', test_id, secure=True, samesite=None)
    response.set_cookie('cookie_samesite_lax_external_test', test_id, samesite="lax")
    response.set_cookie('cookie_samesite_strict_external_test', test_id, samesite="strict")
    response.set_cookie('cookie_samesite_none_img_test', test_id, samesite=None)
    response.set_cookie('cookie_samesite_none_secure_img_test', test_id, secure=True, samesite=None)
    response.set_cookie('cookie_samesite_lax_img_test', test_id, samesite="lax")
    response.set_cookie('cookie_samesite_strict_img_test', test_id, samesite="strict")
    response.set_cookie('cookie_samesite_none_img_external_test', test_id, samesite=None)
    response.set_cookie('cookie_samesite_none_secure_img_external_test', test_id, secure=True, samesite=None)
    response.set_cookie('cookie_samesite_lax_img_external_test', test_id, samesite="lax")
    response.set_cookie('cookie_samesite_strict_img_external_test', test_id, samesite="strict")
    response['Access-Control-Allow-Origin'] = CURRENT_ORIGIN
    response['Access-Control-Allow-Credentials'] = 'true'
    save(test_id, "cookie_samesite_setup", "test_setup")
    return response

# Checks if the secure cookie is sent over HTTP
def samesite_check(request, test_id, value):
    cookie_value = request.COOKIES.get('cookie_samesite_{value}_test'.format(value=value))

    if cookie_value is not None and cookie_value == test_id:
        # Cookie is set
        save(test_id, "cookie_samesite_{value}_check".format(value=value), "cookie_is_set")
    else:
        # Cookie is not set: failed
        save(test_id, "cookie_samesite_{value}_check".format(value=value), "cookie_is_not_set")

    response = JsonResponse(status=200, data={})
    response['Access-Control-Allow-Origin'] = CURRENT_ORIGIN
    response['Access-Control-Allow-Credentials'] = 'true'
    return response


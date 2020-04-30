from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from saveresult.utils import save
import re
import logging
from testsuite.settings import CURRENT_SECURE_ORIGIN

def index(request):
    response = HttpResponse('Referrer-Policy test index')
    return response



#-----------------------------------------------------------------------------------------------------------------------
# Test value: header not set
#-----------------------------------------------------------------------------------------------------------------------

# Setup test without header from HTTP to HTTP
def none_httptohttp_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/none_httptohttp_setup.html', context)
    save(test_id, "referrerpolicy_none_httptohttp_setup", "test_setup")
    return response

# Setup test without header from HTTP to HTTPS
def none_httptohttps_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/none_httptohttps_setup.html', context)
    save(test_id, "referrerpolicy_none_httptohttps_setup", "test_setup")
    return response

# Setup test without header from HTTPS to HTTP
def none_httpstohttp_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/none_httpstohttp_setup.html', context)
    save(test_id, "referrerpolicy_none_httpstohttp_setup", "test_setup")
    return response

# Setup test without header from HTTPS to HTTPS
def none_httpstohttps_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/none_httpstohttps_setup.html', context)
    save(test_id, "referrerpolicy_none_httpstohttps_setup", "test_setup")
    return response

# Check if referrer is sent from HTTP to HTTP
def none_httptohttp_check(request, test_id):
    # from HTTP to HTTP: should send referrer
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_none_httptohttp_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_none_httptohttp_check', 'no_referrer_sent')
    else:
        save(test_id, 'referrerpolicy_none_httptohttp_check', 'referrer_sent')
    return HttpResponse('Referrer-Policy referrerpolicy_none_httptohttp')

# Check if referrer is sent from HTTP to HTTPS
def none_httptohttps_check(request, test_id):
    # from HTTP to HTTPS: should send referrer
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_none_httptohttps_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_none_httptohttps_check', 'no_referrer_sent')
    else:
        save(test_id, 'referrerpolicy_none_httptohttps_check', 'referrer_sent')
    return HttpResponse('Referrer-Policy referrerpolicy_none_httptohttps')

# Check if referrer is sent from HTTPS to HTTP
def none_httpstohttp_check(request, test_id):
    # from HTTPS to HTTP: should not send any referrer information
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_none_httpstohttp_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_none_httpstohttp_check', 'no_referrer_sent')
    else:
        save(test_id, 'referrerpolicy_none_httpstohttp_check', 'referrer_sent')
    return HttpResponse('Referrer-Policy referrerpolicy_none_httpstohttp')

# Check if referrer is sent from HTTPS to HTTPS
def none_httpstohttps_check(request, test_id):
    # from HTTPS to HTTPS: should send referrer
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_none_httpstohttps_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_none_httpstohttps_check', 'no_referrer_sent')
    else:
        save(test_id, 'referrerpolicy_none_httpstohttps_check', 'referrer_sent')
    return HttpResponse('Referrer-Policy referrerpolicy_none_httpstohttps')



#-----------------------------------------------------------------------------------------------------------------------
# Test value: no-referrer
#-----------------------------------------------------------------------------------------------------------------------

# Setup test with header set to no-referrer
def noreferrer_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/noreferrer_setup.html', context)
    response['Referrer-Policy'] = 'no-referrer'
    save(test_id, "referrerpolicy_noreferrer_setup", "test_setup")

    return response

# CHeck if referrer is sent
def noreferrer_check(request, test_id):
    # should not send any referrer information
    referrer = request.META.get('HTTP_REFERER')
    if not referrer:
        save(test_id, 'referrerpolicy_noreferrer_check', 'no_referrer_sent')
    else:
        save(test_id, 'referrerpolicy_noreferrer_check_value', referrer)
        save(test_id, 'referrerpolicy_noreferrer_check', 'referrer_sent')
    return HttpResponse('Referrer-Policy norreferrer')



#-----------------------------------------------------------------------------------------------------------------------
# Test value: no-referrer-when-downgrade
#-----------------------------------------------------------------------------------------------------------------------

# Setup test with header set to no-referrer-when-downgrade (HTTP to HTTP)
def noreferrerwhendowngrade_httptohttp_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/noreferrerwhendowngrade_httptohttp_setup.html', context)
    response['Referrer-Policy'] = 'no-referrer-when-downgrade'
    save(test_id, "referrerpolicy_noreferrerwhendowngrade_httptohttp_setup", "test_setup")
    return response

# Setup test with header set to no-referrer-when-downgrade (HTTP to HTTPS)
def noreferrerwhendowngrade_httptohttps_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/noreferrerwhendowngrade_httptohttps_setup.html', context)
    response['Referrer-Policy'] = 'no-referrer-when-downgrade'
    save(test_id, "referrerpolicy_noreferrerwhendowngrade_httptohttps_setup", "test_setup")
    return response

# Setup test with header set to no-referrer-when-downgrade (HTTPS to HTTP)
def noreferrerwhendowngrade_httpstohttp_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/noreferrerwhendowngrade_httpstohttp_setup.html', context)
    response['Referrer-Policy'] = 'no-referrer-when-downgrade'
    save(test_id, "referrerpolicy_noreferrerwhendowngrade_httpstohttp_setup", "test_setup")
    return response

# Setup test with header set to no-referrer-when-downgrade (HTTPS to HTTPS)
def noreferrerwhendowngrade_httpstohttps_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/noreferrerwhendowngrade_httpstohttps_setup.html', context)
    response['Referrer-Policy'] = 'no-referrer-when-downgrade'
    save(test_id, "referrerpolicy_noreferrerwhendowngrade_httpstohttps_setup", "test_setup")
    return response

# CHeck if referrer is sent HTTP to HTTP
def noreferrerwhendowngrade_httptohttp_check(request, test_id):
    # from HTTP to HTTP: should send referrer
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_noreferrerwhendowngrade_httptohttp_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_noreferrerwhendowngrade_httptohttp_check', 'no_referrer_sent')
    else:
        save(test_id, 'referrerpolicy_noreferrerwhendowngrade_httptohttp_check', 'referrer_sent')
    return HttpResponse('Referrer-Policy referrerpolicy_noreferrerwhendowngrade_httptohttp')

# CHeck if referrer is sent HTTP to HTTPS
def noreferrerwhendowngrade_httptohttps_check(request, test_id):
    # from HTTP to HTTPS: should send referrer
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_noreferrerwhendowngrade_httptohttps_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_noreferrerwhendowngrade_httptohttps_check', 'no_referrer_sent')
    else:
        save(test_id, 'referrerpolicy_noreferrerwhendowngrade_httptohttps_check', 'referrer_sent')
    return HttpResponse('Referrer-Policy referrerpolicy_noreferrerwhendowngrade_httptohttps')

# CHeck if referrer is sent HTTPS to HTTP
def noreferrerwhendowngrade_httpstohttp_check(request, test_id):
    # from HTTPS to HTTP: should not send any referrer information
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_noreferrerwhendowngrade_httpstohttp_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_noreferrerwhendowngrade_httpstohttp_check', 'no_referrer_sent')
    else:
        save(test_id, 'referrerpolicy_noreferrerwhendowngrade_httpstohttp_check', 'referrer_sent')
    return HttpResponse('Referrer-Policy referrerpolicy_noreferrerwhendowngrade_httpstohttp')

# Checks if referrer is sent HTTPS to HTTPS
def noreferrerwhendowngrade_httpstohttps_check(request, test_id):
    # from HTTPS to HTTPS: should send referrer
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_noreferrerwhendowngrade_httpstohttps_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_noreferrerwhendowngrade_httpstohttps_check', 'no_referrer_sent')
    else:
        save(test_id, 'referrerpolicy_noreferrerwhendowngrade_httpstohttps_check', 'referrer_sent')
    return HttpResponse('Referrer-Policy referrerpolicy_noreferrerwhendowngrade_httpstohttps')



#-----------------------------------------------------------------------------------------------------------------------
# Test value: same-origin
#-----------------------------------------------------------------------------------------------------------------------

# Setup test with header set to same-origin (request from same origin)
def sameorigin_sameorigin_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/sameorigin_sameorigin_setup.html', context)
    response['Referrer-Policy'] = 'same-origin'
    save(test_id, "referrerpolicy_sameorigin_sameorigin_setup", "test_setup")
    return response

# Setup test with header set to same-origin (request from cross origin)
def sameorigin_crossorigin_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/sameorigin_crossorigin_setup.html', context)
    response['Referrer-Policy'] = 'same-origin'
    save(test_id, "referrerpolicy_sameorigin_crossorigin_setup", "test_setup")
    return response

# Checks if referrer is sent from same origin
def sameorigin_sameorigin_check(request, test_id):
    # send referrer
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_sameorigin_sameorigin_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_sameorigin_sameorigin_check', 'no_referrer_sent')
    else:
        save(test_id, 'referrerpolicy_sameorigin_sameorigin_check', 'referrer_sent')
    return HttpResponse('Referrer-Policy sameorigin sameorigin')

# Checks if referrer is sent from cross origin
def sameorigin_crossorigin_check(request, test_id):
    # send no referrer information
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_sameorigin_crossorigin_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_sameorigin_crossorigin_check', 'no_referrer_sent')
    else:
        save(test_id, 'referrerpolicy_sameorigin_crossorigin_check', 'referrer_sent')
    return HttpResponse('Referrer-Policy sameorigin crossorigin')



#-----------------------------------------------------------------------------------------------------------------------
# Test value: origin
#-----------------------------------------------------------------------------------------------------------------------

# Sets up test with header set to origin
def origin_setup(request, test_id):
    # only send origin
    context = { 'test_id': test_id, 'current_secure_origin': CURRENT_SECURE_ORIGIN }
    response = render(request, 'referrerpolicytest/origin_setup.html', context)
    response['Referrer-Policy'] = 'origin'
    save(test_id, "referrerpolicy_origin_setup", "test_setup")
    return response

# Checks if only the origin information was sent
def origin_check(request, test_id, value):
    # only send origin (protocol://domain.tld/), not complete URL
    response = HttpResponse('Referrer-Policy origin')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_origin_{value}_check_value'.format(value=value), referrer)
    # check if referrer is empty
    if not referrer:
        save(test_id, 'referrerpolicy_origin_{value}_check'.format(value=value), 'no_referrer_sent')
        return response

    # test if referrer matches format protocol://domain.tld(:port)/ (note the trailing slash)
    if validate_origin_format(referrer):
        save(test_id, 'referrerpolicy_origin_{value}_check'.format(value=value), 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_origin_{value}_check'.format(value=value), 'referrer_invalid_format')
    return response



#-----------------------------------------------------------------------------------------------------------------------
# Test value: strict-origin
#-----------------------------------------------------------------------------------------------------------------------

# Sets up test with header set to strict-origin (HTTP to HTTP)
def strictorigin_httptohttp_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/strictorigin_httptohttp_setup.html', context)
    response['Referrer-Policy'] = 'strict-origin'
    save(test_id, "referrerpolicy_strictorigin_httptohttp_setup", "test_setup")
    return response

# Sets up test with header set to strict-origin (HTTP to HTTPS)
def strictorigin_httptohttps_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/strictorigin_httptohttps_setup.html', context)
    response['Referrer-Policy'] = 'strict-origin'
    save(test_id, "referrerpolicy_strictorigin_httptohttps_setup", "test_setup")
    return response

# Sets up test with header set to strict-origin (HTTPS to HTTP)
def strictorigin_httpstohttp_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/strictorigin_httpstohttp_setup.html', context)
    response['Referrer-Policy'] = 'strict-origin'
    save(test_id, "referrerpolicy_strictorigin_httpstohttp_setup", "test_setup")
    return response

# Sets up test with header set to strict-origin (HTTPS to HTTPS)
def strictorigin_httpstohttps_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/strictorigin_httpstohttps_setup.html', context)
    response['Referrer-Policy'] = 'strict-origin'
    save(test_id, "referrerpolicy_strictorigin_httpstohttps_setup", "test_setup")
    return response

# Checks if referrer is sent (HTTP to HTTP)
def strictorigin_httptohttp_check(request, test_id):
    # from HTTP to HTTP: should send referrer
    response = HttpResponse('Referrer-Policy referrerpolicy_strictorigin_httptohttp')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_strictorigin_httptohttp_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_strictorigin_httptohttp_check', 'no_referrer_sent')
        return response

    if validate_origin_format(referrer):
        save(test_id, 'referrerpolicy_strictorigin_httptohttp_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_strictorigin_httptohttp_check', 'referrer_invalid_format')
    return response

# Checks if referrer is sent (HTTP to HTTPS)
def strictorigin_httptohttps_check(request, test_id):
    # from HTTP to HTTPS: should send referrer
    response = HttpResponse('Referrer-Policy referrerpolicy_strictorigin_httptohttps')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_strictorigin_httptohttps_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_strictorigin_httptohttps_check', 'no_referrer_sent')
        return response

    if validate_origin_format(referrer):
        save(test_id, 'referrerpolicy_strictorigin_httptohttps_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_strictorigin_httptohttps_check', 'referrer_invalid_format')
    return response

# Checks if referrer is sent (HTTPS to HTTP)
def strictorigin_httpstohttp_check(request, test_id):
    # from HTTPS to HTTP: should not send any referrer information
    response = HttpResponse('Referrer-Policy referrerpolicy_strictorigin_httpstohttp')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_strictorigin_httpstohttp_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_strictorigin_httpstohttp_check', 'no_referrer_sent')
        return response

    if validate_origin_format(referrer):
        save(test_id, 'referrerpolicy_strictorigin_httpstohttp_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_strictorigin_httpstohttp_check', 'referrer_invalid_format')
    return response

# Checks if referrer is sent (HTTPS to HTTPS)
def strictorigin_httpstohttps_check(request, test_id):
    # from HTTPS to HTTPS: should send referrer
    response = HttpResponse('Referrer-Policy referrerpolicy_strictorigin_httpstohttps')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_strictorigin_httpstohttps_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_strictorigin_httpstohttps_check', 'no_referrer_sent')
        return response

    if validate_origin_format(referrer):
        save(test_id, 'referrerpolicy_strictorigin_httpstohttps_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_strictorigin_httpstohttps_check', 'referrer_invalid_format')
    return response



#-----------------------------------------------------------------------------------------------------------------------
# Test value: origin-when-cross-origin
#-----------------------------------------------------------------------------------------------------------------------

# Sets up test with header set to origin-when-cross-origin (request from same origin)
def originwhencrossorigin_sameorigin_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/originwhencrossorigin_sameorigin_setup.html', context)
    response['Referrer-Policy'] = 'origin-when-cross-origin'
    save(test_id, "referrerpolicy_originwhencrossorigin_sameorigin_setup", "test_setup")
    return response

# Sets up test with header set to origin-when-cross-origin (request from cross origin)
def originwhencrossorigin_crossorigin_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/originwhencrossorigin_crossorigin_setup.html', context)
    response['Referrer-Policy'] = 'origin-when-cross-origin'
    save(test_id, "referrerpolicy_originwhencrossorigin_crossorigin_setup", "test_setup")
    return response

# Checks which referrer information was sent from same origin
def originwhencrossorigin_sameorigin_check(request, test_id):
    # send full URL
    response = HttpResponse('Referrer-Policy referrerpolicy_originwhencrossorigin_sameorigin')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_originwhencrossorigin_sameorigin_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_originwhencrossorigin_sameorigin_check', 'no_referrer_sent')
        return response

    if validate_url_format(referrer):
        save(test_id, 'referrerpolicy_originwhencrossorigin_sameorigin_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_originwhencrossorigin_sameorigin_check', 'referrer_invalid_format')
    return response

# Checks which referrer information was sent from same origin
def originwhencrossorigin_crossorigin_check(request, test_id):
    # send origin only
    response = HttpResponse('Referrer-Policy referrerpolicy_originwhencrossorigin_crossorigin')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_originwhencrossorigin_crossorigin_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_originwhencrossorigin_crossorigin_check', 'no_referrer_sent')
        return response

    if validate_origin_format(referrer):
        save(test_id, 'referrerpolicy_originwhencrossorigin_crossorigin_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_originwhencrossorigin_crossorigin_check', 'referrer_invalid_format')
    return response



#-----------------------------------------------------------------------------------------------------------------------
# Test value: strict-origin-when-cross-origin
#-----------------------------------------------------------------------------------------------------------------------

# Sets up test with header set to strict-origin-when-cross-origin (request from same origin)
def strictoriginwhencrossorigin_sameorigin_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/strictoriginwhencrossorigin_sameorigin_setup.html', context)
    response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    save(test_id, "referrerpolicy_strictoriginwhencrossorigin_sameorigin_setup", "test_setup")
    return response

# Sets up test with header set to strict-origin-when-cross-origin (request from cross origin, HTTP to HTTP)
def strictoriginwhencrossorigin_crossorigin_httptohttp_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/strictoriginwhencrossorigin_crossorigin_httptohttp_setup.html', context)
    response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    save(test_id, "referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttp_setup", "test_setup")
    return response

# Sets up test with header set to strict-origin-when-cross-origin (request from cross origin, HTTP to HTTPS)
def strictoriginwhencrossorigin_crossorigin_httptohttps_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/strictoriginwhencrossorigin_crossorigin_httptohttps_setup.html', context)
    response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    save(test_id, "referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttps_setup", "test_setup")
    return response

# Sets up test with header set to strict-origin-when-cross-origin (request from cross origin, HTTPS to HTTP)
def strictoriginwhencrossorigin_crossorigin_httpstohttp_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/strictoriginwhencrossorigin_crossorigin_httpstohttp_setup.html', context)
    response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    save(test_id, "referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttp_setup", "test_setup")
    return response

# Sets up test with header set to strict-origin-when-cross-origin (request from cross origin, HTTPS to HTTPS)
def strictoriginwhencrossorigin_crossorigin_httpstohttps_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/strictoriginwhencrossorigin_crossorigin_httpstohttps_setup.html', context)
    response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    save(test_id, "referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttps_setup", "test_setup")
    return response

# Checks if the correct referrer information was sent (request from same origin)
def strictoriginwhencrossorigin_sameorigin_check(request, test_id):
    # send full URL
    response = HttpResponse('Referrer-Policy referrerpolicy_strictoriginwhencrossorigin_sameorigin')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_sameorigin_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_sameorigin_check', 'no_referrer_sent')
        return response

    if validate_url_format(referrer):
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_sameorigin_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_sameorigin_check', 'referrer_invalid_format')
    return response

# Checks if the correct referrer information was sent (request from cross origin, HTTP to HTTP)
def strictoriginwhencrossorigin_crossorigin_httptohttp_check(request, test_id):
    # send origin only
    response = HttpResponse('Referrer-Policy referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttp')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttp_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttp_check', 'no_referrer_sent')
        return response

    if validate_origin_format(referrer):
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttp_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttp_check', 'referrer_invalid_format')
    return response

# Checks if the correct referrer information was sent (request from cross origin, HTTP to HTTPS)
def strictoriginwhencrossorigin_crossorigin_httptohttps_check(request, test_id):
    # send origin only
    response = HttpResponse('Referrer-Policy referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttps')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttps_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttps_check', 'no_referrer_sent')
        return response

    if validate_origin_format(referrer):
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttps_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httptohttps_check', 'referrer_invalid_format')
    return response

# Checks if the correct referrer information was sent (request from cross origin, HTTPS to HTTP)
def strictoriginwhencrossorigin_crossorigin_httpstohttp_check(request, test_id):
    # send no referrer
    response = HttpResponse('Referrer-Policy referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttp')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttp_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttp_check', 'no_referrer_sent')
        return response
    else:
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttp_check', 'referrer_sent')
    return response

# Checks if the correct referrer information was sent (request from cross origin, HTTPS to HTTPS)
def strictoriginwhencrossorigin_crossorigin_httpstohttps_check(request, test_id):
    # send origin only
    response = HttpResponse('Referrer-Policy referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttps')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttps_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttps_check', 'no_referrer_sent')
        return response

    if validate_origin_format(referrer):
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttps_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_strictoriginwhencrossorigin_crossorigin_httpstohttps_check', 'referrer_invalid_format')
    return response



#-----------------------------------------------------------------------------------------------------------------------
# Test value: unsafe-url
#-----------------------------------------------------------------------------------------------------------------------

# Sets up the test with header set to unsafe-url (request from same origin)
def unsafeurl_sameorigin_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/unsafeurl_sameorigin_setup.html', context)
    response['Referrer-Policy'] = 'unsafe-url'
    save(test_id, "referrerpolicy_unsafeurl_sameorigin_setup", "test_setup")
    return response

# Sets up the test with header set to unsafe-url (request from cross origin, HTTP to HTTP)
def unsafeurl_crossorigin_httptohttp_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/unsafeurl_crossorigin_httptohttp_setup.html', context)
    response['Referrer-Policy'] = 'unsafe-url'
    save(test_id, "referrerpolicy_unsafeurl_crossorigin_httptohttp_setup", "test_setup")
    return response

# Sets up the test with header set to unsafe-url (request from cross origin, HTTP to HTTPS)
def unsafeurl_crossorigin_httptohttps_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/unsafeurl_crossorigin_httptohttps_setup.html', context)
    response['Referrer-Policy'] = 'unsafe-url'
    save(test_id, "referrerpolicy_unsafeurl_crossorigin_httptohttps_setup", "test_setup")
    return response

# Sets up the test with header set to unsafe-url (request from cross origin, HTTPS to HTTP)
def unsafeurl_crossorigin_httpstohttp_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/unsafeurl_crossorigin_httpstohttp_setup.html', context)
    response['Referrer-Policy'] = 'unsafe-url'
    save(test_id, "referrerpolicy_unsafeurl_crossorigin_httpstohttp_setup", "test_setup")
    return response

# Sets up the test with header set to unsafe-url (request from cross origin, HTTPS to HTTPS)
def unsafeurl_crossorigin_httpstohttps_setup(request, test_id):
    context = { 'test_id': test_id }
    response = render(request, 'referrerpolicytest/unsafeurl_crossorigin_httpstohttps_setup.html', context)
    response['Referrer-Policy'] = 'unsafe-url'
    save(test_id, "referrerpolicy_unsafeurl_crossorigin_httpstohttps_setup", "test_setup")
    return response

# Checks if the correct referrer information was sent (request from same origin)
def unsafeurl_sameorigin_check(request, test_id):
    # send full url
    response = HttpResponse('Referrer-Policy referrerpolicy_unsafeurl_sameorigin')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_unsafeurl_sameorigin_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_unsafeurl_sameorigin_check', 'no_referrer_sent')
        return response

    if validate_url_format(referrer):
        save(test_id, 'referrerpolicy_unsafeurl_sameorigin_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_unsafeurl_sameorigin_check', 'referrer_invalid_format')
    return response

# Checks if the correct referrer information was sent (request from cross origin, HTTP to HTTP)
def unsafeurl_crossorigin_httptohttp_check(request, test_id):
    # send full url
    response = HttpResponse('Referrer-Policy referrerpolicy_unsafeurl_corssorigin_httptohttp')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httptohttp_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httptohttp_check', 'no_referrer_sent')
        return response

    if validate_url_format(referrer):
        save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httptohttp_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httptohttp_check', 'referrer_invalid_format')
    return response

# Checks if the correct referrer information was sent (request from cross origin, HTTP to HTTPS)
def unsafeurl_crossorigin_httptohttps_check(request, test_id):
    # send full url
    response = HttpResponse('Referrer-Policy referrerpolicy_unsafeurl_corssorigin_httptohttps')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httptohttps_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httptohttps_check', 'no_referrer_sent')
        return response

    if validate_url_format(referrer):
        save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httptohttps_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httptohttps_check', 'referrer_invalid_format')
    return response

# Checks if the correct referrer information was sent (request from cross origin, HTTPS to HTTP)
def unsafeurl_crossorigin_httpstohttp_check(request, test_id):
    # send full url
    response = HttpResponse('Referrer-Policy referrerpolicy_unsafeurl_corssorigin_httpstohttp')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httpstohttp_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httpstohttp_check', 'no_referrer_sent')
        return response

    if validate_url_format(referrer):
        save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httpstohttp_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httpstohttp_check', 'referrer_invalid_format')
    return response

# Checks if the correct referrer information was sent (request from cross origin, HTTPS to HTTPS)
def unsafeurl_crossorigin_httpstohttps_check(request, test_id):
    # send full url
    response = HttpResponse('Referrer-Policy referrerpolicy_unsafeurl_corssorigin_httpstohttps')
    referrer = request.META.get('HTTP_REFERER')
    save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httpstohttps_check_value', referrer)
    if not referrer:
        save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httpstohttps_check', 'no_referrer_sent')
        return response

    if validate_url_format(referrer):
        save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httpstohttps_check', 'referrer_matches_format')
    else:
        save(test_id, 'referrerpolicy_unsafeurl_corssorigin_httpstohttps_check', 'referrer_invalid_format')
    return response



# ----------------------------------------------------------------------------------------------------------------------
# Utility functions
# ----------------------------------------------------------------------------------------------------------------------

def validate_origin_format(origin):
    regex = re.compile("https?://[a-zA-Z0-9.-]+(:[0-9]+)?/$")
    return regex.match(origin)

def validate_url_format(origin):
    regex = re.compile("https?://[a-zA-Z0-9.-]+(:[0-9]+)?/[a-zA-Z0-9.-/]*")
    return regex.match(origin)

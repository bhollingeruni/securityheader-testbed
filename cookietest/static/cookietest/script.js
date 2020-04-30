function cookie_tests() {
    return $.when(
        cookie_header_test(),
        cookie_httponly_test(),
        cookie_expires_test(),
        cookie_subdomain_test(),
        cookie_path_test(),
        cookie_secure_test(),
        cookie_domain_test(),
        cookie_domainreverse_test(),
        cookie_maxage_test(),
        cookie_samesite_test()
    )

}


// ----------------- Cookie test: set header -----------------------------------------------------------------------

/**
 * Tests whether the header Set-Cookie is implemented.
 * Setup: request the setup URL. The response contains the Set-Cookie header.
 * Check: request the check URL. The response body is "cookie_correct" if the cookie was sent with the request.
 * Process: Test is passed if the cookie is set by the response header and sent with the check request.
 */
function cookie_header_test() {
    return cookie_header_setup().then(cookie_header_check).then(cookie_header_process);
}

/**
 * Sends the setup request for the cookie header test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_header_setup() {
    return $.ajax({
        url: "/cookietest/header_setup/" + test_id + "/"
    });
}

/**
 * Sends the check request for the cookie header test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_header_check() {
    return $.ajax({
        url: "/cookietest/header_check/" + test_id + "/"
    });
}

/**
 * Processes the result of the cookie header check test.
 * This test only needs server-side checks, so this function only marks the test as completed.
 * @param result
 */
function cookie_header_process(result) {
    $("#cookie-header-result").html("<strong>Done</strong>");
}


// ----------------- Cookie test: httponly -----------------------------------------------------------------------

/**
 * Tests whether the cookie attribute "httponly" is implemented
 * Setup: request the setup URL. The response contains the Set-Cookie header with the attribute "httponly".
 * Check: request the check URL. The response body is "cookie_correct" if the cookie was sent with the request.
 * Process: Test is passed if the cookie is set by the response header, sent with the check request and not
 * accessible via Javascript.
 */
function cookie_httponly_test() {
    return cookie_httponly_setup().then(cookie_httponly_check).then(cookie_httponly_process);
}

/**
 * Sends the setup request for the cookie httponly test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_httponly_setup() {
    return $.ajax({
        url: "/cookietest/httponly_setup/" + test_id + "/"
    });
}

/**
 * Sends the check request for the cookie httponly test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_httponly_check() {
    return $.ajax({
        url: "/cookietest/httponly_check/" + test_id + "/"
    });
}

/**
 * Processes the result of the cookie httponly check test.
 * Checks whether the cookie can be accessed via javascript.
 * @param result
 */
function cookie_httponly_process(result) {
    save_result(test_id,
        "cookie_httponly_client_check",
        typeof Cookies.get('cookie_httponly_test') !== 'undefined'
            ? "cookie_accessed"
            : "cookie_not_accessed");
    $("#cookie-httponly-result").html("<strong>Done</strong>");
}


// ----------------- Cookie test: expires -----------------------------------------------------------------------

/**
 * Tests whether the cookie attribute "expires" is implemented
 * Setup: request the setup URL. The response contains the Set-Cookie header with the attribute "expires" set to a
 * past date.
 * Check: request the check URL. The response body is "cookie_correct" if the cookie was sent with the request.
 * Process: Test is passed if the cookie is set by the response header, but not sent with the check request.
 */
function cookie_expires_test() {
    return cookie_expires_setup().then(cookie_expires_check).then(cookie_expires_process);
}

/**
 * Sends the setup request for the cookie expires test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_expires_setup() {
    return $.ajax({
        url: "/cookietest/expires_setup/" + test_id + "/"
    });
}

/**
 * Sends the check request for the cookie expires test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_expires_check() {
    return $.ajax({
        url: "/cookietest/expires_check/" + test_id + "/"
    });
}

/**
 * Processes the result of the cookie expires check test.
 * This test only needs server-side validation, so this function only marks the test as complete
 * @param result
 */
function cookie_expires_process(result) {
    $("#cookie-expires-result").html("<strong>Done</strong>");

}


// ----------------- Cookie test: maxage -----------------------------------------------------------------------

/**
 * Tests whether the cookie attribute "maxage" is implemented
 * Setup: request the setup URL. The response contains the Set-Cookie header with 4 entries:
 *  1. a cookie with the attribute "max-age" set to 0.
 *  2. a cookie with the attribute "max-age" set to -1.
 *  3. a cookie with the attribute "max-age" set to 1 (the check function will let this expire before checking).
 *  4. a cookie with the attribute "max-age" set to 1000.
 * Check: request the check URL. The response body is "cookie_correct" if only the cookie with max-age=1000 was
 * sent with the request.
 * Process: Test is passed, if only the cookie with max-age=1000 is sent with the check request.
 */
function cookie_maxage_test() {
    return cookie_maxage_setup().then(cookie_maxage_check).then(cookie_maxage_process);
}

/**
 * Sends the setup request for the cookie maxage test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_maxage_setup() {
    return $.ajax({
        url: "/cookietest/maxage_setup/"+ test_id + "/"
    });
}


/**
 * Sends the check request for the cookie maxage test. Waits for 4 seconds before sending to let the 1 second max-age
 * cookie expire.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_maxage_check() {
    return new Promise((resolve) => setTimeout(resolve, 4000)).then(function(){
        return $.ajax({
            url: "/cookietest/maxage_check/"+ test_id + "/"
        });
    });

}

/**
 * Processes the result of the cookie maxage check test.
 * This test only needs server-side validation, so this function only marks the test as complete
 * @param result
 */
function cookie_maxage_process(result) {
    $("#cookie-maxage-result").html("<strong>Done</strong>");
}

// ----------------- Cookie test: subdomain -----------------------------------------------------------------------

/**
 * Tests whether the cookie behaviour for subdomains is implemented correctly.
 * Setup: request the setup URL from a subdomain. The response contains the Set-Cookie header set for a subdomain.
 * Check: request the check URL from the parent domain. The response body is "cookie_correct" if the cookie was not
 * sent with the request.
 * Process: Test is passed if the cookie is set by the response header and not sent with the check request.
 */
function cookie_subdomain_test() {
    return cookie_subdomain_setup().then(cookie_subdomain_check).then(cookie_subdomain_process);
}

/**
 * Sends the setup request for the cookie subdomain test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_subdomain_setup() {
    return $.get({
        url: subdomain_origin + "/cookietest/subdomain_setup/"+ test_id + "/"
    }).fail(function(){ console.log('subdomain setup error')});
}

/**
 * Sends the check request for the cookie subdomain test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_subdomain_check() {
    return $.ajax({
        url: "/cookietest/subdomain_check/"+ test_id + "/"
    });
}

/**
 * Processes the result of the cookie subdomain check test.
 * This test only needs server-side validation, so this function only marks the test as complete
 * @param result
 */
function cookie_subdomain_process(result) {
    $("#cookie-subdomain-result").html("<strong>Done</strong>");

}


// ----------------- Cookie test: path -----------------------------------------------------------------------

/**
 * Tests whether the cookie attribute "path" is implemented
 * Setup: request the setup URL. The response contains two cookies:
 * 1. A cookie with the path set to a path conflicting with the path of the check URL
 * 2. A cookie with the path set to a path exactly matching the path of the check URL
 * 3. A cookie with the path set to a path containing the beginning of the path of the check URL
 * Check: request the check URL. The response body is "cookie_correct" if the cookies 2 and 3 are sent, and cookie 1
 * is not sent with the request
 * Process: Test is passed if the cookie 1, 2 and 3 are set by the response header and cookie 1 is not sent with the
 * check request while cookies 2 and 3 are sent with the check request.
 */
function cookie_path_test() {
    return cookie_path_setup().then(cookie_path_check).then(cookie_path_process);
}

/**
 * Sends the setup request for the cookie path test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_path_setup() {
    return $.get({
        url: "/cookietest/path_setup/"+ test_id + "/"
    });
}

/**
 * Sends the check request for the cookie path test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_path_check() {
    return $.ajax({
        url: "/cookietest/path_check/"+ test_id + "/"
    });
}

/**
 * Processes the result of the cookie path check test.
 * @param result
 */
function cookie_path_process(result) {
    save_result(test_id, "cookie_path_invalid_client_check", Cookies.get('cookie_path_test_invalid') !== 'undefined' ? 'cookie_accessed' : 'cookie_not_accessed');
    save_result(test_id, "cookie_path_exact_client_check", Cookies.get('cookie_path_test_exact') !== 'undefined' ? 'cookie_accessed' : 'cookie_not_accessed');
    save_result(test_id, "cookie_path_fuzzy_client_check", Cookies.get('cookie_path_test_fuzzy') !== 'undefined' ? 'cookie_accessed' : 'cookie_not_accessed');
    $("#cookie-path-result").html("<strong>Done</strong>");

}

// ----------------- Cookie test: domain -----------------------------------------------------------------------

/**
 * Tests whether the cookie attribute "domain" is implemented
 * Setup: request the setup URL. The response contains three cookies:
 * 1. A cookie with the domain set to a domain conflicting with the domain of the check URL
 * 2. A cookie with the domain set to a domain exactly matching a subdomain of the check URL
 * 3. A cookie with the domain set to a domain matching the domain of the check URL
 * Process: Test is passed if the cookie 1, 2 and 3 are set by the response header and cookies 1 and 2 are not sent
 * with the check request while cookie 3 is sent with the check request.
 */
function cookie_domain_test() {
    return cookie_domain_setup().then(cookie_domain_check).then(cookie_domain_process);
}

/**
 * Sends the setup request for the cookie domain test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_domain_setup() {
    return $.get({
        url: subdomain_origin + "/cookietest/domain_setup/"+ test_id + "/"
    });
}

/**
 * Sends the check request for the cookie domain test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_domain_check() {
    return $.ajax({
        url: "/cookietest/domain_check/"+ test_id + "/"
    });
}

/**
 * Processes the result of the cookie domain check test.
 * @param result
 */
function cookie_domain_process(result) {
    save_result(test_id, "cookie_domain_invalid_client_check", Cookies.get('cookie_domain_test_invalid') !== 'undefined' ? 'cookie_accessed' : 'cookie_not_accessed');
    save_result(test_id, "cookie_domain_exact_client_check", Cookies.get('cookie_domain_test_exact') !== 'undefined' ? 'cookie_accessed' : 'cookie_not_accessed');
    save_result(test_id, "cookie_domain_fuzzy_client_check", Cookies.get('cookie_domain_test_fuzzy') !== 'undefined' ? 'cookie_accessed' : 'cookie_not_accessed');
    $("#cookie-domain-result").html("<strong>Done</strong>");
}


// ----------------- Cookie test: domainreverse -----------------------------------------------------------------------

/**
 * Tests whether the cookie attribute "domain" is implemented
 * Setup: request the setup URL. The response contains three cookies:
 * 1. A cookie with the domain set to a domain conflicting with the domain of the check URL
 * 2. A cookie with the domain set to a domain exactly matching a subdomain of the check URL
 * 3. A cookie with the domain set to a domain matching the domain of the check URL
 * Process: Test is passed if the cookie 1, 2 and 3 are set by the response header and cookies 1 and 2 are not sent
 * with the check request while cookie 3 is sent with the check request.
 */
function cookie_domainreverse_test() {
    return cookie_domainreverse_setup().then(cookie_domainreverse_check).then(cookie_domainreverse_process);
}

/**
 * Sends the setup request for the cookie domain test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_domainreverse_setup() {
    return $.get({
        url: current_origin + "/cookietest/domainreverse_setup/"+ test_id + "/"
    });
}

/**
 * Sends the check request for the cookie domain test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_domainreverse_check() {
    return $.ajax({
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        url: subdomain_origin + "/cookietest/domainreverse_check/"+ test_id + "/"
    });
}

/**
 * Processes the result of the cookie domain check test.
 * @param result
 */
function cookie_domainreverse_process(result) {
    save_result(test_id, "cookie_domainreverse_invalid_client_check", Cookies.get('cookie_domainreverse_test_invalid') !== 'undefined' ? 'cookie_accessed' : 'cookie_not_accessed');
    save_result(test_id, "cookie_domainreverse_exact_client_check", Cookies.get('cookie_domainreverse_test_exact') !== 'undefined' ? 'cookie_accessed' : 'cookie_not_accessed');
    save_result(test_id, "cookie_domainreverse_fuzzy_client_check", Cookies.get('cookie_domainreverse_test_fuzzy') !== 'undefined' ? 'cookie_accessed' : 'cookie_not_accessed');
    $("#cookie-domainreverse-result").html("<strong>Done</strong>");
}

// ----------------- Cookie test: secure -----------------------------------------------------------------------

/**
 * Tests whether the cookie attribute "domain" is implemented
 * Setup: request the setup URL. The response contains four cookies:
 * 1. A cookie with the domain set to a domain conflicting with the domain of the check URL
 * 2. A cookie with the domain set to a domain exactly matching a subdomain of the check URL
 * 3. A cookie with the domain set to a domain matching the domain of the check URL
 * Check: request the check URL. The response body is "cookie_correct" if cookie 3 is sent, and cookies 1 and 2
 * are not sent with the request
 * Process: Test is passed if the cookie 1, 2 and 3 are set by the response header and cookies 1 and 2 are not sent
 * with the check request while cookie 3 is sent with the check request.
 */
function cookie_secure_test() {
    return cookie_secure_setup()
        .then(cookie_secure_check)
        .then(cookie_securehttps_setup)
        .then(cookie_securehttps_check)
        .then(cookie_securehttps_process);
}

/**
 * Sends the setup request for the cookie secure test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_secure_setup() {
    return $.get({
        url: current_origin + "/cookietest/secure_setup/"+ test_id + "/"
    });
}

/**
 * Sends the check request for the cookie secure test over HTTP.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_secure_check() {
    return $.ajax({
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        url: current_origin + "/cookietest/secure_check/"+ test_id + "/"
    });
}

/**
 * Processes the result of the cookie domain check test.
 * @param result
 */
function cookie_secure_process(result) {
    save_result(test_id, "cookie_secure_client_check", Cookies.get('cookie_secure_test') !== 'undefined' ? 'cookie_accessed' : 'cookie_not_accessed');
    $("#cookie-secure-result").html("<strong>Done</strong>");
}

/**
 * Sends the setup request for the cookie secure HTTPS test.
 * @returns {*}
 */
function cookie_securehttps_setup() {
    return $.get({
        url: "/cookietest/securehttps_setup/"+ test_id + "/"
    });
}

/**
 * Sends the check request for the cookie secure test over HTTPS.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_securehttps_check() {
    return $.ajax({
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        url: current_secure_origin + "/cookietest/securehttps_check/"+ test_id + "/"
    });
}

/**
 * Processes the result of the cookie secure check test.
 * @param result
 */
function cookie_securehttps_process(result) {
    save_result(test_id, "cookie_securehttps_client_check", Cookies.get('cookie_securehttps_test') !== 'undefined' ? 'cookie_accessed' : 'cookie_not_accessed');
    $("#cookie-securehttps-result").html("<strong>Done</strong>");
    save_result(test_id, "cookie_secure_client_check", Cookies.get('cookie_secure_test') !== 'undefined' ? 'cookie_accessed' : 'cookie_not_accessed');
    $("#cookie-secure-result").html("<strong>Done</strong>");
}


/**
 * Tests whether the cookie attribute "sameSite" is implemented
 * Setup: request the setup URL. The response contains four cookies:
 * 1. A cookie with the sameSite attribite  set to "None" and the attribute "secure" unset
 * 2. A cookie with the sameSite attribite  set to "None" and the attribute "secure" set to True
 * 2. A cookie with the sameSite attribite  set to "Lax"
 * 2. A cookie with the sameSite attribite  set to "Strict"
 * Check: request the check URL.
 */
function cookie_samesite_test() {
    return cookie_samesite_setup()
        .then(cookie_samesite_none_check)
        .then(cookie_samesite_none_secure_check)
        .then(cookie_samesite_lax_check)
        .then(cookie_samesite_strict_check)
        .then(cookie_samesite_none_external_check)
        .then(cookie_samesite_none_secure_external_check)
        .then(cookie_samesite_lax_external_check)
        .then(cookie_samesite_strict_external_check)
        .then(cookie_samesite_img_check);
}

/**
 * Sends the setup request for the cookie secure test.
 * @returns {*|{getAllResponseHeaders, abort, setRequestHeader, readyState, getResponseHeader, overrideMimeType, statusCode}}
 */
function cookie_samesite_setup() {
    return $.get({
        url: current_origin + "/cookietest/samesite_setup/"+ test_id + "/"
    });
}

function cookie_samesite_none_check() {
    return $.ajax({
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        url: current_origin + "/cookietest/samesite_check/"+ test_id + "/none/"
    });
}

function cookie_samesite_none_secure_check() {
    return $.ajax({
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        url: current_secure_origin + "/cookietest/samesite_check/"+ test_id + "/none_secure/"
    });
}

function cookie_samesite_lax_check() {
    return $.ajax({
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        url: current_origin + "/cookietest/samesite_check/"+ test_id + "/lax/"
    });
}

function cookie_samesite_strict_check() {
    return $.ajax({
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        url: current_origin + "/cookietest/samesite_check/"+ test_id + "/strict/"
    });
}
function cookie_samesite_none_external_check() {
    return $.ajax({
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        url: external_origin + "/cookietest/samesite_check/"+ test_id + "/none_external/"
    });
}

function cookie_samesite_none_secure_external_check() {
    return $.ajax({
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        url: external_secure_origin + "/cookietest/samesite_check/"+ test_id + "/none_secure_external/"
    });
}

function cookie_samesite_lax_external_check() {
    return $.ajax({
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        url: external_origin + "/cookietest/samesite_check/"+ test_id + "/lax_external/"
    });
}

function cookie_samesite_strict_external_check() {
    return $.ajax({
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        url: external_origin + "/cookietest/samesite_check/"+ test_id + "/strict_external/"
    });
}

function cookie_samesite_img_check() {
    console.log("appending images");
    $("#cookie-samesite-result").append($('<img>',{src:current_origin + '/cookietest/samesite_check/' + test_id + '/none_img/'}));
    $("#cookie-samesite-result").append($('<img>',{src:current_secure_origin + '/cookietest/samesite_check/' + test_id + '/none_secure_img/'}));
    $("#cookie-samesite-result").append($('<img>',{src:current_origin + '/cookietest/samesite_check/' + test_id + '/lax_img/'}));
    $("#cookie-samesite-result").append($('<img>',{src:current_origin + '/cookietest/samesite_check/' + test_id + '/strict_img/'}));
    $("#cookie-samesite-result").append($('<img>',{src:external_origin + '/cookietest/samesite_check/' + test_id + '/none_img_external/'}));
    $("#cookie-samesite-result").append($('<img>',{src:external_secure_origin + '/cookietest/samesite_check/' + test_id + '/none_secure_img_external/'}));
    $("#cookie-samesite-result").append($('<img>',{src:external_origin + '/cookietest/samesite_check/' + test_id + '/lax_img_external/'}));
    $("#cookie-samesite-result").append($('<img>',{src:external_origin + '/cookietest/samesite_check/' + test_id + '/strict_img_external/'}));
    $("#cookie-samesite-result").append('<strong>Done</strong>');

}


/**
 * Processes the result of the cookie samesite check test.
 * @param result
 */
function cookie_secure_process(result) {
    //$("#cookie-samesite-result").html("<strong>Done</strong>");
}


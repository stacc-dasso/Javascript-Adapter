var username = 'testuser';
var password = '41366860726384';
var api_url = "http://104.248.248.147"+":5678/api/v2/";
var stacc_id = "1234567";
var website = "local.magento";

var unsent_requests = []
var recs = {}

/**
 * Method for sending search event to API
 * @param {String} query
 * @param {Array} filters 
 * @param {Object} properties 
 */
function send_search_request(query,filters=[],properties={}) {
    var request_params = {
        'query': query,
        'filters': filters,
        'properties': properties,
        'stacc_id': stacc_id,
        'website': website,
    };
    send_api_request(request_params, 'send_search');
}

/**
 * Method for sending viewed item to API
 * @param {String} item_id 
 * @param {Object} properties 
 */
function send_view_request(item_id,properties={}) {
    var request_params = {
        'item_id': item_id,
        'properties': properties,
        'stacc_id': stacc_id,
        'website': website,
    };
    send_api_request(request_params, 'send_view');
}

/**
 * Method for sending add to cart events
 * @param {String} item_id 
 * @param {Object} properties 
 */
function send_addtocart_request(item_id, properties={}) {
    var request_params = {
        'item_id': item_id,
        'properties': properties,
        'stacc_id': stacc_id,
        'website': website,
    };
    send_api_request(request_params, 'send_add_to_cart');
}

/**
 * Method for sending checkout events
 * @param {String} item_id 
 * @param {Object} properties 
 */
function send_checkout_request(itemList=[], properties={}) {
    var request_params = {
        'item_list': itemList,
        'properties': properties,
        'stacc_id': stacc_id,
        'website': website,
        'currency':'EUR',
    };
    send_api_request(request_params, 'send_purchase');
}

/**
 * 
 * @param {Object} request_params 
 * @param {String} endpoint 
 */
function send_api_request(request_params,endpoint) {
    var request = new XMLHttpRequest();
    request.open('POST', api_url+endpoint, true);
    request.setRequestHeader("Authorization", "Basic " + btoa(username+":"+password));

    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status == 200) {
            if (endpoint === 'get_recs') {
                recs = JSON.parse(request.response);
            };

            reqs = JSON.parse(localStorage.getItem('unsent_requests'));
            
            if (reqs.length > 0) {
                var errorRequest = new XMLHttpRequest();
                errorRequest.open('POST', api_url+'send_error_log', true)
                errorRequest.setRequestHeader("Authorization", "Basic " + btoa(username+":"+password));
                params = {
                    'stacc_id':stacc_id,
                    'website':website,
                    'log_message':"There was a problem with sending recorded events."
                }
                errorRequest.send(JSON.stringify(params));
                
                for (var i = 0; i < reqs.length; i++) {
                    var obj = reqs[i];
                    var req = new XMLHttpRequest();
                    req.open('POST', api_url+obj.endpoint, true);
                    req.setRequestHeader("Authorization", "Basic " + btoa(username+":"+password));
                    req.send(obj.params);
                }
                var a = []
                localStorage.setItem('unsent_requests',JSON.stringify(a));
            }
        } else if (request.readyState === 4) {
            var a = []
            a = JSON.parse(localStorage.getItem('unsent_requests'));
            
            a.push({'params':request_params,
                    'endpoint':endpoint});

            localStorage.setItem('unsent_requests',JSON.stringify(a));
        }
    }
    request.send(JSON.stringify(request_params));
}

/**
 * Method for getting recommendations
 * @param {String} item_id 
 * @param {Object} properties 
 */
function get_recommendations(item_id, properties={}) {
    var request_params = {
        'item_id': item_id,
        'properties': properties,
        'stacc_id': stacc_id,
        'website': website,
        'block_id':1
    };
    send_api_request(request_params, 'get_recs');
}

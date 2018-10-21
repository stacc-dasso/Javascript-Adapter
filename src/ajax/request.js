var username = 'testuser';
var password = '41366860726384';
var api_url = 'http://104.248.248.147:5678/api/v2/';
var stacc_id = "1234567";
var website = "local.magento";

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
 * 
 * @param {Object} request_params 
 * @param {String} endpoint 
 */
function send_api_request(request_params,endpoint) {
    var request = new XMLHttpRequest();
    request.open('POST', api_url+endpoint, true);
    request.setRequestHeader("Authorization", "Basic " + btoa(username+":"+password));

    request.onload = function () {
        console.log(this.response);
    }

    request.send(JSON.stringify(request_params));
}

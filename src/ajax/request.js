var username = 'testuser';
var password = '41366860726384';
var api_url = document.location.origin+":5678/api/v2/";
var stacc_id = "1234567";
var website = "local.magento";

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

    request.onload = function () {
        if (endpoint === 'get_recs') {
            recs = JSON.parse(this.response);
        };
        return this.response;
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

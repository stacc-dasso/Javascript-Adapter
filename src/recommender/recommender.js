var box_node;

function recommender_box(item_id) {
    get_recommendations(item_id);
    setTimeout(function() {
        buildBox();
    },2000);
}

function buildBox() {
	
    var div_element = document.createElement("DIV");
    div_element.setAttribute("class","recommender_box");
    div_element.setAttribute("id","recommender_box_1");
	
	// If there was a problem with getting recommended products or they don't exist then return function without creating box
	if (Object.keys(recs).length == 0) {
		box_node = div_element;
		return;
	}

    var box_title = document.createElement("h2");
    box_title.appendChild(document.createTextNode("Recommended products"));
    box_title.setAttribute("class","recommender_box_title");
    div_element.appendChild(box_title);

    var products_div = document.createElement("div");
    products_div.setAttribute("class","products_box products-grid");

    for (var key in recs["items"]) {
        var id = key;
        var name = recs["items"][key][0];
        var img = recs["items"][key][1];
        var price = recs["items"][key][2];
        var url = recs["items"][key][3];

        var product_element  = document.createElement("DIV");
        product_element.setAttribute("class","recommended_product");

        var img_element = document.createElement("a");
        var img_content = document.createElement("IMG");
        img_content.setAttribute("src",img);
        img_element.appendChild(img_content);
        img_element.setAttribute("href",url);

        var link_element = document.createElement("a");
        var title_element = document.createElement("h3");
        title_element.appendChild(document.createTextNode(name));
        title_element.setAttribute("class","recommended_product_text product-name");
        link_element.appendChild(title_element);
        link_element.setAttribute("href",url);

        var price_node = document.createElement("div");
        price_node.setAttribute("class","price-box");
        var price_element = document.createElement("p");
        price_element.appendChild(document.createTextNode(price));
        price_element.setAttribute("class","recommended_product_text price");
        price_node.appendChild(price_element);

        product_element.appendChild(img_element);
        product_element.appendChild(link_element);
        product_element.appendChild(price_node);
        products_div.appendChild(product_element);
    }
    div_element.appendChild(products_div);
    box_node = div_element;
}
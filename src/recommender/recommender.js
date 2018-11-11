console.log(recommender_box("421"));
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

    for (var key in recs["items"]) {
        var id = key;
        var name = recs["items"][key][0];
        var url = recs["items"][key][1];

        var product_element  = document.createElement("DIV");
        product_element.setAttribute("class","recommended_product");

        var img_element = document.createElement("IMG");
        img_element.setAttribute("src",url);

        var title_element = document.createTextNode(name);

        product_element.appendChild(img_element);
        product_element.appendChild(title_element);
        div_element.appendChild(product_element);
    }
    return div_element;
}
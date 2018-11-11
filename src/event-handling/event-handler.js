window.onload = function(){

	var searchbox = document.getElementById("search_mini_form");
	if (searchbox) {
		searchbox.addEventListener('submit',function(e) {
			var query = e.target[0].value;
			send_search_request(query);
		});
	}

	// Sending view event right after clicking


	/* 
	var itemsArray = document.getElementsByClassName("item");
	if (itemsArray) {
		for (var i = 0; i < itemsArray.length; i++) {
			itemsArray[i].addEventListener('click', function(e) {
				var item_id = e.target.closest(".item").querySelector("a").href.split("-").pop().replace(".html","");
				send_view_request(item_id);
			});
		};
	}
	*/

	var addToCartForm = document.getElementById('product_addtocart_form');
	if (addToCartForm) {
		var id = addToCartForm.getElementsByClassName("no-display")[0].firstElementChild.value;
		send_view_request(id);

		addToCartForm.getElementsByClassName("btn-cart")[0].addEventListener('click',function() {
			send_addtocart_request(id);
		});

		var product_view = addToCartForm.parentElement.parentElement;
		var rec_node = recommender_box(id);
		product_view.parentElement.insertBefore(rec_node, product_view.nextElementSibling);
	}
};




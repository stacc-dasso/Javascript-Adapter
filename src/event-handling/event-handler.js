window.onload = function(){

	var searchbox = document.getElementById("search_mini_form");
	if (searchbox) {
		searchbox.addEventListener('submit',function(e) {
			var query = e.target[0].value;
			send_search_request(query);
		});
	}

	var addToCartForm = document.getElementById('product_addtocart_form');
	if (addToCartForm) {
		var id = addToCartForm.getElementsByClassName("no-display")[0].firstElementChild.value;
		send_view_request(id);

		addToCartForm.getElementsByClassName("btn-cart")[0].addEventListener('click',function() {
			send_addtocart_request(id);
		});

		var product_view = addToCartForm.parentElement.parentElement;
		var rec_node = recommender_box(id);
		setTimeout(function() {
			product_view.parentElement.insertBefore(box_node, product_view.nextElementSibling);
		}, 2000);
	}

	var main_page_new_products = document.getElementsByClassName("widget-new-products")[0];
	if (main_page_new_products) {
		var rec_node = recommender_box("1");
		setTimeout(function() {
			console.log(box_node);
			main_page_new_products.parentElement.insertBefore(box_node, main_page_new_products.nextElementSibling);
		}, 2000);
	}

	var checkout_button = document.getElementsByClassName("btn-checkout")[0];
	if (checkout_button) {
		checkout_button.addEventListener("click", function(e) {
			send_checkout_request();
			e.preventDefault();
		});
	}

};




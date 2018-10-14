window.onload = function(){

	var searchbox = document.getElementById("search_mini_form");
	if (searchbox) {
		searchbox.addEventListener('submit',function(e) {
			var query = e.target[0].value;
			send_search_request(query);
		});
	}

	var itemsArray = document.getElementsByClassName("item");
	if (itemsArray) {
		for (var i = 0; i < itemsArray.length; i++) {
			itemsArray[i].addEventListener('click', function(e) {
				var item_id = e.target.closest(".item").querySelector("a").href.split("-").pop().replace(".html","");
				send_view_request(item_id);
			});
		};
	}
	
	var addToCartForm = document.getElementById('product_addtocart_form');
	if (addToCartForm) {
		addToCartForm.addEventListener('submit',function(e) {
			e.preventDefault();
			console.log(e);
		});
	}

};




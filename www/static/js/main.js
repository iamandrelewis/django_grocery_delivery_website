import InstantSearch from "./InstantSearch.js";
import ShoppingCart from "./ShoppingCart.js";

const searchBar = document.querySelector('.searchbar-container');
const updateCart = document.querySelectorAll('.update-cart')
const cartInstance = new ShoppingCart(updateCart,{
    searchURL: new URL('api',window.location.origin),
});
const searchInstance = new InstantSearch(searchBar,{
    
    searchURL: new URL('api',window.location.origin),
    isCategoryPage : true,
    categoryQuery: document.querySelector('.searchbar-container input').id,
    responseParser: (responseData) => {
        return Object.values(responseData.data)
    },
    templateFunction: (result) => {
        return `<div class="product_card-container" style="position: relative;">
        <a href="../../shop/products/${result.product.product.id}" style="display: block; width: 100%; height: 100%; position: absolute;"></a>
        <div class="product-img">
            <span></span>
            <div class="product-add">
                <button data-product="${result.product.id}" data-action="add" class="product_add-btn update-cart">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="#FFFFFF" xmlns="http://www.w3.org/2000/svg" size="24" color="systemGrayscale00"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3.5A1.5 1.5 0 0 1 13.5 5v5.5H19a1.5 1.5 0 0 1 1.493 1.355L20.5 12a1.5 1.5 0 0 1-1.5 1.5h-5.5V19a1.5 1.5 0 0 1-1.355 1.493L12 20.5a1.5 1.5 0 0 1-1.5-1.5v-5.5H5a1.5 1.5 0 0 1-1.493-1.355L3.5 12A1.5 1.5 0 0 1 5 10.5h5.5V5a1.5 1.5 0 0 1 1.355-1.493L12 3.5Z"></path>
                    </svg>
                </button>            
            </div>
        </div>
        <div class="product-details">
            <div class="product-title">
                <div class="product_price-container">
                    <div class="product-price">
                        <p class="dollars" id="product_price-dollars">${result.price.currency == 'JMD'? 'J' : result.price.currency == 'USD' ? '':''}$${result.price.value}</p>
                    </div>
                </div>  
                <p class="product_variety">${result.product.name}</p>
                <p class="product_name">${result.product.product.name}</p>
                <p class="product_unit">per ${result.unit.unit} (${result.unit.unitAbbr}.)</p> 
            </div>
        </div>
    </div>`
    },
});



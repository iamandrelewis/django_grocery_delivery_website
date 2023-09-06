import InstantSearch from "./InstantSearch.js";
import ShoppingCart from "./ShoppingCart.js";

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

/*const searchBar = document.querySelector('.searchbar-container');
const updateCart = document.querySelectorAll('.update-cart')
const cartInstance = new ShoppingCart(updateCart,{
    searchURL: new URL('api',window.location.origin),
    templateFunction:(result) => {
        return `
        <div class="cart_item-container" id="${result.order.id}">
            <div class="item-details" id="cart_details" style="position: relative;">
                <a href="{% url 'product-details'%}" style=" display: block; position: absolute; width: 100%; height: 100%;"></a>
                <p class="item-title" id="cart_product-title">{{item.product_grade.product.product.name}}</p>
                <p class="item-unit" id="cart_product-unit">per {{item.product_grade.unit.unit}} ({{item.product_grade.unit.unit_abbr}}.)</p>
                <div class="item-others">
                    <p class="item-variety" id="cart_product-variety">{{item.product_grade.product.name}}</p>
                    <p class="item-grade" id="cart_product-grade">Grade {{item.product_grade.grade}}</p>
                </div>
            </div>
            <div class="item_price-container" style="width: fit-content; display: flex; align-items: center;" >
                <input type="number" name="{{item.product_grade.id}}" id="id_product_qty{{forloop.counter0}}" data-id="{{forloop.counter0}}" data-item_id="{{item.id}}" value="{{item.quantity}}" class="cart-input" style="width: 25px; height: 30px;">
                <span style="font-weight: 600; font-size: 12.5px; margin-right: 8px;">{{item.product_grade.unit.unit_abbr}}</span>
            </div>
            <div class="item_price-container">
                <p class="currency">J$</p>
                <input type="number" name="{{item.product_grade.id}}" id="id_product_price{{forloop.counter0}}" data-id="{{forloop.counter0}}" data-item_id="{{item.id}}" value="{{item.subtotal|floatformat:2}}" class="cart-input">
            </div>
            <div class="item_actions">
                <button id="id_more_options{{item.id}}" class="more_options-btn">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="# 343538" xmlns="http://www.w3.org/2000/svg" size="20" color="systemGrayscale70" class="css-1qx34im"><path fill-rule="evenodd" clip-rule="evenodd" d="M3 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm9 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm12-3a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"></path></svg>
                </button>
                <div id="id_more_options{{item.id}}-menu" class="more_options-menu hidden">
                <ul>

                    <li class="add_note-option" data-product="{{item.product_grade.id}}">
                        <span>Add instructions</span>
                    </li>
                    <li style="position: relative;">
                        <a href="{% url 'product-details'%}" style="display: block; position: absolute; width: 100%; height: 100%;"></a>
                        <span>Edit product</span>
                    </li>
                    <li class="rmv_item-option" data-product="{{item.product_grade.id}}" data-action="remove">
                        <span>Remove</span>
                    </li>
                </ul>
                </div>
            </div>
        </div>
        `
    }
});
const searchInstance = new InstantSearch(searchBar,{
    
    searchURL: new URL('api',window.location.origin),
    isCategoryPage : false,
    responseParser: (responseData) => {
        return Object.values(responseData.data)
    },
    templateFunction: (result) => {
        return `<div class="product_card-container" style="position: relative;">
        <a href="../../shop/products/${result.product.product.id}" style="display: block; width: 100%; height: 100%; position: absolute;"></a>
        <div class="product-img">
            <span></span>
            <div class="product-add">
                <button data-product="${result.id}" data-action="add" class="product_add-btn update-cart">
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
});*/

const getCartCount = () => {
        const url  = new URL(new URL('shop/update-cart',window.location.origin).toString());    
        return fetch(url,{
        method:'POST',
        headers:{
            "Content-Type":"application/json",
            "X-CSRFToken": csrftoken,
        },
        credentials:"include",
        mode:"same-origin",
        body: JSON.stringify({
            'productID':'',
            'action':'getCartCount'
        })
    }).then(response =>{
        return response.json()
    }).then(responseData => {
        console.log(responseData)
        return responseData
    }).finally(results =>{
        return results
    })
}
const itemTotal = getCartCount().then(result => document.querySelectorAll('#cartNumber').forEach(element => {
    if(result > 0) {
        element.innerHTML = result
    }
    else{
        element.parentNode.parentElement.style.display = 'none';
    }
})) 



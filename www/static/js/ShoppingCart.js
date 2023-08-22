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

/**
 * @typedef {Object} ShoppingCartOptions
 * @property {URL} searchURL
 * 
 */
class ShoppingCart {
    /**
     * @param {HTMLElement} item 
     * @param {ShoppingCartOptions} options 
     */
    constructor(item,options){
        this.options = options
        this.elements = {
            main: item,
            cart_items_input : document.querySelectorAll('.cart_item-container input'),
            cart_item : document.querySelector('.cart_item-container')
        }
        this.addListeners()
    }
    

    addListeners(){
        this.elements.main.forEach(element=>{
            element.addEventListener('click',() => {
                let productID = element.dataset.product
                let action = element.dataset.action
                this.performUpdate(productID,action).then(results => console.log(results))
                window.location.reload()
            })
        });
        this.elements.cart_items_input.forEach(element => {
            element.addEventListener('input', (e) => {
                const productInfo = this.getProduct(element.name)

                if (element.id == `id_product_price${element.dataset.id}`){
                    setTimeout(() => e.target.value = parseFloat(e.target.value).toFixed(2),1000)
                    
                    productInfo.then(results => {
                        document.querySelector(`.cart_item-container input#id_product_qty${element.dataset.id}`).value = e.target.value/results[0].productGrade.price.value
                    })

                }
                else if(element.id == `id_product_qty${element.dataset.id}`){
                    productInfo.then(results => {
                        document.querySelector(`.cart_item-container input#id_product_price${element.dataset.id}`).value = parseFloat(e.target.value * results[0].productGrade.price.value).toFixed(2)                     })

                 }
            });
        })
    }
    getProduct(ID){
        const url  = new URL(this.options.searchURL.toString());        
        const Query = `query {
            orderProductById(product:"${ID}",order:"${this.elements.cart_item.id}"){
                id
                quantity
                productGrade {
                    product {
                      name
                      product{
                        name
                      }
                    }
                    price{
                      value
                      currency
                    }
                  }
                }
            }`;
        console.log(Query)
        return fetch(url,{
            method:'POST',
            headers:{
                "Content-Type":"application/json",
                "X-CSRFToken":csrftoken,
            },
            credentials:"include",
            mode:"same-origin",
            body: JSON.stringify({
                query:Query,
                variables:{},
            })
        }).then(response => {
            return response.json()
        }).then( responseData => {
            return Object.values(responseData.data)
        }).finally(results => {
            return results
        })
    }
    performUpdate(ID,Action){
        const url  = new URL(new URL('shop/update-cart',window.location.origin).toString());
        return fetch(url,{
            method:'POST',
            headers:{
                "Content-Type":"application/json",
                "X-CSRFToken":csrftoken,
            },
            credentials:"include",
            mode:"same-origin",
            body: JSON.stringify({
                'productID':ID,
                'action':Action
            })
        }).then(response => {
            return response.json()
        }).then( responseData => {
            return responseData
        }).finally(results => {
            return results
        })
    }
}
export default ShoppingCart;
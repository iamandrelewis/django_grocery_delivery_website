import ShoppingCart from "./ShoppingCart.js";
import getCookie from "./csrftoken.js";

const csrftoken = getCookie('csrftoken');

/**
 * @typedef {Object} InstantSearchOptions
 * @property {URL} searchURL
 * @property {String} queryParam
 * @property {Function} responseParser 
 * @property {Function} templateFunction
 * @property {Boolean} isCategoryPage
 * @property {String} categoryQuery
 */ 

class InstantSearch{
    /**
     * @param {HTMLElement} searchbar
     * @param {InstantSearchOptions} options
     */
    constructor(searchbar,options){
        this.options = options;
        this.elements = {
            main: searchbar,
            input: document.querySelector('.searchbar-container input'),
            resultsContainer: document.querySelector('#frm-product_wall')
        }
        this.addListeners()
    }
    addListeners(){
        let delay;
        this.elements.input.addEventListener('input', () =>{
            clearTimeout(delay);

            const query = this.elements.input.value;
            delay = setTimeout(()=>{
                this.performSearch(query).then(results =>
                {
                    this.renderResults(results)
                })
            },500)
            
        })
    }
    renderResults(results){

      while(this.elements.resultsContainer.firstChild){
        this.elements.resultsContainer.removeChild(this.elements.resultsContainer.firstChild)
      }
      results.forEach(element => {
        
        element.forEach(element=>{
                  this.elements.resultsContainer.innerHTML += this.options.templateFunction(element)
        })
      })
      const cartInstance = new ShoppingCart(document.querySelectorAll('.update-cart'),{
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
    }
    performSearch(query){
        const url  = new URL(this.options.searchURL.toString())
        const categoryQuery = this.options.isCategoryPage ? `category:"${this.elements.input.id}"`:''
        const Query = `
        query { 
            allProductGrades(search:"${query}",${categoryQuery}){
            id
            product{
              id
              name
              product{
                id
                name
                subcategory{
                  category{
                    name
                  }
                  name
                }
              }
            }
              grade
              price{
              value
              currency
            }
              unit{
              unit
              unitAbbr
            }
        }
        }`
        return fetch(url,{
            method:'POST',
            headers:{
                "Content-Type":"application/json",
                "X-CSRFToken":csrftoken,
            },
            mode:"same-origin",
            body: JSON.stringify({
                query:Query,
                variables:{},
            })
        }).then(response => {

            if (response.status !== 200){
                throw new Error('something went wrong with the search')
            }

            return response.json()

        }).then(responseData => {

            return this.options.responseParser(responseData)
        }).catch(error => {
            console.error(error)

            return [];

        }).finally(results =>{

            return results;
        })
    }
}
export default InstantSearch;
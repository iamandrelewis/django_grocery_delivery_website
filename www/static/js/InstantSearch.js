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
      });
    }
    performSearch(query){
        const url  = new URL(this.options.searchURL.toString())
        const categoryQuery = this.options.isCategoryPage ? `category:"${this.elements.input.id}"`:''
        const Query = `
        query { 
            allProductGrades(search:"${query}",${categoryQuery}){
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
import getCookie from "./csrftoken.js";
import ShoppingCart from "./ShoppingCart.js";
import ReplacementCart from "./ReplacementCart.js";
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

class itemSearch{
    /**
     * 
     * @param {HTMLElement} searchbar 
     * @param {InstantSearchOptions} options 
     */
    constructor(searchbar,options){
        this.elements ={
            main:searchbar,
            input: document.querySelector('.search_bar input'),
            resultsContainer: document.querySelector('.results-container'),
        }
        this.options = options
        this.addListeners()
    }
    addListeners(){
        this.performSearch('','').then(results =>
            {
                this.renderResults(results)
            })
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
    performSearch(query,category){
        const url  = new URL(this.options.searchURL.toString())
        //console.log(document.querySelector('.category_selector-btn.is_active').dataset.product_category)
        const categoryQuery = document.querySelector('.category_selector-btn.is_active').dataset.product_category
        const Query = `
        query { 
            allProductGrades(search:"${query}",category:"${categoryQuery}"){
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
    renderResults(results){
        
      while(this.elements.resultsContainer.firstChild){
        this.elements.resultsContainer.removeChild(this.elements.resultsContainer.firstChild)
      }
      results.forEach(element => {
        
        element.forEach(element=>{
                  this.elements.resultsContainer.innerHTML += this.options.templateFunction(element)
        })
      })
      const replacement = new ReplacementCart(document.querySelectorAll('.product_add-btn.update-replace'),{
        searchURL :  new URL('api',window.location.origin),
    });
    }
}
export default itemSearch;
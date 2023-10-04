import ShoppingCart from "./ShoppingCart.js";
import getCookie from "./csrftoken.js";
import { getCartCount } from "./cart.js";
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
class GeneralSearch{
    /**
     * @param {HTMLElement} searchbar
     * @param {InstantSearchOptions} options
     */
    constructor(searchbar,options){
        this.options = options;
        this.elements = {
            main: searchbar,
            input: document.querySelector('.search_container-home input'),
            resultsContainer: document.querySelector(' .search_container-home .resultsContainer'),
            backdrop: document.querySelector('.backdrop_search'),
            body: document.querySelector('body'),
            categorySelectorButton: document.querySelectorAll('.category_selector-btn'),
        }
        this.addListeners()
    }
    addListeners(){
        let delay;
        let menu = document.querySelector('.account_auth_menu-container')
        let cartCount = 0;
        const itemTotal = getCartCount().then(result => cartCount =result) 
        let cart_indicator = document.querySelector('.cart_active-indicator')

        this.elements.input.addEventListener('click',() => {
            console.log(cartCount)
            menu.style.display = 'none';
            if(cartCount > 0) cart_indicator.style.display = 'flex';
            this.elements.main.style.zIndex = "202";
            this.elements.body.classList.add('fixed')
            this.elements.backdrop.classList.remove('hidden')
            this.elements.resultsContainer.classList.remove('hidden')
        })
        this.elements.input.addEventListener('input', () =>{
            clearTimeout(delay);
            /*this.elements.main.innerHTML += 
            `<svg width="14px" height="14px" viewBox="0 0 24 24" fill="var(--black)" xmlns="http://www.w3.org/2000/svg" size="24" style=" margin-left:6px; display:flex; align-items: center; position:absolute; right:0px; z-index:202; ">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.06 4.94a1.5 1.5 0 0 1 0 2.12L14.122 12l4.94 4.94a1.5 1.5 0 0 1 .103 2.007l-.103.114a1.5 1.5 0 0 1-2.122 0L12 14.12l-4.94 4.94a1.5 1.5 0 0 1-2.12-2.122L9.878 12l-4.94-4.94a1.5 1.5 0 0 1-.103-2.007l.103-.114a1.5 1.5 0 0 1 2.122 0L12 9.88l4.94-4.94a1.5 1.5 0 0 1 2.12 0Z"></path>
            </svg>
            `*/
            const query = this.elements.input.value;
            delay = setTimeout(()=>{
                this.performSearch(query).then(results =>
                {
                    this.renderResults(results)
                })
            },500)

            
        })
        document.addEventListener('keydown',(e)=>{
            console.log(e)
            if(e.key==='Escape'){
                this.elements.input.value='';
                this.elements.body.classList.remove('fixed')
                this.elements.backdrop.classList.add('hidden');
                this.elements.main.style.zIndex="100";  
                this.elements.resultsContainer.classList.add('hidden')
            }
        })
        this.elements.backdrop.addEventListener('click',()=>{
            this.elements.input.value='';
                this.elements.body.classList.remove('fixed')
                this.elements.backdrop.classList.add('hidden')
                this.elements.resultsContainer.classList.add('hidden')
                this.elements.main.style.zIndex="100";  
        })
        this.elements.categorySelectorButton.forEach(element => {
            console.log(element)
            element.addEventListener('click',(e)=>{
                console.log(` clicked => ${e}`)
                document.querySelector('.category_selector-btn.is_active').classList.remove('is_active')
                if(e.target.classList.contains('category_selector-btn')){
                    e.target.classList.toggle('is_active')
                }
                else{
                    e.target.parentElement.classList.add('is_active')
                }
                this.performSearch('').then(results =>
                {
                    this.renderResults(results)
                })
                this.addListeners()
            })
        })
    }
    renderResults(results){
      const activeCategory = document.querySelector(".category_selector-btn.is_active").dataset.product_category;
      while(this.elements.resultsContainer.firstChild){
        this.elements.resultsContainer.removeChild(this.elements.resultsContainer.firstChild)
      }
      this.elements.resultsContainer.innerHTML +=`
      <div class="productCategory-wrapper" style="border-bottom: 1px solid  rgb(232, 233, 235); border-top: 1px solid  rgb(232, 233, 235); padding:  12px 32px 12px 32px; position: relative; overflow: hidden; overflow-x: auto; display: flex; align-items: center; width: 100%; ">
      <div class="productCategory-container" style="display: flex;  overflow-x: hidden; flex-wrap: nowrap; width: 90%; ">
          <div class="category_selector-btn ${activeCategory == "" ? "is_active":""}" data-product_category=""  style="border-radius: 14px; border: 1px solid rgb(232, 233, 235); width: max-content;  padding: 8px 14px; height: 20px; position: relative; display: flex; align-items: center; justify-content: center; margin-right: 12px; ">
              <div style="font-size: 14px; font-weight: 600; text-align: center; display: flex; align-items: center; width: max-content;"> 
                  All
              </div>
          </div>
          <div class="category_selector-btn ${activeCategory == "Green Produce" ? "is_active":""}" data-product_category="Green Produce"  style="border-radius: 14px; border: 1px solid rgb(232, 233, 235); width: max-content;  padding: 8px 14px; height: 20px; position: relative; display: flex; align-items: center; justify-content: center; margin-right: 12px; ">
              <div style="font-size: 14px; font-weight: 600; text-align: center; display: flex; align-items: center; width: max-content;"> 
                  Green Produce
              </div>
          </div>
          <div class="category_selector-btn ${activeCategory == "Vegetables" ? "is_active":""}" data-product_category="Vegetables"  style="border-radius: 14px; border: 1px solid rgb(232, 233, 235); width: max-content;  padding: 8px 14px; height: 20px; position: relative; display: flex; align-items: center; justify-content: center; margin-right: 12px; ">
              <div style="font-size: 14px; font-weight: 600; text-align: center; display: flex; align-items: center; width: max-content;"> 
                  Vegetables
              </div>
          </div>
          <div class="category_selector-btn ${activeCategory =="Fruits" ? "is_active":""}" data-product_category="Fruits"  style="border-radius: 14px; border: 1px solid rgb(232, 233, 235); width: max-content;  padding: 8px 14px; height: 20px; position: relative; display: flex; align-items: center; justify-content: center; margin-right: 12px; ">
              <div style="font-size: 14px; font-weight: 600; text-align: center; display: flex; align-items: center; width: max-content;"> 
                  Fruits
              </div>
          </div>
          <div class="category_selector-btn ${activeCategory == "Herbs & Spices" ? "is_active":""}" data-product_category="Herbs & Spices"  style="border-radius: 14px; border: 1px solid rgb(232, 233, 235); width: max-content;  padding: 8px 14px; height: 20px; position: relative; display: flex; align-items: center; justify-content: center; margin-right: 12px; ">
              <div style="font-size: 14px; font-weight: 600; text-align: center; display: flex; align-items: center; width: max-content;"> 
                 Herbs & Spices
              </div>
          </div>
          <div class="category_selector-btn ${activeCategory == "Tubers & Provisions" ? "is_active":""}" data-product_category="Tubers & Provisions"  style="border-radius: 14px; border: 1px solid rgb(232, 233, 235); width: max-content;  padding: 8px 14px; height: 20px; position: relative; display: flex; align-items: center; justify-content: center; margin-right: 12px; ">
              <div style="font-size: 14px; font-weight: 600; text-align: center; display: flex; align-items: center; width: max-content;"> 
                 Tubers & Provisions
              </div>
          </div>
          <div class="category_selector-btn ${activeCategory == "Nuts & Grains" ? "is_active":""}" data-product_category="Nuts & Grains"  style="border-radius: 14px; border: 1px solid rgb(232, 233, 235); width: max-content;  padding: 8px 14px; height: 20px; position: relative; display: flex; align-items: center; justify-content: center; margin-right: 12px; ">
              <div style="font-size: 14px; font-weight: 600; text-align: center; display: flex; align-items: center; width: max-content;"> 
                 Nuts & Grains
              </div>
          </div>
          <div class="category_selector-btn ${activeCategory == "Meats" ? "is_active":""}" data-product_category="Meats"  style="border-radius: 14px; border: 1px solid rgb(232, 233, 235); width: max-content;  padding: 8px 14px; height: 20px; position: relative; display: flex; align-items: center; justify-content: center; margin-right: 12px; ">
              <div style="font-size: 14px; font-weight: 600; text-align: center; display: flex; align-items: center; width: max-content;"> 
                 Meats
              </div>
          </div>
          <div class="category_selector-btn ${activeCategory == "Poultry" ? "is_active" : ""}" data-product_category="Poultry"  style="border-radius: 14px; border: 1px solid rgb(232, 233, 235); width: max-content;  padding: 8px 14px; height: 20px; position: relative; display: flex; align-items: center; justify-content: center; margin-right: 12px; ">
              <div style="font-size: 14px; font-weight: 600; text-align: center; display: flex; align-items: center; width: max-content;"> 
                  Poultry
              </div>
          </div>
          <div class="category_selector-btn ${activeCategory == "Lean Meats" ? "is_active":""}" data-product_category="Lean Meats"  style="border-radius: 14px; border: 1px solid rgb(232, 233, 235); width: max-content;  padding: 8px 14px; height: 20px; position: relative; display: flex; align-items: center; justify-content: center; margin-right: 12px; ">
              <div style="font-size: 14px; font-weight: 600; text-align: center; display: flex; align-items: center; width: max-content;"> 
                  Lean Meats
              </div>
          </div>
          <div class="category_selector-btn ${activeCategory == "Fish & Seafood" ? "is_active":""}" data-product_category="Fish & Seafood"  style="border-radius: 14px; border: 1px solid rgb(232, 233, 235); width: max-content;  padding: 8px 14px; height: 20px; position: relative; display: flex; align-items: center; justify-content: center; margin-right: 12px; ">
              <div style="font-size: 14px; font-weight: 600; text-align: center; display: flex; align-items: center; width: max-content;"> 
                  Fish & Seafood
              </div>
          </div>
          <div class="category_selector-btn ${activeCategory == "Deli" ? "is_active":""}" data-product_category="Deli"  style="border-radius: 14px; border: 1px solid rgb(232, 233, 235); width: max-content;  padding: 8px 14px; height: 20px; position: relative; display: flex; align-items: center; justify-content: center; margin-right: 12px; ">
              <div style="font-size: 14px; font-weight: 600; text-align: center; display: flex; align-items: center; width: max-content;"> 
                  Deli
              </div>
          </div>
      </div>
  </div>
        `;
        document.querySelectorAll('.category_selector-btn').forEach(element => {
            element.addEventListener('click',(e)=>{
                
                document.querySelector('.category_selector-btn.is_active').classList.remove('is_active')
                if(e.target.classList.contains('category_selector-btn')){
                    e.target.classList.toggle('is_active')
                }
                else{
                    e.target.parentElement.classList.add('is_active')
                }
                this.performSearch('').then(results =>
                {
                    this.renderResults(results)
                })
                this.addListeners()

            })
        })
      this.elements.resultsContainer.innerHTML += `                  
      <div class="productsWrapper" style=" height: fit-content; position: relative; padding: 16px 64px; bottom: 16px;">
      <p style=" font-weight: 700; font-size: 14.5px;">Products</p>
      <div class="productsContainer" style=" display: flex; flex-wrap: wrap; align-items: center; position: relative;  width: 1220px;">
        `
    
      results.forEach(element => {
        
        element.forEach(element=>{
                  document.querySelector('.productsContainer').innerHTML += this.options.productsTemplateFunction(element)
        })
        
      })
      this.elements.resultsContainer.innerHTML += `</div>`

      const cartInstance = new ShoppingCart(document.querySelectorAll('.update-cart'),{
        searchURL: new URL('api',window.location.origin),
        templateFunction:(result) => {
            return ``
        },
      });
    }
    performSearch(query){
            const url  = new URL(this.options.searchURL.toString())
            console.log(document.querySelector('.category_selector-btn.is_active').dataset.product_category)
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
}
export default GeneralSearch;
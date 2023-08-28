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
                console.log(e.target.id,e.target.value.length,e.target.value)
                if (element.id == `id_product_price${element.dataset.id}`){ 
                    setTimeout(() => e.target.value = parseFloat(e.target.value).toFixed(2),1200)
                    
                    productInfo.then(results => {
                        const quantity = e.target.value/results[0].productGrade.price.value
                        document.querySelector(`.cart_item-container input#id_product_qty${element.dataset.id}`).value = quantity
                        
                    })
                    setTimeout(()=>{
                        if(document.querySelector(`.cart_item-container input#id_product_qty${element.dataset.id}`).value.length !== 0 || Number.isNaN(document.querySelector(`.cart_item-container input#id_product_qty${element.dataset.id}`).value) !== false ){
                            console.log(document.querySelector(`.cart_item-container input#id_product_qty${element.dataset.id}`).value.length != 0)
                            this.updateQuantity(element.dataset.item_id, document.querySelector(`.cart_item-container input#id_product_qty${element.dataset.id}`).value)
                        }
                        else{
                            console.log(document.querySelector(`.cart_item-container input#id_product_qty${element.dataset.id}`).value.length != 0)
                            this.updateQuantity(element.dataset.item_id, 1)
                        }
                        window.location.reload()
                    },1200)

                }
                else if(element.id == `id_product_qty${element.dataset.id}`){
                    productInfo.then(results => {
                        document.querySelector(`.cart_item-container input#id_product_price${element.dataset.id}`).value = parseFloat(e.target.value * results[0].productGrade.price.value).toFixed(2)                     })
                        setTimeout(()=>{
                            if(document.querySelector(`.cart_item-container input#id_product_qty${element.dataset.id}`).value.length !== 0 || Number.isNaN(document.querySelector(`.cart_item-container input#id_product_qty${element.dataset.id}`).value) !== false ){
                                console.log(document.querySelector(`.cart_item-container input#id_product_qty${element.dataset.id}`).value)
                                if(document.querySelector(`.cart_item-container input#id_product_qty${element.dataset.id}`).value == 0){
                                    this.performUpdate(element.name,'remove')
                                }
                                else{
                                    this.updateQuantity(element.dataset.item_id, document.querySelector(`.cart_item-container input#id_product_qty${element.dataset.id}`).value)
                                }
                            }
                            else{
                                this.updateQuantity(element.dataset.item_id, 1)
                            }
                           window.location.reload()
                        },1200)
                 }
            });
            const optionsMenuRmvButton = document.querySelector(`#id_more_options${element.dataset.item_id}-menu .rmv_item-option`)
            optionsMenuRmvButton.addEventListener('click',() =>{
                this.performUpdate(optionsMenuRmvButton.dataset.product,optionsMenuRmvButton.dataset.action)
                window.location.reload()

            })
            const optionsMenuAddInstructionsButton = document.querySelector(`#id_more_options${element.dataset.item_id}-menu .add_note-option `)
            optionsMenuAddInstructionsButton.addEventListener('click',() => {
                this.renderInstructionsModal(optionsMenuAddInstructionsButton.dataset.product)
            })
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
                        id
                        name
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
                }
            }`;
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
    updateQuantity(ID,quantity){
        const url  = new URL(new URL('api',window.location.origin).toString());
        const Mutation = `mutation OrderMutations{
            updateOrder(id:"${ID}",quantity:"${quantity}"){
              order{
                productGrade{
                  product{
                    name
                  }
                }
              }
            }
          }`
        return fetch(url,{
            method:'POST',
            headers:{
                "Content-Type":"application/json",
                "X-CSRFToken":csrftoken,
            },
            credentials:"include",
            mode:"same-origin",
            body: JSON.stringify({
                query:Mutation,
                variables:{},
            })
        }).then(response => {
            return response.json()
        }).then( responseData => {
            return responseData
        }).finally(results => {
            return results
        })

    }
    renderInstructionsModal(ID){
        const productInfo = this.getProduct(ID).then(results => {
            const modal = `
            <div class="add_notes-modal-container">
            <div class="add_notes-modal-content">
                    <div class="form-header">
    
                    </div>
    
                    <div class="product_details-container">
                        <div class="product" style="position: relative;">
                            <a href="../products/${results[0].productGrade.product.product.id}" style="display: block; position: absolute; height: 100%; width: 100%;"></a>
                            <div class="">
                            <h5 style="margin: 0px;">Product Details</h5>
                            <p class="product_variety-modal" style="font-size: 12px; margin: 0px; font-weight: 500;">${results[0].productGrade.product.name}</p>
                            <p class="product_name-modal" style="font-size: 12px; margin: 0px; font-weight: 600;">${results[0].productGrade.product.product.name}</p>
                            <p class="product_grade-modal" style="font-size: 12px; margin: 0px;">Grade <span id="modal_product-grade" style="font-weight: 500;">${results[0].productGrade.grade}</span></p>
                            <p class="product_quantity-modal" style="font-size: 12px; margin: 0px;"><span class="qty_number-modal">${results[0].quantity} </span><span class="product_unit-modal">${results[0].productGrade.unit.unitAbbr}.</span></p>
                           
                            </div>
                            <div class="modal_arrow-container">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="#343538" xmlns="http://www.w3.org/2000/svg" color="var(--green)" size="16">
                                        <path fill-rule="evenodd" clip-rule="evenodd" d="m16.879 12-5.94-5.94a1.5 1.5 0 0 1 2.122-2.12l7 7a1.5 1.5 0 0 1 0 2.12l-7 7a1.5 1.5 0 0 1-2.122-2.12L16.88 12Z"></path>
                                    </svg>
                                </div>
                        </div>
                        <div class="product_replacement-container">
                            <h6 style="margin: 0px;">Your preferences</h6>
                            <p class="product_quantity-modal">If out of stock...</p>
                            <div class="product-replacement_item">
                                <div class="replacement_actions-container">
                                    <div class="refund_item-btn">
                                        <span>Refund</span>
                                    </div>
                                    <div class="replace_item-btn">
                                        <span>Replace</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
    
                    <h4 class="add_note-heading">Add a note</h4>
                    <textarea class="additional_notes-textbox" placeholder="I would like..."></textarea>
                <div class="add_notes-modal_actions-container">
                    
                    <div class="note_forget-btn">
                        <span >Cancel</span>
                    </div>
                    <div class="note_save-btn">
                        <span>Save</span>
                    </div>
                </div>
            </div>
    
            </div>`   
            document.querySelector('.modal').innerHTML = modal;

        let registerModalClose = () =>{
            add_notes_modal.classList.toggle('hidden');
            document.querySelector('.modal').classList.toggle('hidden')
            getBodyElement.classList.toggle('fixed')
        }

        let add_notes_save_btn = document.querySelector(`.note_save-btn`);
        let add_notes_cancel_btn = document.querySelector(`.note_forget-btn`);

        add_notes_cancel_btn.addEventListener('click',registerModalClose)
        add_notes_save_btn.addEventListener('click',() =>{
            registerModalClose();
        });

        let add_notes_modal = document.querySelector('.add_notes-modal-container')
        let getBodyElement = document.querySelector('body')
        })

    }
    populateResults(results){
        while(this.elements.cart_item.firstChild){
            this.elements.cart_item.removeChild(this.elements.cart_item.firstChild)
        }

        results.forEach(element =>{
            element.forEach( result => {
                this.elements.cart_item.innerHTML += this.options.templateFunction(element)
            })
        })
    }
}
export default ShoppingCart;
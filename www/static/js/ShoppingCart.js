import getCookie from "./csrftoken.js";
import itemTotal from "./cart.js";
import itemSearch from "./ItemSearch.js";
import ReplacementCart from "./ReplacementCart.js";


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
            cart_item : document.querySelector('.cart_item-container'),
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
            const optionsMenuAddInstructionsButton = document.querySelector(`#id_more_options${element.dataset.item_id}-menu .add_note-option`)
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
                    id
                    product {
                      id
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
            console.log(results)
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
            console.log(results)
            return results
        })

    }
    renderInstructionsModal(ID){

        const productInfo = this.getProduct(ID).then(results => {
            const modal = `
            <div class="add_notes-modal-container" id=${results[0].productGrade.id}>
            <div class="add_notes-modal-content">
                    <div class="form-header">
    
                    </div>
    
                    <div class="product_details-container">
                        <div class="product" style="position: relative;">
                            <a href="../products/${results[0].productGrade.product.product.id}${results[0].productGrade.product.id}" style="display: block; position: absolute; height: 100%; width: 100%;"></a>
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
            document.querySelector('.modal').classList.remove('hidden');
            document.body.classList.add('fixed');
        
        let add_notes_modal = document.querySelector('.add_notes-modal-container')
        let registerModalClose = () =>{
            add_notes_modal.classList.toggle('hidden');
            document.querySelector('.modal').classList.toggle('hidden')
            getBodyElement.classList.remove('fixed')
        }

        let add_notes_save_btn = document.querySelector(`.note_save-btn`);
        let add_notes_cancel_btn = document.querySelector(`.note_forget-btn`);

        add_notes_cancel_btn.addEventListener('click',registerModalClose)
        add_notes_save_btn.addEventListener('click',() => {
            registerModalClose();
        });

        const id = ID
        let replacement = document.querySelector('.replace_item-btn');
        replacement.addEventListener('click',() => {
            this.renderReplacementModal(ID);
            const replace_item = new ReplacementCart({
                cart_item_id: this.elements.cart_item.id,
                searchURL: new URL('api', window.location.origin),
                ID: id
            });
        });
        });

    }
    renderReplacementModal(ID){
        document.querySelector('.modal').innerHTML = `
        <div class="replacement-modal-container" id=${ID}>
        <div class="main_product-modal-content" style="    
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
        width: 1220px;
        height: 550px;
        background-color: white;
        border-radius: 14px;
        padding: 20px;
        box-shadow: rgba(0, 0, 0, 0.16) 0px 0px 8px;
        display: flex;
        flex-direction: column;
        overflow-y: auto;
        overflow-x: hidden;">
        <div class="" style="display: flex; flex-direction: column; justify-content: center; width: 100%; height: 550px; padding: 4px 0px; position:relative;">
            <div class="" style="display: flex; flex-direction: column;">
                <div class="close-btn" style="display: flex; align-items: center; margin-bottom: 16px; max-width: fit-content; padding: 6px 32px 6px 6px; border: 1px solid rgb(232,233,235); border-radius: 10px; cursor: pointer;">
                    <svg width="1em" height="1em" viewBox="0 0 24 24" fill="var(--grey2);" xmlns="http://www.w3.org/2000/svg" color="systemGrayscale00;" style="transform: rotate(180deg);" >
                        <path fill-rule="evenodd" clip-rule="evenodd" d="m13.06 3.94 7 7 .02.02c.022.022.043.045.063.068l-.082-.089a1.513 1.513 0 0 1 .274.377 1.494 1.494 0 0 1-.071 1.493 1.28 1.28 0 0 1-.121.163 1.57 1.57 0 0 1-.062.068l-.02.02-7 7a1.5 1.5 0 0 1-2.122 0l-.103-.113a1.5 1.5 0 0 1 .103-2.008l4.44-4.439H5A1.5 1.5 0 0 1 3.5 12l.007-.145A1.5 1.5 0 0 1 5 10.5h10.379l-4.44-4.44a1.5 1.5 0 0 1 2.122-2.12Z"></path>
                    </svg>
                    <span style="margin-left: 10px; font-size: 12px; font-weight: 600;">Back</span>
                </div>

            </div>

            <div class="" style="width: 100%; position: relative; padding: 24px; padding-top: 0px;">
            <div class="">
                <div class="search_container replace"  style="display: flex; flex-direction: column; justify-content: center; border: 1px solid rgb(232,233,235); padding: 16px; border-radius: 14px; margin-top: 16px; margin-right: 48px;">
                    <p style="margin: 0px 0px 16px 0px; font-size: 32px; font-weight: 700;">Choose a replacement</p>
                    <div class="" style="display: flex; align-items: center; margin-bottom: 24px;">
                        <div class="category_selector-btn is_active" style="padding: 6px 24px; border-radius: 10px; margin-right: 16px; border: 1px solid #3f9b3152; cursor: default;" data-product_category=""><span style="font-size: 12px; font-weight: 700; color: var(--green);">All</span></div>
                        <div class="category_selector-btn" style="padding: 6px 24px; border: 1px solid rgb(232,233,235); border-radius: 10px; margin-right: 16px; cursor: pointer;" data-product_category="Green Produce"><span style="font-size: 12px; font-weight: 600;">Green Produce</span></div>
                        <div class="category_selector-btn"  style="padding: 6px 24px; border: 1px solid rgb(232,233,235); border-radius: 10px; margin-right: 16px; cursor: pointer;" data-product_category="Meats"><span style="font-size: 12px; font-weight: 600;">Meats</span></div>
                        <div class="category_selector-btn"  style="padding: 6px 24px; border: 1px solid rgb(232,233,235); border-radius: 10px; margin-right: 16px; cursor: pointer;" data-product_category="Deals"><span style="font-size: 12px; font-weight: 600;">Deals</span></div>
                        <div class="category_selector-btn"  style="padding: 6px 24px; border: 1px solid rgb(232,233,235); border-radius: 10px; cursor: pointer;" data-product_category="Buy it again"><span style="font-size: 12px; font-weight: 600;">Buy it again</span></div>
                    </div>
                    <div class="search_bar" style="display: flex; align-items: center;">
                        <div class="" style="border: 1px solid rgb(232,233,235); display: flex; justify-content: center; align-items: center; border-radius: 7px; padding: 4px 8px; width: 100%; background-color: var(--grey);">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="#343538" xmlns="http://www.w3.org/2000/svg" size="24" color="var(-grey2)">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M16.396 14.275a7 7 0 1 0-2.121 2.121l3.664 3.665a1.5 1.5 0 0 0 2.122-2.122l-3.665-3.664ZM10.5 14.5a4 4 0 1 1 0-8 4 4 0 0 1 0 8Z"></path>
                            </svg>
                            <input type="text" style="background-color: transparent; font-size: 14px; padding: 6px 6px 6px  6px; outline: none; border:transparent; width: 100%;" placeholder="Search">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>
        <div style=" margin: 8px 32px 32px 32px; position: relative; width: 100%;">
            <div class="" style="position: relative;">
                <div class="results-container" style=" display: flex; flex-wrap: wrap; align-items: center; min-height: 290px;">
                </div>
            </div>
        </div>  
            <div class=""></div>
        </div>
    </div>
        `
        const item_search = new itemSearch(document.querySelector('.search_bar'),{
            searchURL :  new URL('api',window.location.origin),
            responseParser: (responseData) => {
                return Object.values(responseData.data)
            },
            templateFunction:(result) => {
                return `
                <div class="product_card-container" style="position: relative;">
                <div class="product-img">
                    <span></span>
                    <div class="product-add">
                        <button data-product="${result.id}" data-action="add" class="product_add-btn update-replace">
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
            </div>
                `
            },
            ID: ID,
        });

        const replacement_back = document.querySelector('.replacement-modal-container .close-btn');
        replacement_back.addEventListener('click',() => this.renderInstructionsModal(ID));    
    }   
    populateResults(results){
        itemTotal()
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
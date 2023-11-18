import getCookie from "./csrftoken.js";
import itemSearch from "./ItemSearch.js";
/**
 * 
 * 
 */
const csrftoken = getCookie('csrftoken');

class Products{
    /**
     * 
     */
    constructor(){
        this.elements = {
            cart_btn: document.querySelector('.update-cart'),
            qty_btn: document.querySelector('.update-qty input'),
            rmv_btn: document.querySelector('.product_remove-btn'),
            rplmt_btn: document.querySelector('.product-replacement')
        }
        this.addListeners();

    }
    addListeners(){
        this.elements.cart_btn.addEventListener('click', () => {
          this.updateBag(this.elements.cart_btn.dataset.product,this.elements.cart_btn.dataset.action).then(result => {
            this.updateQuantity(result,this.elements.qty_btn.value)
            window.location.reload();
        })
    
        })
        this.elements.qty_btn.addEventListener('input',()=>{
            let total = document.querySelector('.prdt_total');
            let qty = document.querySelector('.prdt_qty');
            let price = document.querySelector('.prdt_price');

            var subtotal = parseFloat(price.innerHTML)*parseFloat(this.elements.qty_btn.value);
            if(this.elements.qty_btn.value == '' ||typeof parseFloat(this.elements.qty_btn.value).toFixed(2) == 'NaN'){
                qty.innerHTML = parseFloat('0').toFixed(2)
            } else
            {
                let number = parseFloat(this.elements.qty_btn.value)
                qty.innerHTML = number.toLocaleString('en-US',{
                    minimumFractionDigits: 2,
                    maximumFractionDigits: 2,
                  })
            }
            if(this.elements.qty_btn.value == '' ||typeof subtotal == 'NaN'){
                total.innerHTML = parseFloat('0').toFixed(2)
            } else
            {
                let number =parseFloat(subtotal)
                total.innerHTML = ` ${number.toLocaleString('en-US',{
                    minimumFractionDigits: 2,
                    maximumFractionDigits: 2,
                  })}`;
            }
            if(typeof this.elements.qty_btn.dataset.order !== 'undefined'){
                setTimeout(()=>{
                if(this.elements.qty_btn.value <= 0){
                    this.updateBag(this.elements.cart_btn.dataset.product,'remove');
                    window.location.reload()
                }
                else{
                    this.updateQuantity(this.elements.qty_btn.dataset.order,this.elements.qty_btn.value);
                }
                },1200);

            }

                
        })
        if(typeof this.elements.qty_btn.dataset.order !== 'undefined'){
            this.elements.rmv_btn.addEventListener('click',()=>{
                this.updateBag(this.elements.cart_btn.dataset.product,'remove')
                window.location.reload()
            })
            this.elements.rplmt_btn.addEventListener('click',() =>{
                this.renderReplacementModal()
            })
        }
        
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
    updateUnit(){

    }
    updateGrade(){

    }
    updateBag(productID,Action){        
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
            'productID':productID,
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
    renderReplacementModal(){

        document.querySelector('.modal').innerHTML = `
        <div class="replacement-modal-container">
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
                        <button data-product="${result.id}" data-action="add" class="product_add-btn update-rep">
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
        });

        document.body.classList.toggle('fixed')
        document.querySelector('.modal').classList.toggle('hidden')
        const replacement_back = document.querySelector('.replacement-modal-container .close-btn');
        replacement_back.addEventListener('click',() => {
            document.querySelector('.modal').classList.toggle('hidden');
            document.querySelector('.replacement-modal-container').classList.toggle('hidden');
            document.body.classList.toggle('fixed')
        }); 

        const replace_add = document.querySelectorAll('.update-rep');
        console.log(replace_add)
        replace_add.forEach(element => {
            element.addEventListener('click',()=>{
                this.updateReplace(element.dataset.product)
                document.querySelector('.modal').classList.toggle('hidden');
                document.querySelector('.replacement-modal-container').classList.toggle('hidden');
            })
        })
    }
    updateReplace(ID){
        this.getProductInfo(ID).then(product => {
            console.log(product)
            document.querySelector('.product-replace-actions').innerHTML = `
            <div style="flex-direction:column;" class="replacement_actions-container">
                                        <div class="" style="
                                        font-size: 14px; 
                                        cursor:pointer;
                                        padding: 8px; 
                                        border-radius: 10px;
                                        font-weight: 600; 
                                        color: var(--black); 
                                        width: 100%; 
                                        display flex; 
                                        position:relative; 
                                        margin:0px; 
                                        flex-direction:column; 
                                        margin-bottom:12px; 
                                        align-items:flex-start; 
                                        justify-content:center;
                                        border: 1px solid rgb(232,233,235);" data-replacement=${product[0].id}>
                                            <p style="margin:0px; margin:12px 0px 0px 24px;font-size:12.5px; font-weight:500;">${product[0].product.name}</p>
                                            <p style="margin:0px; margin:0px 0px 12px 24px; font-size:12.5px; font-weight:600;">${product[0].product.product.name}</p>
                                        </div>
                                        <div class="product-replacement">
                                            <span>Change...</span>
                                        </div>
            `;
            
        })
    }
    getProductInfo(ID){
        const url  = new URL(new URL('api', window.location.origin).toString());  
        const Query = `query {
            productById(product:"${ID}"){
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
    }`;
        
        fetch(url,{
            method:'POST',
            headers:{
                "Content-Type":"application/json",
                "X-CSRFToken":csrftoken,
            },
            credentials:"include",
            mode:"same-origin",
            body: JSON.stringify({
                query: Query,
                variables:{},
            })
        }).then(response => {
            return response.json()
        }).then( responseData => {
            return Object.values(responseData.data)
        }).finally(result => {
            return result
        })
    }
}
export default Products;
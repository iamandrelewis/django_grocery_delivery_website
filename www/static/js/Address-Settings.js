/**
 * 
 */
class Address_Settings{
    /**
     * 
     * @param {*} options 
     */
    constructor(options){
        this.options = options;
        this.elements = {
            bd: document.querySelector('.modal'),
            add_address_btn: document.querySelector('.add_address-btn'),
        }
        this.modals = {
            add_address: document.querySelector('.address-modal-container'),


        }
        this.addListeners();
    }
    addListeners(){
        this.elements.add_address_btn.addEventListener('click',()=>{
            document.body.classList.toggle('fixed')
            this.elements.bd.classList.toggle('hidden');
            this.modals.add_address.classList.toggle('hidden');
        })
    }
}
const settings = new Address_Settings();
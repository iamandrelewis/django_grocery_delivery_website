class Delivery_Address{
    constructor(options){
        this.options = options
        this.elements = {
            delivery_address_list: document.querySelectorAll('.'),

        }
        this.addListeners();
    }
    addListeners(){

    }
}

class Delivery_Instructions {
    constructor(options){
        this.options = options
        this.elements = {
            delivery_instructions: document.querySelector('.'),
            delivery_instructions_save: document.querySelector('.'),
        }
        this.addListeners();
    }
    addListeners(){

    }
}
class Payment_Checkout{
    constructor(options){
        this.options = options
        this.elements = {
            select_payment_btn: document.querySelector('.'),
            select_payment_modal: document.querySelector('.'),

            add_payment_btn: document.querySelector('.'),
            add_payment_modal: document.querySelector('.'),

            split_payment_btn: document.querySelector('.'),
            split_payment_modal: document.querySelector('.'),

        }
        this.modals = {

        }
        this.addListeners();
    }
    addListeners(){
        
    }
}
class Delivery_Options{
    constructor(options){
        this.options = options
        this.elements = {
            
            priority_btn: document.querySelector('.priority_btn'),
            standard_btn: document.querySelector('.standard_btn'),
            early_bird_window: document.querySelector('early_bird_btn'),
            night_owl_window: document.querySelector('night_owl_btn'),

            early_bird_window_modal: document.querySelector('.early_bird-wrapper'),
            night_owl_window_modal: document.querySelector('.night_owl-wrapper'),

        }
        this.addListeners();
    }
    addListeners(){

    }
}
class MobileNumber{
    constructor(options){
        this.options = options
        this.elements = {
            select_area_code : document.querySelector('.'),
            mobile_number_input: document.querySelector('.'),

            mobile_number_save: document.querySelector('.'),
            mobile_number_terms: document.querySelector('.'),
        }
        this.addListeners();
    }
    addListeners(){
        
    }
}
class Apply_Promo_Code{
    constructor(options) {
        this.options = options
        this.elements = {
            promo_code_btn: document.querySelector('.'),
            promo_code_modal: document.querySelector('.')

        }   
        this.addListeners();
    }
    addListeners(){

    }
    
}
class Recurring_Order{
    constructor(options) {
        this.options = options
        this.elements = {
            
        }
    }
    addListeners(){

    }
    
}
class Order{
    constructor(options){
        this.options = options
        this.elements = {

        }
        this.addListeners();
    }
    addListeners(){

    }
    getOrderItems(){

    }
}
const payment = new Payment_Checkout();
class Payment_Settings{
    constructor(options){
        this.options = options
        this.elements = {
            bd: document.querySelector('.modal'),
            business_membership_btn: document.querySelector('.business_membership_btn'),
            business_membership_close: document.querySelector('.business_sub_wrapper .close-btn'),
            


            express_membership_btn: document.querySelector('.express_membership_btn'),
            express_membership_close: document.querySelector('.express_sub_wrapper .close-btn'),
            express_membership_join: document.querySelector('.join_express_btn'),


            premium_membership_btn: document.querySelector('.premium_membership_btn'),
            premium_membership_close: document.querySelector('.premium_sub_wrapper .close-btn'),
            premium_membership_join: document.querySelector('.join_premium_btn'),

            add_payment_method_btn: document.querySelector('.add_payment_method_btn'),
            add_payment_method_close: document.querySelector('.add_payment_method-wrapper .close-btn'),
            add_payment_method_card: document.querySelector('.add_payment_method-wrapper .card_option'),

            add_payment_method_billing_close: document.querySelector('.add_payment_method-wrapper .add_billing_details .close-btn'),
            add_payment_method_card_close: document.querySelector('.add_payment_method-wrapper .add_payment_details .close-btn'),
            add_payment_method_billing_continue: document.querySelector('.add_payment_method-wrapper .add_billing_details .continue-btn'),


            express_payment_back: document.querySelector('.express_sub_wrapper .make_payment .close-btn'),
            premium_payment_back: document.querySelector('.premium_sub_wrapper .make_payment .close-btn'),



        }

        this.modals = {
            payment_method: document.querySelector('.add_payment_method-wrapper'),
            payment_method_menu: document.querySelector('.add_payment_method-wrapper .add_payment_menu'),
            payment_method_card: document.querySelector('.add_payment_method-wrapper .add_card-container'),
            payment_method_billing: document.querySelector('.add_payment_method-wrapper .add_billing_details'),
            payment_method_card_details: document.querySelector('.add_payment_method-wrapper .add_payment_details'),

            business_membership: document.querySelector('.business_sub_wrapper'),
            express_membership: document.querySelector('.express_sub_wrapper'),
            premium_membership: document.querySelector('.premium_sub_wrapper'),

            business_membership_features: document.querySelector('.business_sub_wrapper .business_sub-container'),
            express_membership_features: document.querySelector('.express_sub_wrapper .express_sub-container'),
            premium_membership_features: document.querySelector('.premium_sub_wrapper .premium_sub-container'),

            express_membership_payment: document.querySelector('.express_sub_wrapper .make_payment'),
            premium_membership_payment: document.querySelector('.premium_sub_wrapper .make_payment'),


            
        }
        this.addListeners();
    }
    addListeners(){
        this.elements.add_payment_method_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden');
            document.body.classList.toggle('fixed');
            this.modals.payment_method.classList.toggle('hidden');
        })
        this.elements.business_membership_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden');
            document.body.classList.toggle('fixed');
            this.modals.business_membership.classList.toggle('hidden');
        })
        this.elements.express_membership_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden');
            document.body.classList.toggle('fixed');
            this.modals.express_membership.classList.toggle('hidden');
        })
        this.elements.premium_membership_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden');
            document.body.classList.toggle('fixed');
            this.modals.premium_membership.classList.toggle('hidden');
        })
        this.elements.premium_membership_close.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden');
            document.body.classList.toggle('fixed');
            this.modals.premium_membership.classList.toggle('hidden');
        })
        this.elements.express_membership_close.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden');
            document.body.classList.toggle('fixed');
            this.modals.express_membership.classList.toggle('hidden');
        })
        this.elements.business_membership_close.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden');
            document.body.classList.toggle('fixed');
            this.modals.business_membership.classList.toggle('hidden');
        })
        this.elements.premium_membership_join.addEventListener('click',()=>{
            this.modals.premium_membership_features.classList.toggle('hidden')
            this.modals.premium_membership_payment.classList.toggle('hidden')
        })
        this.elements.express_membership_join.addEventListener('click',()=>{
            this.modals.express_membership_features.classList.toggle('hidden')
            this.modals.express_membership_payment.classList.toggle('hidden')
        })
        this.elements.premium_payment_back.addEventListener('click',()=>{
            this.modals.premium_membership_features.classList.toggle('hidden')
            this.modals.premium_membership_payment.classList.toggle('hidden')

        })
        this.elements.express_payment_back.addEventListener('click',()=>{
            this.modals.express_membership_features.classList.toggle('hidden')
            this.modals.express_membership_payment.classList.toggle('hidden')

        })
        this.elements.add_payment_method_close.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden');
            document.body.classList.toggle('fixed');
            this.modals.payment_method.classList.toggle('hidden');
        })
        this.elements.add_payment_method_card.addEventListener('click',()=>{
            this.modals.payment_method_menu.classList.toggle('hidden')
            this.modals.payment_method_card.classList.toggle('hidden')
            this.modals.payment_method_billing.classList.toggle('hidden')
        })
        this.elements.add_payment_method_billing_continue.addEventListener('click',()=>{
            this.modals.payment_method_billing.classList.toggle('hidden')
            this.modals.payment_method_card_details.classList.toggle('hidden')
        })
        this.elements.add_payment_method_card_close.addEventListener('click',()=>{
            this.modals.payment_method_billing.classList.toggle('hidden')
            this.modals.payment_method_card_details.classList.toggle('hidden')
        })
        this.elements.add_payment_method_billing_close.addEventListener('click',()=>{
            this.modals.payment_method_menu.classList.toggle('hidden')
            this.modals.payment_method_card.classList.toggle('hidden')
            this.modals.payment_method_billing.classList.toggle('hidden')
        })
    }
    getPaymentMethod(){

    } 
}

settings = new Payment_Settings();
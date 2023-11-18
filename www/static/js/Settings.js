
class Settings{
    constructor(options){
        this.options = options
        this.elements = {
            bd: document.querySelector('.backdrop'),
            name_btn: document.querySelector('.name_stg-container'),
            gender_btn: document.querySelector('.gender_stg-container'),
            birthday_btn: document.querySelector('.birthday_stg-container'),
            password_btn: document.querySelector('.password_stg-container'),
            email_btn: document.querySelector('.email_stg-container'),
            phone_btn: document.querySelector('.phone_stg-container'),
            sec_phone_btn: document.querySelector('.sec_phone_stg-container'),
            preferred_btn: document.querySelector('.preferred_stg-container'),
            business_name_btn: document.querySelector('.business_name_stg-container'),
            business_category_btn: document.querySelector('.business_category_stg-container'),
            add_team_member_btn: document.querySelector('.add_team_stg-container'),

            name_modal: document.querySelector('.edit_name-container'),
            gender_modal: document.querySelector('.edit_gender-container'),
            birthday_modal: document.querySelector('.edit_birthday-container'),
            password_modal: document.querySelector('.edit_password-container'),
            email_modal: document.querySelector('.edit_email-container'),
            phone_modal: document.querySelector('.edit_phone-container'),
            sec_phone_modal: document.querySelector('.edit_sec_phone-container'),
            preferred_modal: document.querySelector('.edit_preferred_method-container'),
            business_name_modal: document.querySelector('.edit_business_name-container'),
            business_category_modal: document.querySelector('.edit_business_category-container'),
            add_team_member_modal: document.querySelector('.add_team-container')
        }
        this.close_btns= {

            name_btn: document.querySelector('.edit_name-container .close-btn'),
            gender_btn: document.querySelector('.edit_gender-container .close-btn'),
            birthday_btn: document.querySelector('.edit_birthday-container .close-btn'),
            password_btn: document.querySelector('.edit_password-container .close-btn'),
            email_btn: document.querySelector('.edit_email-container .close-btn'),
            phone_btn: document.querySelector('.edit_phone-container .close-btn'),
            sec_phone_btn: document.querySelector('.edit_sec_phone-container .close-btn'),
            preferred_btn: document.querySelector('.edit_preferred_method-container .close-btn'),
            business_name_btn: document.querySelector('.edit_business_name-container .close-btn'),
            business_category_btn: document.querySelector('.edit_business_category-container .close-btn'),
            add_team_member_btn: document.querySelector('.add_team-container .close-btn')
        }

        this.addListeners();
    }
    addListeners(){

        this.elements.name_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.name_modal.classList.toggle('hidden')
        })

        this.elements.gender_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.gender_modal.classList.toggle('hidden')
        })

        this.elements.password_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.password_modal.classList.toggle('hidden')
        })

        this.elements.email_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.email_modal.classList.toggle('hidden')
        })

        this.elements.phone_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.phone_modal.classList.toggle('hidden')
        })

        this.elements.sec_phone_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.sec_phone_modal.classList.toggle('hidden')
        })

        this.elements.preferred_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.preferred_modal.classList.toggle('hidden')
        })

        this.elements.business_category_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.business_category_modal.classList.toggle('hidden')
        })
        this.elements.business_name_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.business_name_modal.classList.toggle('hidden')
        })

        this.elements.add_team_member_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.add_team_member_modal.classList.toggle('hidden')
        })

        this.close_btns.name_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.name_modal.classList.toggle('hidden')
        })

        this.close_btns.gender_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.gender_modal.classList.toggle('hidden')
        })

        this.close_btns.password_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.password_modal.classList.toggle('hidden')
        })

        this.close_btns.email_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.email_modal.classList.toggle('hidden')
        })

        this.close_btns.phone_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.phone_modal.classList.toggle('hidden')
        })

        this.close_btns.sec_phone_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.sec_phone_modal.classList.toggle('hidden')
        })

        this.close_btns.preferred_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.preferred_modal.classList.toggle('hidden')
        })

        this.close_btns.business_category_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.business_category_modal.classList.toggle('hidden')
        })
        this.close_btns.business_name_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.business_name_modal.classList.toggle('hidden')
        })

        this.close_btns.add_team_member_btn.addEventListener('click',()=>{
            this.elements.bd.classList.toggle('hidden')
            document.body.classList.toggle('fixed');
            this.elements.add_team_member_modal.classList.toggle('hidden')
        })
    }
}

const settings = new Settings({});
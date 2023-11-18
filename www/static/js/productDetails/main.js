import Products from "../Products.js";
import { getCartCount } from "../cart.js";
const details = new Products();

const itemTotal = getCartCount().then(result => document.querySelectorAll('#cartNumber').forEach(element => {
    element.innerHTML = result
    if(result <= 0) {
        //console.log(element.parentNode.parentElement)
        element.parentNode.parentElement.style.display='none';
    }
    else{
        //console.log(element.parentNode.parentElement)
        element.parentNode.parentElement.style.display='flex';
    }
    })) 
    
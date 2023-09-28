import getCookie from "./csrftoken.js";

const csrftoken = getCookie('csrftoken');


export const getCartCount = () => {
    const url  = new URL(new URL('shop/update-cart',window.location.origin).toString());    
    return fetch(url,{
    method:'POST',
    headers:{
        "Content-Type":"application/json",
        "X-CSRFToken": csrftoken,
    },
    credentials:"include",
    mode:"same-origin",
    body: JSON.stringify({
        'productID':'',
        'action':'getCartCount'
    })
}).then(response =>{
    return response.json()
}).then(responseData => {
    //console.log(responseData)
    return responseData
}).finally(results =>{
    return results
})
}
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

export default itemTotal;

const option = document.querySelectorAll('.stg-option')
document.body.innerHTML += `<div class="backdrop hidden" style=" position: fixed; height: 100vh; width: 100vw; background-color: rgba(0, 0, 0, 0.16); z-index: 203;"></div>`
const bd = document.querySelector('.backdrop')

option.forEach(x => {
    console.log(x)
    x.addEventListener('click', () => {
        console.log(document.body)
        bd.classList.toggle('hidden')
        document.body.classList.toggle('fixed')
    });
})
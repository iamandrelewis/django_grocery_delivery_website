import InstantSearch from "../js/InstantSearch";
import ShoppingCart from "../js/ShoppingCart";
searchBar = document.querySelector('.searchbar-container');

searchInstance = new InstantSearch(searchBar,{
    
    searchURL: new URL('api/',window.location.origin),
    isCategoryPage : true,
    categoryQuery: searchBar.id,

});

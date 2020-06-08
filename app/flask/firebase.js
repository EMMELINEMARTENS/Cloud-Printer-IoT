import firebaseconfig from '../config/config'; 


const app = {
    init() {

        console.log("fuck")
        // initialiseer de firebase app
        firebase.initializeApp(firebaseconfig);
        this._db = firebase.firestore();
        // cache the DOM
        this.cacheDOMElements();
        this.cacheDOMEvents();

       
    },
}
app.init();
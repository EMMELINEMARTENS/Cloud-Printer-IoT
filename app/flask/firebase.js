import firebaseconfig from '../config/config'; 


const app = {
    init() {


        // initialiseer de firebase app
        firebase.initializeApp(firebaseconfig);
        this._db = firebase.firestore();
        // cache the DOM
        this.cacheDOMElements();
        this.cacheDOMEvents();

       
    },
}
app.init();
(function () {
	
	const firebaseConfig = {
      apiKey: "AIzaSyDrLrP7CszjZU5Y_ijiZN0ZTWYrzapN8Ik",
      authDomain: "timed-response-9151d.firebaseapp.com",
      databaseURL: "https://timed-response-9151d.firebaseio.com",
      //projectId: "timed-response-9151d",
      storageBucket: "",
      //messagingSenderId: "824844136558",
      //appId: "1:824844136558:web:27b98fbc295d78f5"
    };
    firebase.initializeApp(firebaseConfig);

    const preData = document.getElementById('participant');

    const dbRef = firebase.database().ref().child('participant');

    dbRef.on('value', snap => console.log(snap.val()));

}());
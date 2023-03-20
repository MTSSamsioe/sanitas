// all code below is from https://testdriven.io/blog/django-stripe-subscriptions/

// Get Stripe publishable key
fetch("/subscriptions/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
  
  // console.log(stripe)
  
  
  // Event handler
  let submitBtn = document.querySelector("#submitBtn");
  
  console.log(submitBtn)
  
  if (submitBtn !== null) {
    
    console.log( "submitBtn !== null ")
    
    submitBtn.addEventListener("click", () => {
      // Get Checkout Session ID
      
      console.log(" event listener")
      
      fetch("/subscriptions/create-checkout-session/")
      .then((result) => { return result.json(); })
      .then((data) => {
        console.log(data);
        // Redirect to Stripe Checkout
        console.log(stripe.redirectToCheckout({sessionId: data.sessionId}))
        return stripe.redirectToCheckout({sessionId: data.sessionId})
      })
      .then((res) => {
        console.log(res);
      });
    });
  }
});

// function planSelect(name, price, priceId) {
//   console.log(name)
//   var inputs = document.getElementsByTagName('input');

//   for(var i = 0; i<inputs.length; i++){
//     inputs[i].checked = false;
//     if(inputs[i].name== name){

//       inputs[i].checked = true;
//     }
//   }

//   var n = document.getElementById('plan');
//   var p = document.getElementById('price');
//   var pid = document.getElementById('priceId');
//   n.innerHTML = name;
//   p.innerHTML = price;
//   pid.innerHTML = priceId;
//       document.getElementById("submit").disabled = false;


// }
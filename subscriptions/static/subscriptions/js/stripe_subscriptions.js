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

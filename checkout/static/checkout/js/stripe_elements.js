/*
Core logic/payment flow for this comes from here:
https://stripe.com/docs/payments/accept-a-payment
CSS from here: 
https://stripe.com/docs/stripe-js

Variables and other code is taken from Code institute lessons Boutique ado
https://github.com/Code-Institute-Solutions/boutique_ado_v1/
blob/250e2c2b8e43cccb56b4721cd8a8bd4de6686546/checkout/static/checkout/js/stripe_elements.js
*/


var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card input

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});



// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                type: 'card',
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.adress.value),
                        city: $.trim(form.city.value),
                        
                    }
                }
            }
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })
});
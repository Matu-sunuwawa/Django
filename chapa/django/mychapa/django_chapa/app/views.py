from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json


def home(request):
    return render(request, 'app/index.html')

@csrf_exempt
def chapa_webhook(request):
    # who knows what kind of request we are getting
    if request.method != 'POST':
        return JsonResponse(
            {
                'errors': 'only POST method allowed'
            },
            status=400,
        )

    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return JsonResponse(
            {
                'error': "Invalid Json Body"
            },
            status=400
        )
    
    model = settings.CHAPA_TRANSACTION_MODEL
    # add your webhook events here and also you can override the model
    model.response_dump = data
    model.save()
    # TODO: this method should be class view for customization support
    return JsonResponse(data)
    # return render(request, 'app/index.html')

"""
    <form method="POST" action="http://checkout.chapa.co/checkout/web/payment/SC-kFzmRfEjnwDM" >
        <input type="hidden" name="public_key" value="CHAPUBK_TEST-3jhFiUJwWuRa8dFrXwkL5aaDlw61qM4E" />
        <input type="hidden" name="tx_ref" value="negade-tx-12345678sss9" />
        <input type="hidden" name="amount" value="500" />
        <input type="hidden" name="currency" value="ETB" />
        <input type="hidden" name="email" value="matyassinaadugna@gmail.com" />
        <input type="hidden" name="first_name" value="Matyas" />
        <input type="hidden" name="last_name" value="Sina" />
        <input type="hidden" name="title" value="Let us do this" />
        <input type="hidden" name="description" value="Paying with Confidence with cha" />
        <input type="hidden" name="logo" value="https://chapa.link/asset/images/chapa_swirl.svg" />
        <input type="hidden" name="callback_url" value="https://example.com/callbackurl" />
        <input type="hidden" name="return_url" value="https://example.com/returnurl" />
        <input type="hidden" name="meta[title]" value="test" />
        <button type="submit">Pay Now</button>
    </form>
"""
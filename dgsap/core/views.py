from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
import transbank
from transbank.webpay import webpay_plus
from transbank.webpay.webpay_plus import WebpayPlus
from .models import Product

from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.webpay.webpay_plus.mall_transaction import MallTransaction, MallTransactionCreateDetails
from transbank.webpay.webpay_plus import IntegrationType
from transbank.error.transbank_error import TransbankError
import random
# Create your views here.

def base(request):
    try:
        webpay_plus.WebpayPlus.webpay_plus_default_commerce_code = str(597043568497)
        webpay_plus.WebpayPlus.default_api_key = "42bdb1c2d4175e67bc45257ac14c03e7"
        webpay_plus.default_integration_type = IntegrationType.LIVE
        WebpayPlus.configure_for_production(webpay_plus.WebpayPlus.webpay_plus_default_commerce_code,webpay_plus.WebpayPlus.default_api_key )
        products = Product.objects.all()
        result = []
        price = []
        name = []
        for product in products:
            return_url = 'https://chillin.cl/exito'
            response = Transaction.create(product.buy_order, product.session_id, product.price, return_url)
            result.append(response)
            if request.method == "POST":
                token = request.GET.get("token_ws")
                token = response.token
                response = Transaction.commit(token)
                result.append(response)
            name.append(product.name)

            price.append(product.price)


        context = {
            'products': products,
            'response': response,
            'result': result,
            'price': price,
            'name': name,
        }


        return render(request, 'base.html', context)
    except TransbankError as e:
        print(e.message)

    context = {
            'products': products,
            'response': response,
            'result': result,
            'price': price,
            'name': name,
        }

    return render(request, 'base.html', context)

@csrf_exempt 
def success(request):
    try:
        token = request.GET.get("token_ws")
        response = Transaction.commit(token)
        context = { 'response': response}
        return render(request, 'success.html', context)
            

    except TransbankError as e:
        print(e.message)
        
    if request.method == "POST":
       token_tbk = request.POST.get("TBK_TOKEN")
       recuest = request.POST
       orden_compra= request.POST.get('TBK_ORDEN_COMPRA')
       id_sesion = request.POST.get('TBK_ID_SESION')
       context = {
           'token_tbk': token_tbk,

       } 

    
    return render(request, 'success.html', context)


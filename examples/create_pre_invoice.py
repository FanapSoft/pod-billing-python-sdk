# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodBilling

try:
    pod_billing = PodBilling(api_token=API_TOKEN, server_type="production")

    params = {
        "sc_api_key": SC_API_KEY,
        "sc_voucher_hash": []
    }
    products = [
        {
            "productId": 4565,
            "price": 1000,
            "quantity": 1,
            "productDescription": "محصول یک"
        }
    ]
    user_id = 123456
    invoice = pod_billing.create_pre_invoice(user_id=user_id, products=products, guild_code="API_GUILD",
                                             redirect_url="http://localhost", **params)
    print("Invoice :\n", invoice)

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

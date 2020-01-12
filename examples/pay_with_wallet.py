# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodBilling

try:
    pod_billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)
    invoice_id = 123456

    payment_link = pod_billing.payment.get_pay_invoice_by_wallet_link(invoice_id=invoice_id)
    print(payment_link)
    # OUTPUT
    # https://sandbox.pod.ir:1033/v1/pbc/payinvoice/?invoiceId=123456&tokenIssuer=1

    payment_link = pod_billing.payment.get_pay_invoice_by_wallet_link(invoice_id=invoice_id,
                                                                      call_url="http://localhost/webhook.php")
    print(payment_link)
    # OUTPUT
    # https://sandbox.pod.ir:1033/v1/pbc/payinvoice/?invoiceId=123456&tokenIssuer=1&callUri=http%3A%2F%2Flocalhost%2Fwebhook.php

    payment_link = pod_billing.payment.get_pay_invoice_by_wallet_link(invoice_id=invoice_id,
                                                                      call_url="http://localhost/webhook.php",
                                                                      redirect_url="http://localhost/callback.php")
    print(payment_link)
    # OUTPUT
    # https://sandbox.pod.ir:1033/v1/pbc/payinvoice/?invoiceId=123456&tokenIssuer=1&redirectUri=http%3A%2F%2Flocalhost%2Fcallback.php&callUri=http%3A%2F%2Flocalhost%2Fwebhook.php

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

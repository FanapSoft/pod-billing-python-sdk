# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodBilling

try:
    pod_billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)
    unique_number = "f6b6e624e4696d41"

    payment_link = pod_billing.get_pay_invoice_by_unique_number_link(unique_number=unique_number,
                                                                     call_url="http://localhost/webhook.php",
                                                                     redirect_url="http://localhost/callback.php")

    print(payment_link)
    # OUTPUT
    # https://sandbox.pod.ir:1033/v1/pbc/payInvoiceByUniqueNumber/?uniqueNumber=f6b6e624e4696d41&gateway=PEP

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

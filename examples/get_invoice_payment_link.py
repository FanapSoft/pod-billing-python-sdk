# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodBilling

try:
    pod_billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)
    invoice_id = 32157

    payment_link = pod_billing.get_invoice_payment_link(invoice_id=invoice_id,
                                                        call_url="http://localhost/webhook.php",
                                                        redirect_url="http://localhost/callback.php")

    print(payment_link)
    # OUTPUT
    # https://sandbox.pod.ir:1033/v1/pbc/payInvoiceByUniqueNumber/?uniqueNumber=6a8419e0de989b8f&gateway=PEP

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

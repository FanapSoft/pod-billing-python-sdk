# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodBilling

try:
    pod_billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)
    invoice_id = 123456

    if pod_billing.verify_and_close_invoice(invoice_id, sc_api_key=SC_API_KEY, sc_voucher_hash=SC_VOUCHER_HASH):
        print("Invoice verified and closed")

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

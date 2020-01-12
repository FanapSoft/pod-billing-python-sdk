# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodBilling

try:
    pod_billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)
    creditor_invoice_id = 32132  # شناسه فاکتور بستانکار
    debtor_invoice_id = 59929  # شناسه فاکتور بدهکار

    if pod_billing.pay_invoice_by_invoice(creditor_invoice_id=creditor_invoice_id, debtor_invoice_id=debtor_invoice_id):
        print("Invoice Payed")


except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

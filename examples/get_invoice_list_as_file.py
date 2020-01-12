# coding=utf-8
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodBilling

try:
    pod_billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)

    params = {
        "lastNRows": 0,  # تعداد ردیف های مورد نظر در خروجی فایل
        "fromDate": "1396/12/01 01:30:00",  # از تاریخ به صورت شمسی و فرمت yyyy/mm/dd hh:ii:ss
        "toDate": "1398/12/29 10:20:20",  # تا تاریخ به صورت شمسی و فرمت yyyy/mm/dd hh:ii:ss

        # # Optional Params
        # "guildCode": "",  # کد صنف
        # "id": "",   #
        # "billNumber": "",  # شماره قبض که به تنهایی با آن می توان جستجو نمود
        # "uniqueNumber": "",  # شماره کد شده ی قبض که به تنهایی با آن می توان جستجو نمود
        # "trackerId": "",  # کد رهگیری
        # "isCanceled": False,  # وضعیت کنسلی فاکتور , True or False
        # "isPayed": False,  # وضعیت پرداختی فاکتور , True or False
        # "isClosed": False,  # وضعیت بسته بودن فاکتور , True or False
        # "isWaiting": False,  # وضعیت در انتظار پرداخت بودن فاکتور , True or False
        # "referenceNumber": "",  # شماره ارجاع ثبت شده در فاکتور
        # "userId": "",  # شناسه کاربری مشتری فاکتور
        # "query": "",  # عبارت دلخواه مورد جستجو
        # "productIdList": [],  # لیست آرایه ای از شماره محصولات
        # "callbackUrl": "",  # آدرس فراخوانی پس از اتمام تولید گزارش
        # "sc_voucher_hash": [],     # لیست کد های تخفیف سرویس کال
        # "sc_api_key": SC_API_KEY,  # api key سرویس کال
    }

    print(pod_billing.get_invoice_list_as_file(**params))
    # OUTPUT
    # {
    #   "id": 1509,
    #   "statusCode": "EXPORT_SERVICE_STATUS_CREATED",
    #   "creationDate": 1578320483505,
    #   "service": "/nzh/biz/getInvoiceList/"
    # }

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)



import requests


def wallet(url,phone):
    xz = url.split("v=")
    realurl = "https://gift.truemoney.com/campaign/vouchers/" + str(xz[1]) + "/redeem"

    json = {"mobile" : str(phone), "voucher_hash" : str(xz[1])}
    header = {
        'Accept' : 'application/json',
        'Content-type' : 'application/json',
        'Origin' : 'https://gift.truemoney.com',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    response = requests.post(url,json=json,headers=header)
    print(response.json)

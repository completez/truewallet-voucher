

import requests


phone = ""

def wallet(url):

    x = url.split("/")

    CODE = str(x[5])

    phone = ""

    json = {"mobile" : phone, "voucher_hash" : CODE}
    header = {
        'Accept' : 'application/json',
        'Content-type' : 'application/json',
        'Origin' : 'https://gift.truemoney.com',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    response = requests.post(url,json=json,headers=header)
    print(response.json)

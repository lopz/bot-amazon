#!/usr/bin/env python
# -- coding: utf-8 --

import json
import re
import time
import ssl
import datetime
import time
import subprocess 
import sys

import http.client
import urllib.parse



products = {
    "video_cards": [
        {"model": "0000", "asin": "B0031QJKI8", "riid": "IMSFGW4KHWZPZ", "price": 1, "count": 11},
        {"model": "1111", "asin": "B07Q3YFLVD","riid": "I1PJ7P2DX4GJ4I", "price": 1, "count": 2},

        {"model": "1030", "asin": "B08RD5VMNN","riid": "I3PGSRN8ZPYR4", "price": 1, "count": 3},

        {"model": "3080", "asin": "B08HH5WF97", "riid": "I18EUH8SDX9LU6", "price": 1200},        
        {"model": "3080", "asin": "B08HHDP9DW", "riid": "I1O2EXHNBVM3Y7", "price": 1200},
        {"model": "3080", "asin": "B08R14HX34", "riid": "IWOH9RAG6EGG6", "price": 1200},
        {"model": "3080", "asin": "B08J6F174Z", "riid": "I3GHOH1AVDQWBN", "price": 1200},
        {"model": "3080", "asin": "B08HVV2P4Z", "riid": "I1B1Y3SGAAGLZL", "price": 1200},
        {"model": "3080", "asin": "B08HBR7QBM", "riid": "I1NLOTOJGASCVQ", "price": 1200},
        {"model": "3080", "asin": "B08HR5SXPS", "riid": "I2EE8A6WS9QRI0", "price": 1200},
        {"model": "3080", "asin": "B08QW8BKDV", "riid": "I3OVPM9GRBQIX0", "price": 1200},
        {"model": "3080", "asin": "B08HR7SV3M", "riid": "IRU46JUBS4087", "price": 1200},
        {"model": "3080", "asin": "B08KGZVKXM", "riid": "I14HEI6SN01H7T", "price": 1200},
        {"model": "3080", "asin": "B08HJTH61J", "riid": "I38SE4M52YS0CA", "price": 1200},
        {"model": "3080", "asin": "B08HJS2JLJ", "riid": "I2OQ3E4FVG19IQ", "price": 1200},
        {"model": "3080", "asin": "B08KJ3VKLQ", "riid": "IOVLKJMSMU5G1", "price": 1200},
        {"model": "3080", "asin": "B08HR55YB5", "riid": "I1Y4FVMGBX0NFZ", "price": 1200},
        {"model": "3080", "asin": "B08HR4RJ3Q", "riid": "I3O0NEM1R7TZJM", "price": 1200},
        {"model": "3080", "asin": "B08HR6FMF3", "riid": "I1NTN3VLN3BXL3", "price": 1200},

        {"model": "3070", "asin": "B08KY266MG", "riid": "I2KBUUFQTMO32C", "price": 800},
        {"model": "3070", "asin": "B08HBF5L3K", "riid": "I1NEIJKGUU52PP", "price": 800},
        {"model": "3070", "asin": "B08KY322TH", "riid": "I309YVY7X8UBCQ", "price": 800},
        {"model": "3070", "asin": "B08KXZV626", "riid": "I3SW1GWO1C8K9R", "price": 800},
        {"model": "3070", "asin": "B08L8L71SM", "riid": "IQO0996SZB9YJ", "price": 800},
        {"model": "3070", "asin": "B08L8KC1J7", "riid": "I3L0E464XXS0K", "price": 800},
        {"model": "3070", "asin": "B08M14Y3C7", "riid": "IHSTOON5215JQ", "price": 800},
        {"model": "3070", "asin": "B08MT6B58K", "riid": "I31OZARI8WSFB2", "price": 800},
        {"model": "3070", "asin": "B08L8LG4M3", "riid": "I3BA4P8UI1XP1W", "price": 800},
        {"model": "3070", "asin": "B08L8HPKR6", "riid": "I3Q2D25JOCVYTI", "price": 800},
        {"model": "3070", "asin": "B08HBJB7YD", "riid": "I1EOH2R6MPEOAD", "price": 800},
        {"model": "3070", "asin": "B08L8JNTXQ", "riid": "I3548MR7V7D0E", "price": 800},
        {"model": "3070", "asin": "B08LF1CWT2", "riid": "I2PR6A3K7GTACY", "price": 800},

        {"model": "3060ti", "asin": "B08NYPKW1Z", "riid": "I3CCUJ3PE2TSEB", "price": 650},
        {"model": "3060ti", "asin": "B08P3V572B", "riid": "I1LXJ37ZD1KB1E", "price": 650},
        {"model": "3060ti", "asin": "B08NW5HNYW", "riid": "II55373DJW2P3", "price": 650},
        {"model": "3060ti", "asin": "B08NW693LG", "riid": "I3J42DASWH61H9", "price": 650},
        {"model": "3060ti", "asin": "B08NYPLXPJ", "riid": "ITXL40RTH3SUF", "price": 650},
        {"model": "3060ti", "asin": "B08NYP7KG6", "riid": "I222VP2WBU1SKF", "price": 650},
        {"model": "3060ti", "asin": "B08NYNJ6RC", "riid": "I1AEUV550JCXOV", "price": 650},
        {"model": "3060ti", "asin": "B08Q8QR7PK", "riid": "I3EHYGJ5SQFX3M", "price": 650},
        {"model": "3060ti", "asin": "B083Z7TR8Z", "riid": "I2GXCX8W3QINYE", "price": 650},
        {"model": "3060ti", "asin": "B08P2H5LW2", "riid": "I9Y6HN4CJD6RW", "price": 650},
        {"model": "3060ti", "asin": "B08R876RTH", "riid": "I2JAIPWU3QKG29", "price": 650},
        {"model": "3060ti", "asin": "B083Z5P6TX", "riid": "I33FDGN9X4DNLY", "price": 650},
        {"model": "3060ti", "asin": "B08P2D1JZZ", "riid": "I3UJ2335WKMY0O", "price": 650},        
    ]
}


COOKIE = {
    "csm-hit": "",
    "session-id": "",
    "session-id-time": "",
    "lc-main": "en_US",
    "skin": "noskin",
    "ubid-main": "",
    "session-token": "",
    "x-main": "",
    "at-main": "",
    "sess-at-main": "",
    "sst-main": "",
    "i18n-prefs": "USD"
}

BODY_ADD_ITEM = {
    "ref": "cm_wl_upd_addItemToCart_l_hz",
    "update": "addItemToCart",
    "filter": "unpurchased",
    "isCollaborator": "true",
    "viewType": "list",
    "page": "1",
    "sort": "default",
#    "sid": "",
    "registryId": "REGISTRYID",
#    "quantity": "1",
#    "registryItemId": "",
    "registryType": "wishlist",
    "registrySubType": "",
#    "asin": "",
#    "canonicalAsin": "",
    "isGift": "0",
    "price": "0.97",
#    "merchantId": "",
#    "offerId": "",
    "promotionId": "",
}


HEADERS = {

    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8",
    "Accept-Language": "es-ES",
    "DNT": 1,
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": 1,
}


AMAZON = "www.amazon.com"
url_list_print = "/hz/wishlist/printview/1Q2G7ZNM00N59?language=en_US"
url_list = "/hz/wishlist/genericItemsPage/1Q2G7ZNM00N59?type=wishlist&filter=all&sort=default&viewType=list"
url_add_card = "/gp/registry/wishlist/ref=cm_wl_upd_addItemToCart_l_hz"
url_product = "/dp/%s/?coliid=%s"

TELEGRAM = "api.telegram.org"
token_tg = "/TOKEN:TG"
url_send_msg = token_tg + "/sendMessage"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



def myhttp(host, method, url, body, headers):
    conn = http.client.HTTPSConnection(host=host, port=443, context=ctx)
    conn.request(method=method, url=url, body=body, headers=headers)
    resp = conn.getresponse()
    try:
        data = str(resp.read())
    except:
        data = ""

    return resp, data

def db_item(rrid, price):
    for item in products["video_cards"]:
        if item["riid"] == rrid:
            price = int(price)
            if price <= item["price"]:
                return item
    return False



def add_to_car(product, count):
    body_add_item = BODY_ADD_ITEM
    body_add_item["quantity"] = count
    body_add_item["offerId"] = product["offerListingID"]
    body_add_item["sid"] = product["session-id"]
    body_add_item["merchantId"] = product["merchantID"]
    body_add_item["asin"] = product["ASIN"]
    body_add_item["canonicalAsin"] = product["ASIN"]
    body_add_item["registryItemId"] = product["sourceCustomerOrgListItemID"]

    body = '&'.join("%s=%s" % (key,val) for (key,val) in body_add_item.items())
    headers = HEADERS
    headers["Cookie"] = '; '.join("%s=%s" % (key,val) for (key,val) in COOKIE.items())
    headers["Referer"] = "https://www.amazon.com/hz/wishlist/ls/1Q2G7ZNM00N59/ref=nav_wishlist_lists_1?_encoding=UTF8&type=wishlist"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["X-Requested-With"] = "XMLHttpRequest"
    headers["Content-Length"] = len(body)
    headers["Origin"] = "https://www.amazon.com"
    c = 0
    #for i in range(count):
    print(headers)
    resp, html = myhttp("POST", url_add_card, body, headers)

    COOKIE["session-token"] = get_token(resp)
    if resp.status == 200:
        #print(html)
        rex = re.search("\">([\w ]+)</d", html)
        if rex:
            msg = rex.groups()
            return msg
    return ""

def get_token(resp):
    cookie = resp.getheader("Set-cookie")
    print(cookie)
    rex = re.search("token=(.+?);", cookie)
    token = rex.groups()[0]
    return token

def send_alert(msg):
    headers = {}
    url_api_ws = "/api/send"
    body = '{"number": "%s", "message": "%s"}' % ("59177091688", msg)
    headers["Content-Length"] = len(body)
    
    conn = http.client.HTTPConnection(host="localhost", port=1111)

    conn.request(method="POST", url=url_api_ws, body=body, headers=headers)
    resp = conn.getresponse()
    print(str(resp.read()))

def send_message(msg):
    headers = {}
    body = '{"chat_id": "%s", "text": "%s", "disable_web_page_preview": "true"}' % ("209785544", msg)
    headers["Content-Length"] = len(body)
    headers["Content-Type"] = "application/json"
    resp, data = myhttp(TELEGRAM, "POST", url=url_send_msg, body=body, headers=headers)
    
    #if resp.status == 200:
    #print(data)

def get_product(item):
    url = url_product % (item["asin"], item["riid"])
    headers = HEADERS
    headers["Cookie"] = '; '.join("%s=%s" % (key,val) for (key,val) in COOKIE.items())
    headers["Host"] = "www.amazon.com"

    print(headers)
    resp, html = myhttp(AMAZON, "GET", url, None, headers=headers)

    if resp.status == 200:
        rex = re.findall("name=\"([\w-]+)\" value=\"([\w%/+=\-]+)?\"", html)
        return dict(rex)
    else:
        return False

def get_whitelist():
    headers = HEADERS
    
    headers["Cookie"] = '; '.join("%s=%s" % (key,val) for (key,val) in COOKIE.items())
    headers["Host"] = "www.amazon.com"
    resp = myhttp(AMAZON, "GET", url_list_print, None, headers=headers)
    return resp

while True:
    now = datetime.datetime.now()
    dt = now.strftime("%Y-%m-%d-%H:%M")

    resp, data = get_whitelist()

    if ((resp.status == 200) and (data != "")):
        #print(resp)
        lines = data.split("\"table")
        for line in lines:
            rex = re.search("Row_([\d\w]+).+?alt=\"([^\"]+).+?small\">([^<]+).+?span>\$(1?,?\d+\.\d+)?", line)

            if rex:
                riid, desc, store, price = rex.groups()
                if price:
                    price = float(price.replace(',', ''))
                res = "%s: %s - %s - [%s -> $%s]" % (dt, riid, desc, store, price)
                print(res)

                item = db_item(riid, price)
                if not item:
                    print("ASIN not found in DB or the price its highest to threshold")
                else:

                    url = url_product % (item["asin"], item["riid"])
                    msg = "https://%s%s - %s - [%s -> $%s]" % (AMAZON, url, desc, store, price)
                    #print(msg)
                    send_message(msg)
                    #product = get_product(item)
                    #print(product)
                    #msg = add_to_car(product, item["count"])
                    #print("The product was added: %s" % msg)
                    
    else:
        print("Response cookie: %s" % resp.headers)
        print(data)
    time.sleep(20)

from flask import Flask, render_template, request
import urllib.request, json
import requests

def other_query(url_add,park_name,limit):
    url = "https://developer.nps.gov/api/v1/" + url_add
    if (limit == 0):
        querystring = {"q":park_name,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
    else:
        querystring = {"limit":limit,"q":park_name,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
    response = requests.request("GET", url, headers=HEADERS, params=querystring)
    json_response = json.loads(response.text)
    return json_response

url_add ="events"

HEADERS = {
    'User-Agent': "PostmanRuntime/7.13.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "ba17e7c0-d7da-4c2f-a6b5-398f119b4d7a,5b667102-566b-4af7-a613-ca45eccbc8fb",
    'Host': "developer.nps.gov",
    'cookie': "AWSALB=0LrrYUMkM9CPBQdkK1vRI3uVY/TPlQK7B4VZM131xzrNV2y50kKVhpn74xb4dcoiW9ZvewtQsDguOG6EQIgWsRPo1PyYhQP4p767UQDPvCN0nffmwxa159B//PWh",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"}

json_response = other_query(url_add,"Acadia National Park",0)
description = json_response['data'][0]['description'].strip("<p>")
description = description.strip("</")
print(description)

from flask import Flask, render_template, request
import urllib.request, json
import requests

HEADERS = {
    'User-Agent': "PostmanRuntime/7.13.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "8be31a7d-050c-438d-a10d-c1a2dfacc4f7,85f05be9-c812-4776-b989-af4c1fa46dd0",
    'Host': "developer.nps.gov",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}
def designation_query(query):
    url = "https://developer.nps.gov/api/v1/parks"

    querystring = {"q":query,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}

    response = requests.request("GET", url, headers=HEADERS, params=querystring)
    json_response = json.loads(response.text)

    return json_response
print(parks_query("","National Memorial"))

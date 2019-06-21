import requests
import json
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
def parks_query(state_code,query):
    url = "https://developer.nps.gov/api/v1/parks"
    if not state_code == "":
        querystring = {"stateCode":state_code,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
        response = requests.request("GET", url, headers=HEADERS, params=querystring)
        json_response = json.loads(response.text)
        return json_response
    elif not query == "":
        querystring = {"limit":500,"fields":"images,operatingHours,entrancefees,entrancepasses","q":query,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
        response = requests.request("GET", url, headers=HEADERS, params=querystring)
        json_response = json.loads(response.text)
        if(json_response['total'] !="1"):

            for i in range(0,int(json_response['total'])):
                if(query ==json_response['data'][i]['fullName']):
                    return(json_response['data'][i])
        else:
            return json_response['data'][0]


def visitor_center_query(park_code):

    url = "https://developer.nps.gov/api/v1/visitorcenters"
    querystring = {"parkCode":park_code,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
    response = requests.request("GET", url, headers=HEADERS, params=querystring)
    json_response = json.loads(response.text)

    titles = []
    descriptions = []
    directions = []
    urls = []
    if(int(json_response['total'])==0):
        output = "none"
    else:
        for i in range(0,int(json_response['total'])):
            titles.append(json_response['data'][i]['name'])
            descriptions.append(json_response['data'][i]['description'])
            directions.append(json_response['data'][i]['directionsInfo'])
            urls.append(json_response['data'][i]['url'])
        output = zip(titles,descriptions,directions,urls)
    return output
def campgrounds_query(park_code):

    url = "https://developer.nps.gov/api/v1/campgrounds"
    querystring = {"parkCode":park_code,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
    response = requests.request("GET", url, headers=HEADERS, params=querystring)
    json_response = json.loads(response.text)

    titles = []
    descriptions = []
    regulations = []
    campsites = []
    directions = []
    if(int(json_response['total'])==0):
        output = "none"
    else:
        for i in range(0,int(json_response['total'])):
            titles.append(json_response['data'][i]['name'])
            descriptions.append(json_response['data'][i]['description'])
            regulations.append(json_response['data'][i]['regulationsoverview'])
            campsites.append(json_response['data'][i]['campsites']['totalsites'])
            directions.append(json_response['data'][i]['directionsoverview'])
        output = zip(titles,descriptions,regulations,campsites,directions)
    return output

def other_query(url_add,park_name,limit):
    url = "https://developer.nps.gov/api/v1/" + url_add
    if (limit == 0):
        querystring = {"q":park_name,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
    else:
        querystring = {"limit":limit,"q":park_name,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
    response = requests.request("GET", url, headers=HEADERS, params=querystring)
    json_response = json.loads(response.text)
    return json_response
def designation_query(query):
    url = "https://developer.nps.gov/api/v1/parks"

    querystring = {"q":query,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}

    response = requests.request("GET", url, headers=HEADERS, params=querystring)
    json_response = json.loads(response.text)

    return json_response

def search_query(search,category):
    url = "https://developer.nps.gov/api/v1/" + category
    querystring = {"q":search,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
    response = requests.request("GET", url, headers=HEADERS, params=querystring)
    json_response = json.loads(response.text)
    return json_response

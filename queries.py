#this python file holds all functions that are used to retrieve json from NPS site
import requests
import json

#headers neccessary for api calls
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

#query to parks endpoint
def parks_query(state_code,query):
    url = "https://developer.nps.gov/api/v1/parks"

    #if state code is given, return information for all parks in specific state
    if not state_code == "":
        querystring = {"stateCode":state_code,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
        response = requests.request("GET", url, headers=HEADERS, params=querystring)
        json_response = json.loads(response.text)
        return json_response

    #if query is given, return information for park with name given in query
    elif not query == "":
        querystring = {"limit":500,"fields":"images,operatingHours,entrancefees,entrancepasses","q":query,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
        response = requests.request("GET", url, headers=HEADERS, params=querystring)
        json_response = json.loads(response.text)

        #ensures that correct park is chosen and return information for that park
        if(json_response['total'] !="1"):

            for i in range(0,int(json_response['total'])):
                if(query ==json_response['data'][i]['fullName']):
                    return(json_response['data'][i])
        else:
            return json_response['data'][0]

#query to endpoints alerts,articles,campgrounds,events,lesson plans ,news releases, and visitor centers
def other_query(url_add,park_name):
    url = "https://developer.nps.gov/api/v1/" + url_add
    querystring = {"q":park_name,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
    response = requests.request("GET", url, headers=HEADERS, params=querystring)
    json_response = json.loads(response.text)
    return json_response

#query for parks in specific given designation
def designation_query(query):
    url = "https://developer.nps.gov/api/v1/parks"

    querystring = {"q":query,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx","limit":500}

    response = requests.request("GET", url, headers=HEADERS, params=querystring)
    json_response = json.loads(response.text)

    return json_response

#query for given search word from user
def search_query(search):
    url = "https://developer.nps.gov/api/v1/parks"
    querystring = {"q":search,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
    response = requests.request("GET", url, headers=HEADERS, params=querystring)
    json_response = json.loads(response.text)
    return json_response

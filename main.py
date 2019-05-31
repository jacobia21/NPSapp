from flask import Flask, render_template, request
import urllib.request, json
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/interactive_map')
def interactive_map():
    return render_template("interactive_map.html")

@app.route('/state_list')
def state_list():
    return render_template("state_list.html")

@app.route('/parks_by_state',methods = ['GET','POST'])
@app.route('/parks_by_state/<state_code>',methods = ['GET','POST'])
def parks_by_state(state_code):
    if state_code is "":
        return render_template("parks_by_state.html")
    else:
        state_code = state_code.replace('"', '')
        json_response =json_reader(state_code)
        output=[]
        for x in range(0,int(json_response['total'])-1):
            output.append(json_response['data'][x]['fullName'])

        return render_template("/parks_by_state.html",output=output)

def json_reader(state_code):
    url = "https://developer.nps.gov/api/v1/parks"
    querystring = {"stateCode":state_code,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
    headers = {
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "ba17e7c0-d7da-4c2f-a6b5-398f119b4d7a,5b667102-566b-4af7-a613-ca45eccbc8fb",
        'Host': "developer.nps.gov",
        'cookie': "AWSALB=0LrrYUMkM9CPBQdkK1vRI3uVY/TPlQK7B4VZM131xzrNV2y50kKVhpn74xb4dcoiW9ZvewtQsDguOG6EQIgWsRPo1PyYhQP4p767UQDPvCN0nffmwxa159B//PWh",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_response = json.loads(response.text)
    return json_response

if __name__ == '__main__':
        app.run(debug=True)


# Configure API request

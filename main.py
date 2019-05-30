from flask import Flask, render_template, request
import urllib.request, json
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/about')
def about():
    parkName = "Forrest"
    description = "Its green"
    address = "YO MOMMAS HOUSE"
    return render_template("about.html", parkName = parkName,description = description, address = address)


@app.route('/park_list')
def park_list():
    output=full_park_list(1)
    output = output[0]
    return render_template('park_list.html',park_list = output)

@app.route('/park_list1')
def park_list1():
    output=full_park_list(50)
    output = output[0]
    return render_template('park_list.html',park_list = output)

@app.route('/park_list2')
def park_list2():
    output=full_park_list(100)
    output = output[0]
    return render_template('park_list.html',park_list = output)

@app.route('/park_list3')
def park_list3():
    output=full_park_list(150)
    output = output[0]
    return render_template('park_list.html',park_list = output)

@app.route('/park_list4')
def park_list4():
    output=full_park_list(200)
    output = output[0]
    return render_template('park_list.html',park_list = output)

@app.route('/park_list5')
def park_list5():
    output = full_park_list(250)
    output = output[0]
    return render_template('park_list.html',park_list = output)

@app.route('/park_list6')
def park_list6():
    output=full_park_list(300)
    output = output[0]
    return render_template('park_list.html',park_list = output)

@app.route('/park_list7')
def park_list7():
    output = full_park_list(350)
    output = output[0]
    return render_template('park_list.html',park_list = output)

@app.route('/park_list8')
def park_list8():
    output=full_park_list(400)
    output = output[0]
    return render_template('park_list.html',park_list = output)

@app.route('/park_list9')
def park_list9():
    output = full_park_list_last(450)
    output = output[0]
    return render_template('park_list.html',park_list = output)

def full_park_list(start):
    url = "https://developer.nps.gov/api/v1/parks"

    querystring = {"start":start,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}

    headers = {
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "ba17e7c0-d7da-4c2f-a6b5-398f119b4d7a,5b667102-566b-4af7-a613-ca45eccbc8fb",
        'Host': "developer.nps.gov",
        'cookie': "AWSALB=0LrrYUMkM9CPBQdkK1vRI3uVY/TPlQK7B4VZM131xzrNV2y50kKVhpn74xb4dcoiW9ZvewtQsDguOG6EQIgWsRPo1PyYhQP4p767UQDPvCN0nffmwxa159B//PWh",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_response = json.loads(response.text)
    output =[]
    descriptions = []
    designation = []
    links = []
    if start==1:
        start = 0
    for x in range (0,49):
        output.append(json_response['data'][x]['fullName'])
        descriptions.append(json_response['data'][x]['description'])
        designation.append(json_response['data'][x]['designation'])
        links.append(json_response['data'][x]['url'])

    return output,descriptions,designation,links

def full_park_list_last(start):
    url = "https://developer.nps.gov/api/v1/parks"

    querystring = {"start":start,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}

    headers = {
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "ba17e7c0-d7da-4c2f-a6b5-398f119b4d7a,5b667102-566b-4af7-a613-ca45eccbc8fb",
        'Host': "developer.nps.gov",
        'cookie': "AWSALB=0LrrYUMkM9CPBQdkK1vRI3uVY/TPlQK7B4VZM131xzrNV2y50kKVhpn74xb4dcoiW9ZvewtQsDguOG6EQIgWsRPo1PyYhQP4p767UQDPvCN0nffmwxa159B//PWh",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_response = json.loads(response.text)
    output =[]
    if start==1:
        start = 0
    for x in range (0,46):
        output.append(json_response['data'][x]['fullName'])

    return output
if __name__ == '__main__':
        app.run(debug=True)


# Configure API request

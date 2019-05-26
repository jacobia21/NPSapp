from flask import Flask, render_template, request
import urllib.request, json
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/info')
def info():
    return render_template("info.html")

@app.route('/state_list.html')
def state_list():
    output = "hello world"
    return render_template("state_list.html")

@app.route('/Alabama')
def Alabama():
    stateCode = "al"
    output = parkName(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)

@app.route('/Alaska')
def Alaska():
    stateCode = "ak"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)



@app.route('/Arizona')
def Arizona():
    stateCode = "az"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Arkansas')
def Arkansas():
    stateCode = "ar"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/California')
def California():
    stateCode = "ca"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)



@app.route('/Colorado')
def Colorado():
    stateCode = "co"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)



@app.route('/Connecticut')
def Connecticut():
    stateCode = "ct"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Deleware')
def Deleware():
    stateCode = "de"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Florida')
def Florida():
    stateCode = "fl"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)



@app.route('/Georgia')
def Georgia():
    stateCode = "ga"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Hawaii')
def Hawaii():
    stateCode = "hi"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Idaho')
def Idaho():
    stateCode = "id"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)



@app.route('/Illinois')
def Illinois():
    stateCode = "il"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)



@app.route('/Indiana')
def Indiana():
    stateCode = "in"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)



@app.route('/Iowa')
def Iowa():
    stateCode = "ia"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)



@app.route('/Kansas')
def Kansas():
    stateCode = "ks"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Kentucky')
def Kentucky():
    stateCode = "ky"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Louisiana')
def Louisiana():
    stateCode = "la"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)



@app.route('/Maine')
def Maine():
    stateCode = "me"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)



@app.route('/Maryland')
def Maryland():
    stateCode = "md"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Massachusetts')
def Massachusetts():
    stateCode = "ma"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Michigan')
def Michigan():
    stateCode = "mi"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Minnesota')
def Minnesota():
    stateCode = "mn"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Mississippi')
def Mississippi():
    stateCode = "ms"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)

@app.route('/Missouri')
def Missouri():
    stateCode = "mo"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Montana')
def Montana():
    stateCode = "mt"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Nebraska')
def Nebraska():
    stateCode = "ne"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Nevada')
def Nevada():
    stateCode = "nv"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/New_Hampshire')
def New_Hampshire():
    stateCode = "nh"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/New_Jersey')
def New_Jersey():
    stateCode = "nj"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/New_Mexico')
def New_Mexico():
    stateCode = "nm"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/New_York')
def New_York():
    stateCode = "ny"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)

@app.route('/North_Carolina')
def North_Carolina():
    stateCode = "nc"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/North_Dakota')
def North_Dakota():
    stateCode = "nd"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Ohio')
def Ohio():
    stateCode = "oh"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Oklahoma')
def Oklahoma():
    stateCode = "ok"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Oregon')
def Oregon():
    stateCode = "or"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Pennsylvania')
def Pennsylvania():
    stateCode = "pa"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Rhode_Island')
def Rhode_Island():
    stateCode = "ri"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/South_Carolina')
def South_Carolina():
    stateCode = "sc"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)

@app.route('/South_Dakota')
def South_Dakota():
    stateCode = "sd"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Tennessee')
def Tennessee():
    stateCode = "tn"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Texas')
def Texas():
    stateCode = "tx"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Utah')
def Utah():
    stateCode = "ut"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Vermont')
def Vermont():
    stateCode = "vt"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Virginia')
def Virginia():
    stateCode = "va"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Washington')
def Washington():
    stateCode = "wa"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/West_Virginia')
def West_Virginia():
    stateCode = "wv"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Wisconsin')
def Wisconsin():
    stateCode = "wi"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)


@app.route('/Wyoming')
def Wyoming():
    stateCode = "wy"
    output = printInfo(stateCode)
    messages = description(stateCode)
    url = links(stateCode)
    return render_template("parks_by_state.html",output=output,messages=messages,url=url)

    
def query(stateCode):
    url = "https://developer.nps.gov/api/v1/parks"

    querystring = {"stateCode":stateCode,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}

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
    return json_response

def parkName(stateCode):
    json_response=query(stateCode)
    output =[]
    for x in range(0,int(json_response['total'])-1):
        output.append(json_response['data'][x]['fullName'])
    return output
def description(stateCode):
    json_response = query(stateCode)
    messages =[]
    for x in range(0,int(json_response['total'])-1):
        messages.append(json_response['data'][x]['description'])
    return messages
def links(stateCode):
    json_response = query(stateCode)
    links =[]
    for x in range(0,int(json_response['total'])-1):
        links.append(json_response['data'][x]['url'])
    return links

if __name__ == '__main__':
        app.run(debug=True)

# Configure API request

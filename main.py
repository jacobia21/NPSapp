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
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)

@app.route('/Alaska')
def Alaska():
    stateCode = "ak"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Arizona')
def Arizona():
    stateCode = "az"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Arkansas')
def Arkansas():
    stateCode = "ar"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)

@app.route('/California')
def California():
    stateCode = "ca"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Colorado')
def Colorado():
    stateCode = "co"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Connecticut')
def Connecticut():
    stateCode = "ct"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Deleware')
def Deleware():
    stateCode = "de"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Florida')
def Florida():
    stateCode = "fl"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Georgia')
def Georgia():
    stateCode = "ga"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)

@app.route('/Hawaii')
def Hawaii():
    stateCode = "hi"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Idaho')
def Idaho():
    stateCode = "id"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Illinois')
def Illinois():
    stateCode = "il"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Indiana')
def Indiana():
    stateCode = "in"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Iowa')
def Iowa():
    stateCode = "ia"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Kansas')
def Kansas():
    stateCode = "ks"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Kentucky')
def Kentucky():
    stateCode = "ky"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Louisiana')
def Louisiana():
    stateCode = "la"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Maine')
def Maine():
    stateCode = "me"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Maryland')
def Maryland():
    stateCode = "md"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Massachusetts')
def Massachusetts():
    stateCode = "ma"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Michigan')
def Michigan():
    stateCode = "mi"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Minnesota')
def Minnesota():
    stateCode = "mn"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Mississippi')
def Mississippi():
    stateCode = "ms"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Missouri')
def Missouri():
    stateCode = "mo"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Montana')
def Montana():
    stateCode = "mt"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Nebraska')
def Nebraska():
    stateCode = "ne"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Nevada')
def Nevada():
    stateCode = "nv"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/New_Hampshire')
def New_Hampshire():
    stateCode = "nh"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/New_Jersey')
def New_Jersey():
    stateCode = "nj"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/New_Mexico')
def New_Mexico():
    stateCode = "nm"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/New_York')
def New_York():
    stateCode = "ny"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/North_Carolina')
def North_Carolina():
    stateCode = "nc"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/North_Dakota')
def North_Dakota():
    stateCode = "nd"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Ohio')
def Ohio():
    stateCode = "oh"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Oklahoma')
def Oklahoma():
    stateCode = "ok"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Oregon')
def Oregon():
    stateCode = "or"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Pennsylvania')
def Pennsylvania():
    stateCode = "pa"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)

@app.route('/Rhode_Island')
def Rhode_Island():
    stateCode = "ri"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/South_Carolina')
def South_Carolina():
    stateCode = "sc"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/South_Dakota')
def South_Dakota():
    stateCode = "sd"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Tennessee')
def Tennessee():
    stateCode = "tn"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Texas')
def Texas():
    stateCode = "tx"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Utah')
def Utah():
    stateCode = "ut"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Vermont')
def Vermont():
    stateCode = "vt"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Virginia')
def Virginia():
    stateCode = "va"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Washington')
def Washington():
    stateCode = "wa"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/West_Virginia')
def West_Virginia():
    stateCode = "wv"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Wisconsin')
def Wisconsin():
    stateCode = "wi"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)


@app.route('/Wyoming')
def Wyoming():
    stateCode = "wy"
    output = printInfo(stateCode)
    return render_template("parks_by_state.html",output=output)




def printInfo(stateCode):

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
    output =[]
    for x in range(0,int(json_response['total'])-1):
        output.append(json_response['data'][x]['fullName'] + ": " + json_response['data'][x]['description'] + "( " + json_response['data'][0]['url'] +" )")
    return output

if __name__ == '__main__':
        app.run(debug=True)

# Configure API request

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

@app.route('/parks_by_state.html')
def parks_by_state():
    return render_template("parks_by_state.html")#output=output)

@app.route('/Alabama',methods=['GET','POST'])
def Alabama():
    stateCode = "al"

    url = "https://developer.nps.gov/api/v1/parks"

    querystring = {"stateCode":"AL","api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}

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

    output =''
    for x in range(0,int(json_response['total'])-1):
        output = output + json_response['data'][x]['fullName'] + "\n"
    print(output)
    return (render_template("Alabama.html"),output)

@app.route('/Alaska')
def Alaska():
    return render_template("Alaska.html")

@app.route('/Arizona')
def Arizona():
    return render_template("Arizona.html")

@app.route('/Arkansas')
def Arkansas():
    return render_template("Arkansas.html")

@app.route('/California')
def California():
    return render_template("California.html")

@app.route('/Colorado')
def Colorado():
    return render_template("Colorado.html")

@app.route('/Connecticut')
def Connecticut():
    return render_template("Connecticut.html")

@app.route('/Deleware')
def Deleware():
    return render_template("Deleware.html")

@app.route('/Florida')
def Florida():
    return render_template("Florida.html")

@app.route('/Georgia')
def Georgia():
    return render_template("Georgia.html")

@app.route('/Hawaii')
def Hawaii():
    return render_template("Hawaii.html")

@app.route('/Idaho')
def Idaho():
    return render_template("Idaho.html")

@app.route('/Illinois')
def Illinois():
    return render_template("Illinois.html")

@app.route('/Indiana')
def Indiana():
    return render_template("Indiana.html")

@app.route('/Iowa')
def Iowa():
    return render_template("Iowa.html")

@app.route('/Kansas')
def Kansas():
    return render_template("Kansas.html")

@app.route('/Kentucky')
def Kentucky():
    return render_template("Kentucky.html")

@app.route('/Louisiana')
def Louisiana():
    return render_template("Louisiana.html")

@app.route('/Maine')
def Maine():
    return render_template("Maine.html")

@app.route('/Maryland')
def Maryland():
    return render_template("Maryland.html")

@app.route('/Massachusetts')
def Massachusetts():
    return render_template("Massachusetts.html")

@app.route('/Michigan')
def Michigan():
    return render_template("Michigan.html")

@app.route('/Minnesota')
def Minnesota():
    return render_template("Minnesota.html")

@app.route('/Mississippi')
def Mississippi():
    return render_template("Mississippi.html")

@app.route('/Missouri')
def Missouri():
    return render_template("Missouri.html")

@app.route('/Montana')
def Montana():
    return render_template("Montana.html")

@app.route('/Nebraska')
def Nebraska():
    return render_template("Nebraska.html")

@app.route('/Nevada')
def Nevada():
    return render_template("Nevada.html")

@app.route('/New_Hampshire')
def New_Hampshire():
    return render_template("New_Hampshire.html")

@app.route('/New_Jersey')
def New_Jersey():
    return render_template("New_Jersey.html")

@app.route('/New_Mexico')
def New_Mexico():
    return render_template("New_Mexico.html")

@app.route('/New_York')
def New_York():
    return render_template("New_York.html")

@app.route('/North_Carolina')
def North_Carolina():
    return render_template("North_Carolina.html")

@app.route('/North_Dakota')
def North_Dakota():
    return render_template("North_Dakota.html")

@app.route('/Ohio')
def Ohio():
    return render_template("Ohio.html")

@app.route('/Oklahoma')
def Oklahoma():
    return render_template("Oklahoma.html")

@app.route('/Oregon')
def Oregon():
    return render_template("Oregon.html")

@app.route('/Pennsylvania')
def Pennsylvania():
    return render_template("Pennsylvania.html")

@app.route('/Rhode_Island')
def Rhode_Island():
    return render_template("Rhode_Island.html")

@app.route('/South_Carolina')
def South_Carolina():
    return render_template("South_Carolina.html")

@app.route('/South_Dakota')
def South_Dakota():
    return render_template("South_Dakota.html")

@app.route('/Tennessee')
def Tennessee():
    return render_template("Tennessee.html")

@app.route('/Texas')
def Texas():
    return render_template("Texas.html")

@app.route('/Utah')
def Utah():
    return render_template("Utah.html")

@app.route('/Vermont')
def Vermont():
    return render_template("Vermont.html")

@app.route('/Virginia')
def Virginia():
    return render_template("Virginia.html")

@app.route('/Washington')
def Washington():
    return render_template("Washington.html")

@app.route('/West_Virginia')
def West_Virginia():
    return render_template("West_Virginia.html")

@app.route('/Wisconsin')
def Wisconsin():
    return render_template("Wisconsin.html")

@app.route('/Wyoming')
def Wyoming():
    return render_template("Wyoming.html")






if __name__ == '__main__':
        app.run(debug=True)

# Configure API request

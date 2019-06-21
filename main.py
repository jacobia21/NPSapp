from flask import Flask, render_template, request
import urllib.request, json
import requests_cache
from datetime import datetime, timedelta

requests_cache.install_cache('demo_cache',expire_after=timedelta(hours=1))
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

app = Flask(__name__)
print(app)
@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/interactive_map')
def interactive_map():
    return render_template("interactive_map.html")

@app.route('/state_list_homepage')
def state_list_homepage():
    return render_template("state_list_homepage.html")

@app.route('/parks_by_state',methods=['GET','POST'])
@app.route('/parks_by_state/<state_code>',methods = ['GET','POST'])
def state_list(state_code):
    state_code = state_code.replace('"', '')
    if state_code is "":
        return render_template("state_list_homepage.html")
    else:
        json_response =parks_query(state_code,"")
        output=[]
        for x in range(0,int(json_response['total'])-1):
            output.append(json_response['data'][x]['fullName'])
        state_code=state_code.upper().lstrip()
        state = states[state_code]

        return render_template("/parks_by_state.html",output=output,state=state,state_code=state_code)


@app.route('/designation',methods=['GET','POST'])
@app.route('/designation/<designation>',methods = ['GET','POST'])
def designation(designation = ""):
    designation = designation.replace('"', '')
    if designation is "":
        return render_template("designation.html",homepage = True)
    else:
        json_response =designation_query(designation)
        output=[]
        for x in range(0,int(json_response['total'])-1):
            output.append(json_response['data'][x]['fullName'])

        return render_template("/designation.html",output=output,designation = designation)

@app.route('/alerts',methods=['GET','POST'])
@app.route('/alerts/<park_name>',methods = ['GET','POST'])
def alerts(park_name = ""):
    if(park_name == ""):
        return render_template("/alerts.html",homepage=True)
    else:
        url_add ="alerts"
        park_name = park_name.replace('"', '')
        json_response = other_query(url_add,park_name,50)
        titles = []
        description = []
        category = []
        symbols = []
        if(int(json_response['total'])==0):
            return render_template("alerts.html",string=("Currently no Alerts for this park"),no_center=True,park=park_name)
        else:
            num = int(json_response['total'])
            if(num > 50):
                num = 50
            for x in range(0,num):
                titles.append(json_response['data'][x]['title'])
                description.append(json_response['data'][x]['description'])
                category.append(json_response['data'][x]['category'])
                if(category[x] == 'Danger'):
                    symbols.append("danger.png")
                elif(category[x] == 'Caution'):
                    symbols.append("caution_symbol.png")
                elif(category[x] == 'Park Closure'):
                    symbols.append("closure.png")
                elif(category[x] == 'Information'):
                    symbols.append("info.png")
                else:
                    symbols.append("https://federalnewsnetwork.com/wp-content/uploads/2019/05/cropped-7E9AE9B6-1DD8-B71B-0BD2CA3A36AEBEC4-1.png")
            return render_template("alerts.html",alerts=zip(titles, description,category,symbols),park=park_name)


@app.route('/articles.html', methods = ['GET','POST'])
@app.route('/articles/<park_name>',methods = ['GET','POST'])
def articles(park_name = ""):
    if(park_name == ""):
        return render_template("/articles.html",homepage=True)
    else:
        url_add ="articles"
        park_name = park_name.replace('"', '')
        json_response = other_query(url_add,park_name,50)
        if(int(json_response['total']) > 50):
            num = 50
        else:
            num = int(json_response['total'])

        if(int(json_response['total']) == 0):
            output = "Currently no articles related to this park"
            return render_template("articles.html",string=output,no_articles=True)
        else:
            titles = []
            listingdescriptions = []
            listingimages = []
            urls =[]

            for i in range(0,num-1):
                titles.append(json_response['data'][i]['title'])
                listingdescriptions.append(json_response['data'][i]['listingdescription'])
                if json_response['data'][i]['listingimage']['url'] != "":
                    listingimages.append(json_response['data'][i]['listingimage']['url'])
                else:
                    listingimages.append("https://federalnewsnetwork.com/wp-content/uploads/2019/05/cropped-7E9AE9B6-1DD8-B71B-0BD2CA3A36AEBEC4-1.png")
                urls.append(json_response['data'][i]['url'])

            return render_template("/articles.html",articles=zip(titles,listingdescriptions,listingimages,urls),park=park_name)



@app.route('/events',methods=['GET','POST'])
@app.route('/events/<park_name>',methods = ['GET','POST'])
def events(park_name = ""):
    if(park_name == ""):
        return render_template("/events.html",homepage=True)
    else:
        url_add ="events"
        park_name = park_name.replace('"', '')
        json_response = other_query(url_add,park_name,0)
        titles = []
        description = []
        contact_name = []
        contact_email = []
        contact_number = []
        category = []
        date_start = []
        recurrence_date_end = []
        regres_info = []
        fees_info = []
        timestart = []
        timeend = []
        urls = []

        if(int(json_response['total'])==0):
            return render_template("events.html",string=("Currently no events for this park"),no_events = True,park=park_name)
        else:
            for x in range(0,int(json_response['total'])):
                titles.append(json_response['data'][x]['title'])
                #descriptions from api had paragraph and strong tags in response, these lines remove them
                des = json_response['data'][x]['description']
                des = des.replace("<p>",'')
                des = des.replace("</p>",'')
                des = des.replace("<strong>.</strong></p>",'.')
                description.append(des)

                category.append(json_response['data'][x]['category'])
                date_start.append(json_response['data'][x]['datestart'])
                timestart.append(json_response['data'][x]['times'][0]['timestart'])
                timeend.append(json_response['data'][x]['times'][0]['timeend'])
                urls.append(json_response['data'][x]['infourl'])
                if(json_response['data'][x]['contactname'] is not ""):
                    contact_name.append(json_response['data'][x]['contactname'])
                    contact_email.append(json_response['data'][x]['contactemailaddress'])
                    contact_number.append(json_response['data'][x]['contacttelephonenumber'])
                else:
                    contact_name.append("No contact given")
                    contact_email.append("")
                    contact_number.append("")

                if(json_response['data'][x]['recurrencedateend'] is "true"):
                    recurence_date_end.append(json_response['data'][x]['recurencedateend'])
                else:
                    recurrence_date_end.append("Not a recurring event")

                if(json_response['data'][x]['isfree'] is "true"):
                    fees_info.append(json_response['data'][x]['feesinfo'])
                else:
                    fees_info.append("No fees Required")

                if(json_response['data'][x]['isregresrequired'] is "true"):
                    regres_info.append(json_response['data'][x]['regresinfo'])
                else:
                    regres_info.append("No registration required")
                contact_info = zip(contact_name, contact_email, contact_number)
                return render_template("events.html",events=zip(titles, description,category,date_start,recurrence_date_end,fees_info,regres_info,timestart,timeend,urls),park=park_name)

@app.route('/news_releases.html')
@app.route('/news_releases/<park_name>',methods = ['GET','POST'])
def news_releases(park_name = ""):
    if(park_name == ""):
        return render_template("/news_releases.html",homepage=True)
    else:
        url_add ="newsreleases"
        park_name = park_name.replace('"', '')
        json_response = other_query(url_add,park_name,0)
        titles = []
        release_dates= []
        images= []
        urls = []
        abstracts = []
        if(int(json_response['total'])==0):
            return render_template("news_releases.html",string=("Currently no News Releases for this park"),no_releases=True,park= park_name)
        else:
            num = int(json_response['total'])
            if(num > 50):
                num = 50
            for x in range(0,num):
                titles.append(json_response['data'][x]['title'])
                release_dates.append(json_response['data'][x]['releasedate'])
                if(json_response['data'][x]['image']['url'] == ""):
                    images.append("https://federalnewsnetwork.com/wp-content/uploads/2019/05/cropped-7E9AE9B6-1DD8-B71B-0BD2CA3A36AEBEC4-1.png")
                else:
                    images.append(json_response['data'][x]['image']['url'])

                urls.append(json_response['data'][x]['url'])
                abstracts.append(json_response['data'][x]['abstract'])
            return render_template("news_releases.html",releases=zip(titles, release_dates,images,urls,abstracts),park=park_name)
@app.route('/education.html')
@app.route('/education/<park_name>',methods = ['GET','POST'])
def education(park_name = ""):
    if(park_name == ""):
        return render_template("/education.html",homepage=True)
    else:
        url_add ="lessonplans"
        park_name = park_name.replace('"', '')
        json_response = other_query(url_add,park_name,0)
        titles = []
        subjects= []
        grade_levels= []
        question_objectives = []
        durations = []
        urls = []
        if(int(json_response['total'])==0):
            return render_template("education.html",string=("Currently no News Releases for this park"),no_resources=True,park= park_name)
        else:
            num = int(json_response['total'])
            if(num > 50):
                num = 50
            for x in range(0,num):
                titles.append(json_response['data'][x]['title'])
                subjects.append(json_response['data'][x]['subject'])
                grade_levels.append(json_response['data'][x]['gradelevel'])
                question_objectives.append(json_response['data'][x]['questionobjective'])
                durations.append(json_response['data'][x]['duration'])
                urls.append(json_response['data'][x]['url'])

            return render_template("education.html",lesson_plans=zip(titles,subjects,grade_levels,question_objectives,durations,urls),park=park_name)
@app.route('/name_list/<alphabetChar>',methods=['GET','POST'])
def name_list(alphabetChar):
    alphabetChar = alphabetChar.replace('"','')
    json_response = parks_query("","")
    output = []
    for i in range(0,495):
        name = json_response['data'][i]['fullName']
        name = name.replace('"','')
        if name.startswith(alphabetChar):
            output.append(name)
    return render_template("/name_list.html",output=output,letter = alphabetChar)

@app.route('/park_info/<park_name>',methods=['GET','POST'])
def park_info(park_name =""):
        park_name = park_name.replace('"', '')
        json_response = parks_query("",park_name)
        park_code = json_response['parkCode']
        designation = json_response['designation']
        description =  json_response['description']
        directionsInfo = json_response['directionsInfo']
        directionsUrl = json_response['directionsUrl']
        url = json_response['url']
        weatherInfo = json_response['weatherInfo']
        entrance_cost = json_response['entranceFees'][0]['cost'].replace("0000","00")
        entrance_description = json_response['entranceFees'][0]['description']
        #print(entrance_fees['cost'].replace("0000","00"))

        try:
            entrance_passes = json_response['entrancePasses'][0]['description']
        except IndexError:
            entrance_passes = ""

        try:
            monday=(json_response['operatingHours'][0]['standardHours']['monday'])
            tuesday= (json_response['operatingHours'][0]['standardHours']['tuesday'])
            wednesday = (json_response['operatingHours'][0]['standardHours']['wednesday'])
            thursday =(json_response['operatingHours'][0]['standardHours']['thursday'])
            friday=(json_response['operatingHours'][0]['standardHours']['friday'])
            saturday = (json_response['operatingHours'][0]['standardHours']['saturday'])
            sunday =(json_response['operatingHours'][0]['standardHours']['sunday'])
        except IndexError:
            monday = tuesday = wednesday = thursday = friday = saturday = sunday = "No Hours Listed"

        try:
            image = json_response['images'][0]['url']
            img_caption = json_response['images'][0]['caption']
        except IndexError:
            image = "https://federalnewsnetwork.com/wp-content/uploads/2019/05/cropped-7E9AE9B6-1DD8-B71B-0BD2CA3A36AEBEC4-1.png"
            img_caption = "No Pictures Were Available"

        vc_info = visitor_center_query(park_code)
        campgrounds = campgrounds_query(park_code)

        return render_template("/park_info.html",park_code=park_code,name=park_name,designation=designation,description=description,directionsInfo = directionsInfo,
        directionsUrl= directionsUrl,url=url,weatherInfo=weatherInfo,visitor_centers = vc_info,monday=monday,tuesday=tuesday,wednesday=wednesday,thursday=thursday,
        friday=friday,saturday=saturday,sunday=sunday,image=image,caption=img_caption,campgrounds=campgrounds,entrance_cost = entrance_cost,entrance_description=entrance_description,passes=entrance_passes)

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
    else:
        querystring = {"limit":500,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
        response = requests.request("GET", url, headers=HEADERS, params=querystring)
        json_response = json.loads(response.text)
        return json_response


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


states = {'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'}

if __name__ == '__main__':
        app.run(debug=True)

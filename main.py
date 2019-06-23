from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from lists import parks, states
from queries import *
import re

app = Flask(__name__)

#sql database
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://:{password}@{hostname}/{databasename}".format(
    username="jacobia",
    password="44Eagles!",
    hostname="jacobia.mysql.pythonanywhere-services.com",
    databasename="jacobia$NPS-database",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)


@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/interactive_map')
def interactive_map():
    return render_template("interactive_map.html")

@app.route('/state_list_homepage')
def state_list_homepage():
    return render_template("state_list_homepage.html")

@app.route('/iparks_by_state',methods=['GET','POST'])
@app.route('/iparks_by_state/<state_code>',methods = ['GET','POST'])
def state_list(state_code):
    state_code = state_code.replace('"', '')

    #if no state_code is passed in, returns a list of states for user to choose from
    if state_code is "":
        return render_template("state_list_homepage.html")
    #if a state code is passed in, returns the parks in specific state, along with the state and state code
    else:
        json_response =parks_query(state_code,"")
        output=[]
        for x in range(0,int(json_response['total'])-1):
            output.append(json_response['data'][x]['fullName'])
        state_code=state_code.upper().lstrip()
        state = states[state_code]

        return render_template("/iparks_by_state.html",output=output,state=state,state_code=state_code)

@app.route('/name_list/<alphabetChar>',methods=['GET','POST'])
def name_list(alphabetChar):
    alphabetChar = alphabetChar.replace('"','')
    output = []
    names = parks
    #finds all parks that begin with selected char, and returns them in a list
    for name in names:
        if(name.startswith(alphabetChar)):
            output.append(name)
    return render_template("/name_list.html",output=output,letter = alphabetChar)

@app.route('/designation',methods=['GET','POST'])
@app.route('/designation/<designation>',methods = ['GET','POST'])
def designation(designation = ""):
    designation = designation.replace('"', '')
    #if no designation is passed in, returns designation homepage
    if designation is "":
        return render_template("designation.html",homepage = True)
    #if designation is passsed in, returns all parks with specified designation
    else:
        json_response =designation_query(designation)
        output=[]
        for x in range(0,int(json_response['total'])-1):
            output.append(json_response['data'][x]['fullName'])
        #small change to National Cemetery so that it appears correctly on page
        if designation == "National Cemetery":
            designation = "National Cemeterie"
        return render_template("/designation.html",output=output,designation = designation)

@app.route('/search',methods=['GET','POST'])
def search():
    if request.method == "GET":
        return render_template("search.html", no_search=True)
    else:
        search = request.form["search"]
        if len(search) < 4:
            return render_template("search.html", short = True)
        search_results = search_query(search)
        names = []
        descriptions = []
        num = int(search_results['total'])
        if num == 1:
            num =2
        if(num > 50):
            num = 50
        for i in range(0,num-1):
            names.append(search_results['data'][i]['fullName'])
            descriptions.append(search_results['data'][i]['description'])

        return render_template("search.html",search=search,results = zip(names,descriptions))

@app.route('/alerts',methods=['GET','POST'])
@app.route('/alerts/<park_name>',methods = ['GET','POST'])
def alerts(park_name = ""):
    url_add ="alerts"
    park_name = park_name.replace('"', '')
    json_response = other_query(url_add,park_name)
    titles = []
    description = []
    symbols = []
    if(int(json_response['total'])==0):
        return render_template("alerts.html",string=("Currently no Alerts for this park"),no_center=True,park=park_name)
    else:
        num = int(json_response['total'])
        if num == 1:
            num =2
        if(num > 50):
            num = 50
        for x in range(0,num-1):
            titles.append(json_response['data'][x]['title'])
            description.append(json_response['data'][x]['description'])
            category = json_response['data'][x]['category']
            if(category == 'Danger'):
                symbols.append("danger.png")
            elif(category == 'Caution'):
                symbols.append("caution_symbol.png")
            elif(category == 'Park Closure'):
                symbols.append("closure.png")
            elif(category == 'Information'):
                symbols.append("info.png")
            else:
                symbols.append("https://federalnewsnetwork.com/wp-content/uploads/2019/05/cropped-7E9AE9B6-1DD8-B71B-0BD2CA3A36AEBEC4-1.png")
        return render_template("alerts.html",alerts=zip(titles, description,symbols),park=park_name)


@app.route('/articles.html', methods = ['GET','POST'])
@app.route('/articles/<park_name>',methods = ['GET','POST'])
def articles(park_name = ""):
    park_name = park_name.replace('"', '')
    json_response = other_query("articles",park_name)

    if(int(json_response['total']) == 0):
        output = "Currently no articles related to this park"
        return render_template("articles.html",string=output,no_articles=True)
    else:
        titles = []
        listingdescriptions = []
        listingimages = []
        urls =[]
        num = int(json_response['total'])
        if num == 1:
            num =2
        if(num > 50):
            num = 50
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
    url_add ="events"
    park_name = park_name.replace('"', '')
    json_response = other_query(url_add,park_name)
    titles = []
    locations = []
    description = []
    category = []
    date_start = []
    recurrence_date_end = []
    regres_info = []
    fees_info = []
    timestart = []
    timeend = []

    if(int(json_response['total'])==0):
        return render_template("events.html",string=("Currently no events for this park"),no_events = True,park=park_name)
    else:
        num = 10
        if (int(json_response['total']) < 10):
            num = int(json_response['total'])
        if (num ==1):
            num =2
        for x in range(0,num-1):
            titles.append(json_response['data'][x]['title'])
            if json_response['data'][x]['location'] == "":
                locations.append("N/A")
            else:
                locations.append(json_response['data'][x]['location'])
            #descriptions from api had paragraph and strong tags in response, these lines remove them
            des = json_response['data'][x]['description']
            des = re.sub("<.*?>", " ", des)
            description.append(des)

            category.append(json_response['data'][x]['category'])
            date_start.append(json_response['data'][x]['datestart'])
            timestart.append(json_response['data'][x]['times'][0]['timestart'])
            timeend.append(json_response['data'][x]['times'][0]['timeend'])


            if(json_response['data'][x]['isrecurring'] == "true"):
                recurrence_date_end.append(json_response['data'][x]['recurrencedateend'])
            else:
                recurrence_date_end.append("Not a recurring event")

            if(json_response['data'][x]['isfree'] == "false"):
                fees_info.append(json_response['data'][x]['feeinfo'])
            else:
                fees_info.append("No fees Required")

            if(json_response['data'][x]['isregresrequired'] == "true"):
                regres_info.append(json_response['data'][x]['regresinfo'])
            else:
                regres_info.append("No registration required")

        return render_template("events.html",events=zip(titles,locations, description,category,date_start,recurrence_date_end,fees_info,regres_info,timestart,timeend),park=park_name)

@app.route('/news_releases.html')
@app.route('/news_releases/<park_name>',methods = ['GET','POST'])
def news_releases(park_name = ""):
    url_add ="newsreleases"
    park_name = park_name.replace('"', '')
    json_response = other_query(url_add,park_name)
    titles = []
    release_dates= []
    images= []
    urls = []
    abstracts = []
    if(int(json_response['total'])==0):
        return render_template("news_releases.html",string=("Currently no News Releases for this park"),no_releases=True,park= park_name)
    else:
        num = int(json_response['total'])
        if num == 1:
            num=2
        if(num > 50):
            num = 50
        for x in range(0,num-1):
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
    url_add ="lessonplans"
    park_name = park_name.replace('"', '')
    json_response = other_query(url_add,park_name)
    if(int(json_response['total'])==0):
        return render_template("education.html",string=("Currently no News Releases for this park"),no_resources=True,park= park_name)
    else:
        titles = []
        subjects= []
        grade_levels= []
        question_objectives = []
        durations = []
        urls = []

        num = int(json_response['total'])
        if num == 1:
            num =2
        if num > 50:
            num = 50
        for x in range(0,num-1):
            titles.append(json_response['data'][x]['title'])
            subjects.append(json_response['data'][x]['subject'])
            grade_levels.append(json_response['data'][x]['gradelevel'])
            question_objectives.append(json_response['data'][x]['questionobjective'])
            durations.append(json_response['data'][x]['duration'])
            urls.append(json_response['data'][x]['url'])

        return render_template("education.html",lesson_plans=zip(titles,subjects,grade_levels,question_objectives,durations,urls),park=park_name)

@app.route('/campgrounds.html', methods = ['GET','POST'])
@app.route('/campgrounds/<park_name>',methods = ['GET','POST'])
def campgrounds(park_name = ""):
    park_name = park_name.replace('"', '')
    json_response = other_query("campgrounds",park_name)

    titles = []
    descriptions = []
    regulations = []
    campsites = []
    directions = []

    if(int(json_response['total'])==0):
        return render_template("campgrounds.html",string=("Currently no Campgrounds for this park"),no_camps=True,park= park_name)

    else:
        num = int(json_response['total'])
        if num == 1:
            num =2
        if num > 50:
            num = 50
        for i in range(0,num-1):
            titles.append(json_response['data'][i]['name'])
            descriptions.append(json_response['data'][i]['description'])
            regulations.append(json_response['data'][i]['regulationsoverview'])
            campsites.append(json_response['data'][i]['campsites']['totalsites'])
            directions.append(json_response['data'][i]['directionsoverview'])

        return render_template("/campgrounds.html",campgrounds = zip(titles,descriptions,regulations,campsites,directions),park=park_name)

@app.route('/visitorcenters.html', methods = ['GET','POST'])
@app.route('/visitorcenters/<park_name>',methods = ['GET','POST'])
def visitorcenters(park_name = ""):
    park_name = park_name.replace('"', '')
    json_response = other_query("visitorcenters",park_name)

    if(int(json_response['total'])==0):
        return render_template("visitor_centers.html",string=("Currently no Visitor Centers for this park"),no_centers=True,park= park_name)

    else:
        titles = []
        descriptions = []
        directions = []
        urls = []

        num = int(json_response['total'])
        if num == 1:
            num =2
        if num > 50:
            num = 50

        for i in range(0,num-1):
            titles.append(json_response['data'][i]['name'])
            descriptions.append(json_response['data'][i]['description'])
            directions.append(json_response['data'][i]['directionsInfo'])
            urls.append(json_response['data'][i]['url'])

        return render_template("/visitorcenters.html",visitor_centers = zip(titles,descriptions,directions,urls),park=park_name)

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
        if(json_response['entranceFees']):
            entrance_cost = json_response['entranceFees'][0]['cost'].replace("0000","00")
            entrance_description = json_response['entranceFees'][0]['description']
            #print(entrance_fees['cost'].replace("0000","00"))
        else:
            entrance_cost = "N/A"
            entrance_description = ""
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


        return render_template("/park_info.html",park_code=park_code,name=park_name,designation=designation,description=description,directionsInfo = directionsInfo,
        directionsUrl= directionsUrl,url=url,weatherInfo=weatherInfo,monday=monday,tuesday=tuesday,wednesday=wednesday,thursday=thursday,
        friday=friday,saturday=saturday,sunday=sunday,image=image,caption=img_caption,entrance_cost = entrance_cost,entrance_description=entrance_description,passes=entrance_passes)
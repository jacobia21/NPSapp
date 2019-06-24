from flask import Flask, render_template,request #neccesary for Flask web app, also allows to request data from NPS api
from flask_sqlalchemy import SQLAlchemy         #imported for database use
from lists import *                             #returns list of all parks, and dictionery that stores state abbreviations and states as keys and vales, respectively
from queries import *                           #imports all query functions from queries.py
import re                                       #used in def events() to remove html tags from json response

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

#homepage route
@app.route('/')
def home():
    return render_template("homepage.html")

#route to interactive map
@app.route('/interactive_map')
def interactive_map():
    return render_template("interactive_map.html")

#route to list of states
@app.route('/state_list_homepage')
def state_list_homepage():
    return render_template("state_list_homepage.html")

#route to list of parks in specific state
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

#route to a list of parks by specific designation
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

#route to enter searches and return parks for specific search
@app.route('/search',methods=['GET','POST'])
def search():
    #takes user to search homepage to begin searching
    if request.method == "GET":
        return render_template("search.html", no_search=True)

    else:
        #calls search_query from queries.py to get results of search
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

#route to alerts page for specific park
@app.route('/alerts/<park_name>',methods = ['GET','POST'])
def alerts(park_name = ""):
    #calls other_query from queries.py to get alerts for specific park
    url_add ="alerts"
    park_name = park_name.replace('"', '')
    json_response = other_query(url_add,park_name)

    #if there are no alerts returned from the query, print this string
    if(int(json_response['total'])==0):
        return render_template("alerts.html",string=("Currently no Alerts for this park"),no_center=True,park=park_name)

    #if there are alerts, return the title, description, category, and symbol for each alert
    else:
        titles = []
        description = []
        symbols = []
        num = int(json_response['total'])
        if num == 1:
            num =2
        if(num > 50):
            num = 50
        for x in range(0,num-1):
            titles.append(json_response['data'][x]['title'])
            description.append(json_response['data'][x]['description'])
            category = json_response['data'][x]['category']
            #adds specific symbol to an alert, based off its category
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


#route for articles for specific park
@app.route('/articles/<park_name>',methods = ['GET','POST'])
def articles(park_name = ""):
    park_name = park_name.replace('"', '')
    json_response = other_query("articles",park_name) #query to find articles related to selected park

    #if there are no parks returned from the query, this string will be displayed
    if(int(json_response['total']) == 0):
        output = "Currently no articles related to this park"
        return render_template("articles.html",string=output,no_articles=True)

    #if there are article, the title, description, image, and url of each article will be gathered and sent to the articles html page
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
            #some articles did not have images in the json, so the nps logo was stored as its image
            if json_response['data'][i]['listingimage']['url'] != "":
                listingimages.append(json_response['data'][i]['listingimage']['url'])
            else:
                listingimages.append("https://federalnewsnetwork.com/wp-content/uploads/2019/05/cropped-7E9AE9B6-1DD8-B71B-0BD2CA3A36AEBEC4-1.png")
            urls.append(json_response['data'][i]['url'])

        return render_template("/articles.html",articles=zip(titles,listingdescriptions,listingimages,urls),park=park_name)



#route for events for specific park
@app.route('/events/<park_name>',methods = ['GET','POST'])
def events(park_name = ""):
    url_add ="events"
    park_name = park_name.replace('"', '')
    json_response = other_query(url_add,park_name)

    #if no parks returns query, output this string
    if(int(json_response['total'])==0):
        return render_template("events.html",string=("Currently no events for this park"),no_events = True,park=park_name)
    #iif there are parks, collect information and send to events html page
    else:
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

            #check to see if the event is recurring or not
            if(json_response['data'][x]['isrecurring'] == "true"):
                recurrence_date_end.append(json_response['data'][x]['recurrencedateend'])
            else:
                recurrence_date_end.append("Not a recurring event")

            #check to see if the event is free or not
            if(json_response['data'][x]['isfree'] == "false"):
                fees_info.append(json_response['data'][x]['feeinfo'])
            else:
                fees_info.append("No fees Required")

            #check to see if the event requires registration
            if(json_response['data'][x]['isregresrequired'] == "true"):
                regres_info.append(json_response['data'][x]['regresinfo'])
            else:
                regres_info.append("No registration required")

        return render_template("events.html",events=zip(titles,locations, description,category,date_start,recurrence_date_end,fees_info,regres_info,timestart,timeend),park=park_name)

#route to news releases for specific park
@app.route('/news_releases/<park_name>',methods = ['GET','POST'])
def news_releases(park_name = ""):
    url_add ="newsreleases"
    park_name = park_name.replace('"', '')
    json_response = other_query(url_add,park_name)

    #if there are no parks returned from the query, this string is displayed
    if(int(json_response['total'])==0):
        return render_template("news_releases.html",string=("Currently no News Releases for this park"),no_releases=True,park= park_name)

    #otherwise, collect information for each returned release and send it to news release html page
    else:
        titles = []
        release_dates= []
        images= []
        urls = []
        abstracts = []
        num = int(json_response['total'])
        if num == 1:
            num=2
        if(num > 50):
            num = 50
        for x in range(0,num-1):
            titles.append(json_response['data'][x]['title'])
            release_dates.append(json_response['data'][x]['releasedate'])

            #some releases did not have images in the json, so the nps logo was stored as its image
            if(json_response['data'][x]['image']['url'] == ""):
                images.append("https://federalnewsnetwork.com/wp-content/uploads/2019/05/cropped-7E9AE9B6-1DD8-B71B-0BD2CA3A36AEBEC4-1.png")
            else:
                images.append(json_response['data'][x]['image']['url'])

            urls.append(json_response['data'][x]['url'])
            abstracts.append(json_response['data'][x]['abstract'])
        return render_template("news_releases.html",releases=zip(titles, release_dates,images,urls,abstracts),park=park_name)

#route to lesson plane for specific park
@app.route('/education/<park_name>',methods = ['GET','POST'])
def education(park_name = ""):
    url_add ="lessonplans"
    park_name = park_name.replace('"', '')
    json_response = other_query(url_add,park_name)

    #if there are no lesson plans returned for the park, display this string
    if(int(json_response['total'])==0):
        return render_template("education.html",string=("Currently no Educational Resources for this park"),no_resources=True,park= park_name)

    #otherwise, gather information for each lesson plan and send it to the education html page
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

#route to campground information near specified park
@app.route('/campgrounds/<park_name>',methods = ['GET','POST'])
def campgrounds(park_name = ""):
    park_name = park_name.replace('"', '')
    json_response = other_query("campgrounds",park_name)

    #if there are no campgrounds returned from the query, this string is displayed
    if(int(json_response['total'])==0):
        return render_template("campgrounds.html",string=("Currently no Campgrounds for this park"),no_camps=True,park= park_name)

    #otherwise, gather title, description, regulations, campsires, and directions for each campground
    else:
        titles = []
        descriptions = []
        regulations = []
        campsites = []
        directions = []
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

        #returns any campground information for campgrounds near specific park
        return render_template("/campgrounds.html",campgrounds = zip(titles,descriptions,regulations,campsites,directions),park=park_name)

#route to visitor centers for specified park
@app.route('/visitorcenters/<park_name>',methods = ['GET','POST'])
def visitorcenters(park_name = ""):
    park_name = park_name.replace('"', '')
    json_response = other_query("visitorcenters",park_name)

    #if there are no visitor centers for specified park , display this string
    if(int(json_response['total'])==0):
        return render_template("visitorcenters.html",string=("Currently no Visitor Centers for this park"),no_centers=True,park= park_name)

    #otherwise, gather title, description, direction, and url for each visitor center
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

        for i in range(num-1):
            titles.append(json_response['data'][i]['name'])
            descriptions.append(json_response['data'][i]['description'])
            directions.append(json_response['data'][i]['directionsInfo'])
            urls.append(json_response['data'][i]['url'])

        #returns info on any visitor centers for specific park
        return render_template("/visitorcenters.html",visitor_centers = zip(titles,descriptions,directions,urls),park=park_name)

#route to page with information on a selected park
@app.route('/park_info/<park_name>',methods=['GET','POST'])
def park_info(park_name =""):
        #stores basic information for selected park
        park_name = park_name.replace('"', '')
        json_response = parks_query("",park_name)
        park_code = json_response['parkCode']
        designation = json_response['designation']
        description =  json_response['description']
        directionsInfo = json_response['directionsInfo']
        directionsUrl = json_response['directionsUrl']
        url = json_response['url']
        weatherInfo = json_response['weatherInfo']

        #stores title, cost, and description of all entrance fees and entrance passes for park, if any
        if(json_response['entranceFees']):
            entrance_fees = json_response['entranceFees']
        else:
            entrance_fees = [{
                                "cost":"",
                                "description": "",
                                "title": "N/A"
                            }]

        if(json_response['entrancePasses']):
            entrance_passes = json_response['entrancePasses']
        else:
            entrance_passes =[{
                                "cost":"",
                                "description": "",
                                "title": "N/A"
                            }]

        #checks to see if there are operating hours listed for park, stores information if there are, stores "No Hours Listed" if not
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

        #checks to see if there is an image for the selected park. if not, stores nps logo as selected park's image
        try:
            image = json_response['images'][0]['url']
            img_caption = json_response['images'][0]['caption']
        except IndexError:
            image = "https://federalnewsnetwork.com/wp-content/uploads/2019/05/cropped-7E9AE9B6-1DD8-B71B-0BD2CA3A36AEBEC4-1.png"
            img_caption = "No Pictures Were Available"

        #returns a lot of information for a specific park, used in park_info html page
        return render_template("/park_info.html",park_code=park_code,name=park_name,designation=designation,description=description,directionsInfo = directionsInfo,
        directionsUrl= directionsUrl,url=url,weatherInfo=weatherInfo,monday=monday,tuesday=tuesday,wednesday=wednesday,thursday=thursday,
        friday=friday,saturday=saturday,sunday=sunday,image=image,caption=img_caption,entrance_fees = entrance_fees, entrance_passes= entrance_passes)
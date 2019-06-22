from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from lists import parks, states
from queries import *


app = Flask(__name__)

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
    if state_code is "":
        return render_template("state_list_homepage.html")
    else:
        json_response =parks_query(state_code,"")
        output=[]
        for x in range(0,int(json_response['total'])-1):
            output.append(json_response['data'][x]['fullName'])
        state_code=state_code.upper().lstrip()
        state = states[state_code]

        return render_template("/iparks_by_state.html",output=output,state=state,state_code=state_code)


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
        if designation == "National Cemetery":
            designation = "National Cemeterie"
        return render_template("/designation.html",output=output,designation = designation)

@app.route('/alerts',methods=['GET','POST'])
@app.route('/alerts/<park_name>',methods = ['GET','POST'])
def alerts(park_name = ""):
    if(park_name == ""):
        return render_template("/alerts.html",homepage=True)
    else:
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
    if(park_name == ""):
        return render_template("/articles.html",homepage=True)
    else:
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
    if(park_name == ""):
        return render_template("/events.html",homepage=True)
    else:
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
                des = des.replace("<p>",'')
                des = des.replace("</p>",'')
                des = des.replace("<strong>.</strong></p>",'.')
                des = des.replace("<strong>.</strong>",'.')
                des = des.replace("<em>",'')
                des = des.replace("</em>",'')
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
    if(park_name == ""):
        return render_template("/news_releases.html",homepage=True)
    else:
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
    if(park_name == ""):
        return render_template("education.html",homepage=True)
    else:
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

@app.route('/name_list/<alphabetChar>',methods=['GET','POST'])
def name_list(alphabetChar):
    alphabetChar = alphabetChar.replace('"','')
    output = []
    names = parks
    for name in names:
        if(name.startswith(alphabetChar)):
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

        vc_info = visitor_center_query(park_code)
        campgrounds = campgrounds_query(park_code)

        return render_template("/park_info.html",park_code=park_code,name=park_name,designation=designation,description=description,directionsInfo = directionsInfo,
        directionsUrl= directionsUrl,url=url,weatherInfo=weatherInfo,visitor_centers = vc_info,monday=monday,tuesday=tuesday,wednesday=wednesday,thursday=thursday,
        friday=friday,saturday=saturday,sunday=sunday,image=image,caption=img_caption,campgrounds=campgrounds,entrance_cost = entrance_cost,entrance_description=entrance_description,passes=entrance_passes)
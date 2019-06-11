from flask import Flask, render_template, request
import urllib.request, json
import requests
def other_query(url_add,park_name,limit):
    url = "https://developer.nps.gov/api/v1/" + url_add
    if (limit == 0):
        querystring = {"q":park_name,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
    else:
        querystring = {"limit":limit,"q":park_name,"api_key":"vb4TG1kgKOIUHOfhy5Zfzs3IB9DC255aVNtUv7Jx"}
    response = requests.request("GET", url, headers=HEADERS, params=querystring)
    json_response = json.loads(response.text)
    return json_response



def park_info(campground_name =""):
        campground_name = campground_name.replace('"', '')
        json_response = other_query("campgrounds",campground_name,0)

        name = json_response['data'][0]['name']
        designation = json_response['data'][0]['designation']
        description =  json_response['data'][0]['description']
        directionsInfo = json_response['data'][0]['directionsInfo']
        directionsUrl = json_response['data'][0]['directionsUrl']
        url = json_response['data'][0]['url']
        weatherInfo = json_response['data'][0]['weatherInfo']

        try:
            monday=(json_response['data'][0]['operatingHours'][0]['standardHours']['monday'])
            tuesday= (json_response['data'][0]['operatingHours'][0]['standardHours']['tuesday'])
            wednesday = (json_response['data'][0]['operatingHours'][0]['standardHours']['wednesday'])
            thursday =(json_response['data'][0]['operatingHours'][0]['standardHours']['thursday'])
            friday=(json_response['data'][0]['operatingHours'][0]['standardHours']['friday'])
            saturday = (json_response['data'][0]['operatingHours'][0]['standardHours']['saturday'])
            sunday =(json_response['data'][0]['operatingHours'][0]['standardHours']['sunday'])
        except IndexError:
            monday = tuesday = wednesday = thursday = friday = saturday = sunday = "No Hours Listed"

        try:
            image = json_response['data'][0]['images'][0]['url']
            img_caption = json_response['data'][0]['images'][0]['caption']
        except IndexError:
            image = "https://federalnewsnetwork.com/wp-content/uploads/2019/05/cropped-7E9AE9B6-1DD8-B71B-0BD2CA3A36AEBEC4-1.png"
            img_caption = "No Pictures Were Available"

        vc_info = visitor_center_query(park_code)

        return render_template("/park_info.html",park_code=park_code,name=park_name,designation=designation,description=description,directionsInfo = directionsInfo,
        directionsUrl= directionsUrl,url=url,weatherInfo=weatherInfo,visitor_centers = vc_info,monday=monday,tuesday=tuesday,wednesday=wednesday,thursday=thursday,
        friday=friday,saturday=saturday,sunday=sunday,image=image,caption=img_caption)

from flask import Flask,render_template
import json
import requests
app=Flask(__name__)

 
def dashboardpage():

   return render_template("dashboard.html") 

def businessapi():
   
   url = "https://news-api14.p.rapidapi.com/top-headlines"

   querystring = {"country":"india","language":"en","pageSize":"10","category":"business"}

   headers = {
	"X-RapidAPI-Key": "25fe4c134cmsh2998c03a51ef787p13796bjsne1b8bb773157",
	"X-RapidAPI-Host": "news-api14.p.rapidapi.com"
   }
 

   response = requests.request("GET", url, headers=headers, params=querystring)
   d=json.loads(response.text)
   dict=d['articles']
   print(dict[0]['title'])
   return render_template("newspage.html",dict=dict)
    
 
def entertainmentapi():
 

   url = "https://news-api14.p.rapidapi.com/top-headlines"

   querystring = {"country":"india","language":"en","pageSize":"10","category":"entertainment"}

   headers = {
      "X-RapidAPI-Key": "25fe4c134cmsh2998c03a51ef787p13796bjsne1b8bb773157",
      "X-RapidAPI-Host": "news-api14.p.rapidapi.com"
   }

   response = requests.request("GET", url, headers=headers, params=querystring)
   d=json.loads(response.text)
   dict=d['articles']
   print(dict[0]['title'])
   return render_template("newspage.html",dict=dict)
 
def technologyapi():

   url = "https://news-api14.p.rapidapi.com/top-headlines"

   querystring = {"country":"india","language":"en","pageSize":"10","category":"technology"}

   headers = {
      "X-RapidAPI-Key": "25fe4c134cmsh2998c03a51ef787p13796bjsne1b8bb773157",
      "X-RapidAPI-Host": "news-api14.p.rapidapi.com"
   }

   response = requests.request("GET", url, headers=headers, params=querystring)
   d=json.loads(response.text)
   dict=d['articles']
   print(dict[0]['title'])
   return render_template("newspage.html",dict=dict)
    

 
def healthapi():
   url = "https://news-api14.p.rapidapi.com/top-headlines"

   querystring = {"country":"india","language":"en","pageSize":"10","category":"health"}

   headers = {
      "X-RapidAPI-Key": "25fe4c134cmsh2998c03a51ef787p13796bjsne1b8bb773157",
      "X-RapidAPI-Host": "news-api14.p.rapidapi.com"
   }

   response = requests.request("GET", url, headers=headers, params=querystring)
   d=json.loads(response.text)
   dict=d['articles']
   print(dict[0]['title'])
   return render_template("newspage.html",dict=dict)
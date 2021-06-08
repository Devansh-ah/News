from django.shortcuts import render,redirect
import requests
# Create your views here.

def index(request):
    # business=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # sports=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # entertainment=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # politics=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=politics&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # health=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # science=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # technology=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # music=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=music&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=9289ff62266d4b389cacb6d84f70d28f).json()
    # data=[business,sports,entertainment,health,politics,science,technology,music,general]
    # return render(request,'index.html',{'data':data})
    top=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    return render(request,'index.html',{'top':top})

def general(request):
    general=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    return render(request,'general.html',{'general':general})

def music(request):
    general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=music&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    return render(request,'music.html',{'music':general})

def sports(request):
    general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    return render(request,'sports.html',{'sports':general})

def entertainment(request):
    general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    return render(request,'entertainment.html',{'entertainment':general})

def technology(request):
    general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    return render(request,'technology.html',{'technology':general})

def science(request):
    general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    return render(request,'science.html',{'science':general})

def politics(request):
    general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=politics&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    return render(request,'politics.html',{'politics':general})

def health(request):
    general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    return render(request,'health.html',{'health':general})

def business(request):
    general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    return render(request,'business.html',{'business':general})
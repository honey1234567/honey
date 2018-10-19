# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.http import HttpResponse
from . import connectionex
from . import friends
#from . import friends
def index(request):
    return render_to_response("blog/bar-chart.html")#initially index.html
def about(request):
    return render_to_response("blog/about.html")
    return render_to_response("blog/contact.html")
    return render_to_response("blog/signup.html")
    return render_to_response("blog/login.html")
    return render_to_response("blog/index.html")
def search(request):
    return render_to_response("blog/search.html")
    return render_to_response("blog/about.html")
    return render_to_response("blog/contact.html")
    return render_to_response("blog/signup.html")
    return render_to_response("blog/login.html")
    return render_to_response("blog/index.html")
def contact(request):
    return render_to_response("blog/contact.html")
    return render_to_response("blog/login.html")
    return render_to_response("blog/signup.html")
    return render_to_response("blog/about.html")
    return render_to_response("blog/index.html")
def flipkart(request):
    return render_to_response("blog/flipkart.html")
    return render_to_response("blog/contact.html")
    return render_to_response("blog/about.html")
    return render_to_response("blog/index.html")
# Create your views here.
def signup(request):
    return render_to_response("blog/signup.html")
    return render_to_response("blog/about.html")
    return render_to_response("blog/contact.html")
    return render_to_response("blog/index.html")
    return render_to_response("blog/login.html")
def login(request):
    return render_to_response("blog/login.html")
    return render_to_response("blog/signup.html")
    return render_to_response("blog/about.html")
    return render_to_response("blog/contact.html")
    return render_to_response("blog/index.html")
def saveTest(request):
   e = request.GET['email']
   p = request.GET['psw']
   s = connectionex.saveData(e,p)
   '''  
   flag=0
   for row in o:
      for col in row:
          if col==e:
           return HttpResponse("unsucessful signup")
   else:
       connectionex.saveData(e,p)
 '''
#return HttpResponse(" sucessful signup")

def showTest(request):

    e = request.GET['email']
    p = request.GET['psw']
    o=connectionex.showTest(e,p)
    t=connectionex.showanalyzedata()
    s5=connectionex.rating()

    return render_to_response("blog/flipkart.html",{'data':o,'data1':t,'data2':s5})
def showcrawldata(request):
    e = request.GET['s1']
    o=connectionex.savecrawldata(e)

    return render_to_response("blog/search.html",{'data':o})
   
#def showfriends(request):
 #   o=friends.frndz()
  #  t=friends.frndz1()
   # return render_to_response("blog/bar-chart.html",{'data':o,'data1':t})
def home(request):
    return render_to_response("blog/home.html")
    return render_to_response("blog/about.html")
    return render_to_response("blog/contact.html")
    return render_to_response("blog/index.html")

def saveTest1(request):

    n = request.GET['name']
    s = friends.frndz1(n)
    #s = [[u'user1','100'],[u'user2','120'],[u'user3','40'],[u'user4','60']]

    return HttpResponse(s)  

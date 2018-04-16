# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . import models
from django.template import loader
import json
from django.core import serializers
import logging
from django.http import HttpResponseRedirect 
from django.core.urlresolvers import reverse  
from django.shortcuts import redirect 
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def index(request):
	#return HttpResponse("Hello,my first web index ")
	#latest_question_list = models.Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('login.html')
	#context = {'latest_question_list':latest_question_list}
	#context={}
	#return HttpResponse(template.render(context,request))
	para = {"findit":True,"username":'',"password":''}
	
	return render(request,'login.html',{'para':json.dumps(para)})

def login(request):
	
	try:
		uname = request.POST['username']
		password = request.POST['password']
		
		#find
		if(models.User.objects.filter(username=uname).count()==0):
			para = {"findit":False,"username":uname,"password":password}
			return render(request,'login.html',{'para':json.dumps(para)})
		else:
			request.session["username"]=uname
			request.session.set_expiry(0) 
			return redirect(reverse('didi', args=[]))
	except :
		para = {"findit":True,"username":'',"password":''}
		return render(request,'login.html',{'para':json.dumps(para)})
		

def verify(request):
	template = loader.get_template('validate.html')
	return HttpResponse(template.render({},request))

def registor(request):
	uname = request.POST['username']
	password = request.POST['password']
	models.User.objects.create(username=uname, userpwd=password)
	return redirect(reverse('login', args=[]))
	
def detail(request,question_id):
	latest_question_list = models.Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)

def didi(request):
	#LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
	#logging.basicConfig(filename='myfirstweb.log', level=logging.ERROR, format=LOG_FORMAT)
	#logging.error("dddddddddddddddddddddddddddddd")
	Drivers = models.Driver.objects.all()
	template = loader.get_template('didi.html')
	context = {'Drivers':Drivers}
	
	return HttpResponse(template.render(context,request))
	
	#data = serializers.serialize("json", Drivers)
	#return render(request, 'didi.html', {
	#            'Drivers': json.dumps(data)
	#        })

def driver(request,driver_id):
	dr = get_object_or_404(models.Driver, pk=driver_id)
	return HttpResponse(dr.driver_name)
	
def blog(request):
	
	Blogs = models.Blog.objects.all()
	template = loader.get_template('blog.html')
	context = {'Blogs':Blogs}
	
	return HttpResponse(template.render(context,request))

def publish(request):
	template = loader.get_template('publish.html')
	return HttpResponse(template.render({},request))

def uploadpic(request):
	if request.method == 'POST':
		file_obj = request.FILES.get('picture')
		f = open(os.path.join(BASE_DIR, 'polls/static', 'pic', file_obj.name), 'wb')

		for chunk in file_obj.chunks():
			f.write(chunk)
		f.close()
		pic = '/static/pic/'+file_obj.name
		return HttpResponse(pic)
	
def publishblog(request):
	if request.method == 'POST':
		blogtitle = request.POST['publishtitle']
		blogcontent = request.POST['publishcontent']
		models.Blog.objects.create(blogtitle=blogtitle, blogcontent=blogcontent)
		return redirect(reverse('blog', args=[]))
		
	
def comment(request,comment_id):
	LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
	#logging.basicConfig(filename='myfirstweb.log', level=logging.ERROR, format=LOG_FORMAT)
	
	
	#logging.error("trace into comment")
	cm = models.Comment.objects.get(pk=comment_id)
	#cm = get_object_or_404(models.Comment, pk=comment_id)
	cm.comment_num +=1
	cm.save()
	rsp = HttpResponse(cm.comment_text)
	#rsp.addHeader('Access-Control-Allow-Origin:*')
	#rsp.addHeader('Access-Control-Allow-Method:POST,GET')
	#logging.error(str(rsp))
	return rsp

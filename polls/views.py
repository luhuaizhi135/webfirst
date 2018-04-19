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
from django.db import transaction
from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext

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
		if(models.User.objects.filter(username=uname,userpwd=password).count()==0):
			para = {"findit":False,"username":uname,"password":password}
			return render(request,'login.html',{'para':json.dumps(para)})
		else:
			request.session["username"]=uname
			request.session.set_expiry(0) 
			return HttpResponseRedirect("/blog/?pg=1&searchval=")
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

def report(request):
	template = loader.get_template('report.html')
	return HttpResponse(template.render({},request))
	
def blog(request):
	if request.method=='GET':
		pg = request.GET.get('pg')
		searchcondition = request.GET.get('searchval')
		
		
		
		av_page=3
		#Blogs = models.Blog.objects.all()
		if searchcondition=='':
			request.session["searchcondition"] = ''
			Blogs = models.Blog.objects.order_by("-blogdate")
		else:
			request.session["searchcondition"] = searchcondition
			Blogs = models.Blog.objects.filter(blogtitle__contains=searchcondition).order_by("-blogdate")
		request.session.set_expiry(0) 
			
		template = loader.get_template('blog.html')
		
		start_pg = (int(pg)-1)*av_page
		end_pg = (int(pg)-1)*av_page+av_page
		
		if Blogs.count()%av_page == 0:
			total_pg = int(Blogs.count()/av_page)
		else:
			total_pg = int(Blogs.count()/av_page)+1
		
		context = {'Blogs':Blogs[start_pg:end_pg],'cur_page':pg,'total_pg':total_pg,'av_page':av_page}
		
		return HttpResponse(template.render(context,request))

def showblog(request):
	if request.method=='GET':
		blogid = request.GET.get('blogid')
		blog = get_object_or_404(models.Blog, pk=blogid)
		template = loader.get_template('showblog.html')
		context = {'blog':blog}
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
	sid = transaction.savepoint()
	try:
		if request.method == 'POST':
			blogtitle = request.POST['publishtitle']
			blogcontent = request.POST['publishcontent']
			models.Blog.objects.create(blogtitle=blogtitle, blogcontent=blogcontent)
			transaction.savepoint_commit(sid)
			#return redirect(reverse('blog', args=[1]))
			return HttpResponseRedirect("/blog/?pg=1&searchval=")
		transaction.savepoint_rollback(sid)
	except:
		transaction.savepoint_rollback(sid)
		
def searchblog(request):
	if request.method=='POST':
		searchcondition = request.POST['searchblogcondition']
		Blogs = models.Blog.objects.filter(blogtitle__contains=searchcondition).order_by("-blogdate")
		pg='1'
		av_page=3
		#Blogs = models.Blog.objects.all()
		#Blogs = models.Blog.objects.order_by("-blogdate")
		template = loader.get_template('blog.html')
		
		start_pg = (int(pg)-1)*av_page
		end_pg = (int(pg)-1)*av_page+av_page
		
		if Blogs.count()%av_page == 0:
			total_pg = int(Blogs.count()/av_page)
		else:
			total_pg = int(Blogs.count()/av_page)+1
		
		context = {'Blogs':Blogs[start_pg:end_pg],'cur_page':pg,'total_pg':total_pg,'av_page':av_page}
		
		return HttpResponse(template.render(context,request))
	
		
	
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

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
from django.views.decorators.csrf import csrf_exempt
import re
from pip._vendor.pyparsing import CaselessKeyword
from django.template.loader import render_to_string
#from django.utils.encoding import force_unicode,smart_unicode, smart_str, DEFAULT_LOCALE_ENCODING  


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


def loginsucc(request):
	para = {"findit":True,"username":'',"password":''}
	return render(request,'loginsucc.html',{'para':json.dumps(para)})

def loginpop(request):
	try:
		uname = request.POST['username']
		password = request.POST['password']
		
		#find
		if(models.User.objects.filter(username=uname,userpwd=password).count()==0):
			para = {"findit":False,"username":uname,"password":password}
			return render(request,'loginpop.html',{'para':json.dumps(para)})
		else:
			request.session["username"]=uname
			request.session.set_expiry(0) 
			
			#para = {"findit":True,"username":uname}
			template = loader.get_template('loginsucc.html')
			#return HttpResponse(template.render(para,request))
		
			context = {'username':uname}
			return HttpResponse(template.render(context,request))

	except :
		para = {"findit":True,"username":'',"password":''}
		return render(request,'loginpop.html',{'para':json.dumps(para)})

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
			#return HttpResponseRedirect("/blog/?pg=1&searchval=")
			return HttpResponseRedirect("/loginsucc")
	except :
		para = {"findit":True,"username":'',"password":''}
		return render(request,'login.html',{'para':json.dumps(para)})

def logout(request):
	request.session.delete("session_key")	
	request.session.clear()
	para = {"findit":True,"username":'',"password":''}
	return HttpResponseRedirect("/")	

def verify(request):
	#template = loader.get_template('validate.html')
	template = loader.get_template('addnewuser.html')
	return HttpResponse(template.render({},request))

def registor(request):
	DebugLog("trace into registor")
	if request.method=='GET':
		uname = request.GET['username']
		password = request.GET['password']
		#repeatpassword = request.GET['repeatpassword']
	else:
		uname = request.POST['username']
		password = request.POST['password']
		#repeatpassword = request.POST['repeatpassword']
	
	DebugLog(uname)
	DebugLog(password)
	#DebugLog(repeatpassword)
	
	if (models.User.objects.filter(username=uname).count()!=0):
		return HttpResponse('fail')
		#return HttpResponseRedirect("/verify")
	else:
		models.User.objects.create(username=uname, userpwd=password)
		#return redirect(reverse('loginpop', args=[]))
		return HttpResponse('ok')
	
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

def genreportmenu(request):
	
	if request.method=='GET':

		menu_dic = {"电力":"ElictricDic","暖通":"CoolingstationDic","消防":"FireProtectionDic","设施":"infrastructureDic"}
		menu_1 = request.GET.get('menu_1')
			
		menus = []

		fun_model = "models."+	menu_dic[menu_1] + 	".objects.all()"
		#models.User.objects.filter(username=uname)
		menu_model = eval(fun_model)
		for menu in menu_model:
			menus.append(menu.menu_item)		
					
		return HttpResponse(json.dumps({"elictric_menu":menus}))
		#return HttpResponse(json.dumps(data))

def updateuserright(request):
	if request.method=='POST':
		DebugLog("===================================================================")
		DebugLog(request.POST)
		DebugLog("===================================================================")
		usersupdate = json.loads(request.POST['aaa'])
		DebugLog(usersupdate)
		DebugLog("===================================================================")
		menu_1 = request.POST['menu_1']
		menu_2 = request.POST['menu_2']
		
		menu_dic = {"电力":"ElictricDic","暖通":"CoolingstationDic","消防":"FireProtectionDic","设施":"infrastructureDic"}
		fun_model = "models."+	menu_dic[menu_1] + 	'.objects.filter(menu_item="'+menu_2+'")'
		menu_model = eval(fun_model)
		DebugLog(menu_model[0].unvisible_users)
		DebugLog(menu_model[0].readonly_users)
		DebugLog(menu_model[0].rw_users)
		
		unvisible_users=json.loads(menu_model[0].unvisible_users)
		readonly_users=json.loads(menu_model[0].readonly_users)
		rw_users=json.loads(menu_model[0].rw_users)
				
		for user in usersupdate:
			username = user['username']
			checkval = user['checkval']
			if checkval=="unvisibleflg":
				if username in readonly_users:
					readonly_users.remove(username)
				if username in rw_users:
					rw_users.remove(username)
				unvisible_users.append(username)
			if checkval=="readonlyflg":
				if username in unvisible_users:
					unvisible_users.remove(username)
				if username in rw_users:
					rw_users.remove(username)
				readonly_users.append(username)
			if checkval=="rwflg":
				if username in unvisible_users:
					unvisible_users.remove(username)
				if username in readonly_users:
					readonly_users.remove(username)
				rw_users.append(username)
			
			fun_model = "models."+	menu_dic[menu_1] + 	'.objects.filter(menu_item="'+menu_2+'")'
			menu_model = eval(fun_model)
			menu_model.update(unvisible_users=json.dumps(unvisible_users),readonly_users=json.dumps(readonly_users),rw_users=json.dumps(rw_users))
		
	return HttpResponse('ok')
		#users = json.dumps(usersupdate)
		#DebugLog(str(users))

def manageuser(request):
	if request.method=='GET':
		menu_1 = request.GET.get('menu_1')
		menu_2 = request.GET.get('menu_2')
		pg     = request.GET.get('cur_pg')
		cur_user = request.GET.get('cur_user')
		
		menu_dic = {"电力":"ElictricDic","暖通":"CoolingstationDic","消防":"FireProtectionDic","设施":"infrastructureDic"}
		menu_1 = request.GET.get('menu_1')
		fun_model = "models."+	menu_dic[menu_1] + 	'.objects.filter(menu_item="'+menu_2+'")'
		#models.User.objects.filter(username=uname)
		#DebugLog(fun_model)
		menu_model = eval(fun_model)
		
		DebugLog(menu_model[0].unvisible_users)
		DebugLog(menu_model[0].readonly_users)
		DebugLog(menu_model[0].rw_users)
		
		users = models.User.objects.all()
		
		av_page=8
		start_pg = (int(pg)-1)*av_page
		end_pg = (int(pg)-1)*av_page+av_page
		
		if users.count()%av_page == 0:
			total_pg = int(users.count()/av_page)
		else:
			total_pg = int(users.count()/av_page)+1
		
		rsltusers=[]	
		pg_users = users[start_pg:end_pg]
		for u in pg_users:
			if u.username in json.loads(menu_model[0].unvisible_users):
				unvisibleflg = True
			else:
				unvisibleflg = False
				
			if u.username in json.loads(menu_model[0].readonly_users):
				readonlyflg = True
			else:
				readonlyflg = False
				
			if u.username in json.loads(menu_model[0].rw_users):
				rwflg = True
			else:
				rwflg = False
				
			rsltusers.append({"username":u.username,"unvisibleflg":unvisibleflg,"readonlyflg":readonlyflg,"rwflg":rwflg})
		
		html_card = render_to_string('usercard123.html',{"Users":rsltusers,"menu_2":menu_2})	
			
		DebugLog("===================================================================")	
		DebugLog(html_card)	
		DebugLog("===================================================================")
		
		#context = {'rsltusers':rsltusers,'cur_page':pg,'total_pg':total_pg,'av_page':av_page,'usercard':html_card}
		context = {'cur_page':pg,'total_pg':total_pg,'av_page':av_page,'usercard':html_card}
		DebugLog(context)
		return HttpResponse(json.dumps(context))
	
def reportdetail(request):	
	if request.method=='GET':
		menu_1 = request.GET.get('menu_1')
		menu_2 = request.GET.get('menu_2')
		pg     = request.GET.get('cur_pg')
		username = request.GET.get('username')
		
		report_menu = menu_1 + menu_2
		
		av_page=8
		
		
		#DebugLog(report_menu)
		Reports = models.Report.objects.filter(reportmenu=report_menu)
		#DebugLog(str(Reports))
		
		start_pg = (int(pg)-1)*av_page
		end_pg = (int(pg)-1)*av_page+av_page
		
		if Reports.count()%av_page == 0:
			total_pg = int(Reports.count()/av_page)
		else:
			total_pg = int(Reports.count()/av_page)+1
		
		data = serializers.serialize("json", Reports[start_pg:end_pg])
		
		
		
		menu_dic = {"电力":"ElictricDic","暖通":"CoolingstationDic","消防":"FireProtectionDic","设施":"infrastructureDic"}
		fun_model = "models."+	menu_dic[menu_1] + 	'.objects.filter(menu_item="'+menu_2+'")'
		menu_model = eval(fun_model)
		if username in menu_model[0].unvisible_users:
			userrole = "unvisibleflg"
		if username in menu_model[0].readonly_users:
			userrole = "readonlyflg"
		if username in menu_model[0].rw_users:
			userrole = "rwflg"
		
		
		
		context = {'Reports':data,'cur_page':pg,'total_pg':total_pg,'av_page':av_page,'userrole':userrole}
		return HttpResponse(json.dumps(context))
	
	
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
	
def uploadreport(request):
	if request.method == 'POST':
		file_obj = request.FILES.get('file')
		f = open(os.path.join(BASE_DIR, 'polls/static', 'report', file_obj.name), 'wb')

		for chunk in file_obj.chunks():
			f.write(chunk)
		f.close()
		report = '/static/report/'+file_obj.name
		return HttpResponse(report)

def genAbstract(blog):
	tag_list = re.findall('<.*?>',blog)	
	for tag in tag_list:
		blog = blog.replace(tag,'')
		
	return blog
	
def publishblog(request):
	sid = transaction.savepoint()
	try:
		if request.method == 'POST':
			blogtitle = request.POST['publishtitle']
			blogcontent = request.POST['publishcontent']
			blogabstract = genAbstract(blogcontent)
			blogabstract=blogabstract[0:200]+"……"
			models.Blog.objects.create(blogtitle=blogtitle, blogcontent=blogcontent,blogabstract=blogabstract)
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
	

def DebugLog(msg):
	LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
	logging.basicConfig(filename='mydebuglog.log', level=logging.ERROR, format=LOG_FORMAT)
	logging.error(msg)
		
	
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

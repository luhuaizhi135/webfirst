# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . import models
from django.template import loader
import json
from django.core import serializers
import logging

# Create your views here.
def index(request):
	#return HttpResponse("Hello,my first web index ")
	latest_question_list = models.Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('index.html')
	context = {'latest_question_list':latest_question_list}
	return HttpResponse(template.render(context,request))
	
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

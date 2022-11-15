# Messaging system- Python, Django
# Aviya yahav


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from first_app.models import Message
from datetime import datetime
import json 

from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView


def messages(request):
    if request.method=="POST":  #add messages 
        data = json.loads(request.body)
        sender=data["sender"]
        receiver=data["receiver"]
        message=data["message"]
        subject=data["subject"]
        creation_date=datetime.utcnow()
        if sender=="" or receiver=="" or message=="" or subject=="":
            return HttpResponse('Missing data')
        else:
            m=Message(sender=sender,receiver=receiver,message=message,subject=subject,creation_date=creation_date)
            m.save()
            return HttpResponse("Add successfuly")
    elif request.method=="GET": #show all messages
        messages=Message.objects.all().values()
        list_result = [entry for entry in messages]
        return HttpResponse(f'{list_result}')
    else:
        return HttpResponse('The method is not defined')

def show_all_messages_for_username(request,user_id): #Show all messages if receiver=username
    if request.method=="GET":
        messages=Message.objects.filter(receiver = user_id).values()
        list_result = [entry for entry in messages]
        if list_result==[]:
            return HttpResponse(f'There is no messages to show')
        return HttpResponse(f'{list_result}')
    else:
        return HttpResponse('The method is not defined')

def show_unread_messages_for_username(request,user_id): #Show unread messages if receiver=username
    if request.method=="GET":
        messages=Message.objects.filter(Q(receiver=user_id),Q(read=False)).values()
        list_result = [entry for entry in messages]
        if list_result==[]:
            return HttpResponse('There is no messages to show')
        return HttpResponse(f'{list_result}')
    else:
        return HttpResponse('The method is not defined')

def readMessage(request,message_id): #Show message filtered by id
    if request.method=="GET":
        m=Message.objects.filter(id=message_id).values()
        list_result = [entry for entry in m]
        if list_result==[]:
            return HttpResponse('There is no message to show')
        return HttpResponse(f'{list_result}')
    else:
        return HttpResponse('The method is not defined')

def delete_message(request,message_id,user_id): #Delete message filter by id of message and name of username
    if request.method=="DELETE":
        m=Message.objects.filter(Q(id=message_id), Q(receiver=user_id) | Q(sender=user_id)) 
        m1=m.values()
        list_result = [entry for entry in m1]
        if list_result==[]:
            return HttpResponse('No such message was found')
        else:
            m.delete()
            return HttpResponse('Message deleted succesfuly')
    else:
        return HttpResponse('The method is not defined')

class messagesAll(APIView):

    def get(self,request): #show message with login
        m1=Message.objects.filter(receiver=request.user.id).values()
        list_result = [entry for entry in m1]
        return JsonResponse(list_result, safe=False)

    def post(self,request): #write message with login
        data=JSONParser().parse(request)
        receiver=data["receiver"]
        message=data["message"]
        subject=data["subject"]
        creation_date=datetime.utcnow()
        m=Message(sender=request.user.id,receiver=receiver,message=message,subject=subject,creation_date=creation_date)
        m.save()
        return HttpResponse("created succefully")
    
class unreadMessage(APIView):

    def get(self,request): #show message with login
        m1=Message.objects.filter(receiver=request.user.id,read=False).values()
        list_result = [entry for entry in m1]
        return JsonResponse(list_result, safe=False)

class messageOne(APIView):

    def get(self,request,message_id): #show one message if sender/receiver=user.id
        m=Message.objects.filter(Q(id=message_id), Q(receiver=request.user.id) | Q(sender=request.user.id)).values()
        list_result = [entry for entry in m]
        if list_result==[]:
            return HttpResponse('There is no message to show')
        return HttpResponse(f'{list_result}')
    
    def delete(self, request, message_id): #Delete message filter by id of message and name of username
        m=Message.objects.filter(Q(id=message_id), Q(receiver=request.user.id) | Q(sender=request.user.id)) 
        m1=m.values()
        list_result = [entry for entry in m1]
        if list_result==[]:
            return HttpResponse('No such message was found')
        else:
            m.delete()
            return HttpResponse('Message deleted succesfuly')

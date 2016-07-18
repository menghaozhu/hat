from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Room, UserProfile

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def rooms(request):
    latest_room_list = Room.objects.order_by('-time_creation')[:10]
    template = loader.get_template('hat/rooms.html')
    context = RequestContext( request, {'latest_room_list': latest_room_list,})
    return HttpResponse(template.render(context))

def room(request, room_id):
    return HttpResponse("It's room %s" % room_id)

def profile(request, userprofile_id):
    return HttpResponse("You are looking on profile of user %s" %userprofile_id)

def rating(request):
    return HttpResponse("Here will be rating of gamers)") 

def rules(request):
    return HttpResponse("Here you will see the rules of the game!")

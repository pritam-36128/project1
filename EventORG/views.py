from django.shortcuts import render, redirect
from django.urls import path



events = {
        'event1': {
            'title': "event1",
            'description': "description-1"
        },
        'event2' : {
            'title': "event2",
            'description': "description-2"
        },
        'event3': {
            'title': "event3",
            'description': "description-3"
        },
        'event4' : {
            'title': "event4",
            'description': "description-4"
        }
    }
isActivated = False

def home(request):
    isActivated = False
    return render(request, "home.html")

def shareEvent(request, eventID):
    isActivated = True
    return render(request, "home.html", {'isActivated': isActivated, 'event': events[eventID]})

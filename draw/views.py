# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')
def plan(request):
    return render(request, 'draw/plan.html')
def view(request):
    return render(request, 'draw/view.html')
def explore(request):
    return render(request, 'draw/explore.html')
def set(request):
    return render(request, 'draw/set.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })

from re import L
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Room, Topic, Message, EVENT
from .forms import RoomForm,UserForm,MyUserCreationForm


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)
        except:
            messages.error(request, 'User Does Not Exist')
    
        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {'page' : page} 
    return render(request, 'mainApp/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)#to get the user object
            #cleaning the data received
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'An error occured during registration.')
    context = {'form' : form}
    return render(request,'mainApp/login_register.html',context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains = q) | Q(name__icontains = q) | Q(description__icontains = q))
    topics =Topic.objects.all()[0:5]
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains = q))
    context = {'rooms' : rooms, 'topics' : topics, 'room_count' : room_count, 'room_messages' : room_messages}
    return render(request, 'mainApp/home.html', context)

# @login_required(login_url = 'login')
def room(request,pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()#message model -> give us the set of messages that are related to the room
    participants = room.participants.all()
    
    if request.method == "POST":
        if request.user.is_authenticated:
            message = Message.objects.create(
                user = request.user,
                room = room,
                body = request.POST.get('body')
            )
            room.participants.add(request.user)
            return redirect('room', pk = room.id)
        else:
            return redirect('login')
        
    context = {'room': room, 'room_messages':room_messages,'participants':participants}
    return render(request, 'mainApp/room.html', context)

def userProfile(request,pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms':rooms , 'topics':topics, 'room_messages':room_messages}
    return render(request, 'mainApp/profile.html', context)

@login_required(login_url = 'login')
def createRoom(request):
    form = RoomForm
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name = topic_name)#if could not find it will create it, and craeted becomes true
        
        Room.objects.create(
            host = request.user,
            topic = topic,
            name = request.POST.get('name'),
            description = request.POST.get('description')
        )

        # form = RoomForm(request.POST)
        # if form.is_valid(): 
        #     room = form.save(commit = False)
        #     room.host = request.user
        #     room.save()
        return redirect('home')

    context = {'form' : form, 'topics':topics}
    return render(request, 'mainApp/room_form.html', context)

@login_required(login_url = 'login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name = topic_name)#if could not find it will create it, and craeted becomes true
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form' : form, 'topics':topics, 'room':room}
    return render(request, 'mainApp/room_form.html',context)

@login_required(login_url = 'login')
def deleteRoom(request,pk):
    room = Room.objects.get(id = pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'mainApp/delete.html', {'obj': room})


@login_required(login_url = 'login')
def deleteMessage(request,pk):
    message = Message.objects.get(id = pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed here!!')
    
    if request.method == 'POST':
        message.delete()
        return redirect('room' , pk = message.room.id)
    return render(request, 'mainApp/delete.html', {'obj': message})

@login_required(login_url = 'login')
def updateUser(request):
    user = request.user
    form = UserForm(instance = user)

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance = user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk = user.id)
    return render(request, 'mainApp/update_user.html', {'form': form})

def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains = q)
    return render(request, 'mainApp/topics.html',{'topics':topics})

def activityPage(request):
    room_messages = Message.objects.all()
    return render(request, 'mainApp/activity.html',{'room_messages':room_messages})

def schedular1(request):
    dat = EVENT.objects.all()
    return render(request, 'mainApp/schedular/events.html', {
        "data": dat
    })
def schedular2(request):
    if request.method == "POST":
        data = request.POST
        name = data['name']
        purpose = data['purpose']
        date = data['date']
        time = data['time']
        place = data['place']
        link = data['link']
        n = len(EVENT.objects.all())
        d = EVENT(E_id=n+1, name=name, purpose=purpose, date=date,
                  time=time, place=place, link=link)
        d.save()
        dat = EVENT.objects.all()
        return render(request, 'mainApp/schedular/add_event.html', {
            "data": dat
        })
    else:
        return render(request,'mainApp/schedular/add_event.html')
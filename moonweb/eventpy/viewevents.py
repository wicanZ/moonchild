from django.shortcuts import render,redirect ,get_object_or_404
from moonch3api.models import Event
from django.contrib import messages 
from moonweb.eventpy.formevents import EventForm
from django.http import HttpResponse, HttpResponseRedirect ,JsonResponse
from django.urls import reverse



def makeEvent(request):
    context = {}
    template = 'event/createevent.html'

    form = EventForm()
    context['form'] = form
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid() :
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('/event/homeevent')
            
        else:
            messages.info(request, form.errors)
    return render(request , template , context)

def ListEvent(request):
    but = False
    context = dict()
    template = 'event/homeevent.html'
    event = Event.objects.all()
    if event.count() != 0:
        but = True
    
    context['but'] = but
    context['event'] = event
    return render(request , template , context)

def viewEvent(request , id=None):
    context = dict()
    template = 'event/viewevent.html'
    event = Event.objects.get(id=id)
    like = event.total_like()
    context['event'] = event
    context['like']  = like 
    return render(request , template , context)

def deleteEvent(request , id=None ) :
    context = {}
    event = Event.objects.get(id=id)
    context['event'] = event
    template = 'event/deleteevent.html'
    if request.method == 'POST' :
        if request.user == event.user:
            event.delete()
        return redirect('/event/homeevent')

    return render(
        request ,
        template ,
        context,
    )

def editEvent(request , id=None):
    context = {}
    template = 'event/editevent.html'
    event = Event.objects.get(id=id)
    form = EventForm(instance=event)
    context['form'] = form
    if request.user.id == event.user.id:
        if request.method == 'POST' :
            form = EventForm(request.POST , instance=event)
            if form.is_valid() :
                event = form.save(commit=False)
                event.user = request.user
                event.save()
                return HttpResponseRedirect(reverse('viewevent', args=[str(id)]) )
                
            else:
                messages.info(request, form.errors)
    else : return HttpResponse('unauthorized')
    return render(request , template , context)

def likeEvent(request ,id=None ) :
    event = Event.objects.get(id=id)
    if event.likes.filter(id=request.user.id).exists():
        event.likes.remove(request.user)
    else: event.likes.add(request.user)
    return HttpResponseRedirect(reverse('viewevent', args=[str(id)]) )

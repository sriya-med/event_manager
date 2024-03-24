from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Event, Participant
from .forms import EventForm, SignupForm
from django.template import loader


# Create your views here.
def index(request):
    events = Event.objects.all()
    output = ", ".join([e.event_name for e in events])
    return HttpResponse(output)

def event_list(request):
    events = Event.objects.all()
    #template = loader.get_template("events")
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signup = form.save(commit=False)
            signup.user = request.user
            signup.event = event
            signup.save()

            event.participant_count += 1
            event.save()
            return redirect('event_detail', event_id=event_id)
    else:
        form = SignupForm()
    return render(request, 'events/event_detail.html', {'event':event, 'form':form})


@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_create.html', {'form':form})

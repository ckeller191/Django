from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    ''' The home page for learning log. '''
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added') # put a - in front of the variable to make it descending order


    context = {'topics':topics}
    return render(request, 'MainApp/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')

    context = {'topic':topic, 'entries':entries}

    return render(request, 'MainApp/topic.html', context)


#def new_topic(request):



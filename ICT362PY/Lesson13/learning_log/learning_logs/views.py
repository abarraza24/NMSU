from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    """Home Page for Learning Log."""
    
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics"""
    
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic."""

    topic = Topic.objects.get(id=topic_id)
    context = {'topic': topic}

    return render(request, 'learning_logs/topic.html', context)
import asyncio
import json
from django.shortcuts import render
from .forms import ContactForm
from xAPI.twitter_service import TwitterService
from xAPI.config import query_get_all_tweets
from helper import utilies

# Create your views here.

def index(request):
    tweet = TwitterService()
    
    
    if request.method == 'POST': 
        form = ContactForm(request.POST)
        if form.is_valid(): # if data are correct gohead
            response = asyncio.run(tweet.get_all_tweets(query_get_all_tweets))
            tweets_as_json = utilies.convert_to_json(response)

            if tweets_as_json is True:
                print("saved as json")
            form.save()
            form = ContactForm() #after the process make new empty form
    else:
        form = ContactForm()
    
    context = {
        'form' : form
    }
    
    return  render(request, 'home/index.html', context)


def contact(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST)
        if form.is_valid(): # if data are correct gohead
            form.save()
            form = ContactForm() #after the process make new empty form
    else:
        form = ContactForm()
    
    context = {
        'form' : form
    }
    
    return render(request, "home/contact.html", context)
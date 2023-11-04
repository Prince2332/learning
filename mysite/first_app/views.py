from django.shortcuts import render
from django.http.response import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)

# Create your views here.
articles = {
    "sports": "Sports Page",
    "finance": "Finance Page",
    "politics": "Politics Page",
    "games": "Gambaaa",
}


def home(request):
    return HttpResponse("Home")


def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = "No page found for that topic"
        return HttpResponseNotFound(result)


def page_num_view(request, page_num):
    topic_list = list(articles.keys())
    topic = topic_list[page_num]
    return HttpResponseRedirect(topic)

from django.shortcuts import render
from django.http import JsonResponse ,Http404  ,HttpResponse
# Create your views here.


def HomeBlog(request) :
    data= {
        'message' : 'woriking',
    }
    return JsonResponse(data)
    
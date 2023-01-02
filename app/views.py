from django.shortcuts import render

# Create your views here.

def loop(request):

    dict={'n1':'LUCKY','n2':'ARPITA'}

    return render(request,'loop.html',dict)
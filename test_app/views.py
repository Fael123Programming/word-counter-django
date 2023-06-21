from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello, welcome!</h1>')
    context = {
        'name': 'Rafael'        
    }
    return render(request, 'index.html', context)


def counter(request):
    return render(request, 'counter.html');


def words(request):
    text = request.POST['text'].strip()
    words = len(text.split())
    context = {
        'words': words
    }
    return render(request, 'words.html', context)

from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from django.shortcuts import render

def index(request):
    title = "Welcome to my Django App"
    return render(request, 'index.html', {
        'title': title
        })


# Create your views here.
def home(request, username):
    print(username)
    return HttpResponse("<h2>Hola %s</h2>" % username)

def about(request):
    username = "lekyam"
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })


def tasks(request, ):
    tasks = Task.objects.all()
    return render(request, 'tasks.html',{
        'tasks': tasks
    })
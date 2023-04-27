from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
#from django.contrib.auth.decorators import login_required
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def hello(request):
    #return HttpResponse("<h1>Hello </h1>")
    title = "----- Django Course -----"
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = "walter"
    return render(request, 'about.html', {
        'username': username
    })
    
#@login_required
def prueba(request, username):
    print(username)
    return HttpResponse("<h1>usuario %s</h1>" %username)
    #if request.user.is_authenticated:
    #    return HttpResponse("Existe una sesion!")
    #else:
    #    return HttpResponse("No existe una Sesión activa")
    
def project(request):
    
    #proy = Project.objects.create(name="Crear un ERP")
    #proy = Project(name="PINEDA")
    #proy.save()
    #projects = list(Project.objects.all().values())
    #return HttpResponse("Project")
    #return JsonResponse(projects, safe=False)
    
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        "projects": projects
    })

def tasksx(request):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id = id)
    task = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        "tasks": task
    })
    
def tarea(request):
    return HttpResponse("<h1>tarea</h2>")
    
def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })    
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('taskk')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html',{
            "form": CreateNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST['name'])
        return render(request, 'projects/create_project.html',{
          'form': CreateNewProject()  
        })
        
def project_detail(request,id):
    #project = Project.objects.filter(id=id)
    
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })

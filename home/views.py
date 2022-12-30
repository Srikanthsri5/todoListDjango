from django.shortcuts import render, HttpResponse
from home.models import Task
def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        time = request.POST['time']
        ins = Task(taskTitle=title, taskDesc=desc, time=time)
        ins.save()
    
        context = {'success': True}
    return render(request, 'index.html', context)

def task(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)

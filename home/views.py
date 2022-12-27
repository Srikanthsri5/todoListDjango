from django.shortcuts import render, HttpResponse
from home.models import Task
from math import ceil
# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}
    return render(request, 'index.html', context)

def task(request):
    allTasks = Task.objects.all()
    # print(allTasks)
    for item in allTasks:
        print(item.taskDesc)
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)


def searchMatch(query, item):
    if query in item.taskDesc.lower() or query in item.taskTitle.lower():
        return True
    else:
        return False



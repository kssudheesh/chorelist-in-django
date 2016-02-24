from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import ChoreList,Chore

def index(request):
    lists = ChoreList.objects.all()
    return render(request, 'chores/index.html', {'chorelists':lists})

def newlist(request):
    if request.POST:
        list = ChoreList(name=request.POST['name'], due_date=request.POST['duedate'])
        list.save()
        return HttpResponseRedirect("/chores")
    else:
        return render(request, 'chores/newlist.html', {})
    
def newchore(request, chorelist_id):
    if request.POST:
        list = get_object_or_404(ChoreList, pk=chorelist_id)
        chore = Chore(name=request.POST['name'], due_date=request.POST['duedate'], complete=request.POST['complete'])
        chore.chore_list = list
        chore.save()
        return HttpResponseRedirect("/chores/"+chorelist_id)
    else:
        list = get_object_or_404(ChoreList, pk=chorelist_id)
        return render(request, 'chores/newchore.html', {'chorelist':list})

def deletelist(request, chorelist_id):
    list = ChoreList.objects.get(pk=chorelist_id)
    list.delete()
    return HttpResponseRedirect("/chores")
    
def deletechore(request, chorelist_id, chore_id):
    chore = Chore.objects.get(pk=chore_id)
    chore.delete()
    return HttpResponseRedirect("/chores/"+chorelist_id)
    
def detail(request, chorelist_id):
    list = get_object_or_404(ChoreList, pk=chorelist_id)
    return render(request, 'chores/detail.html', {'chorelist':list})    

def choredetail(request, chorelist_id, chore_id):
    list = get_object_or_404(ChoreList, pk = chorelist_id)
    chore = get_object_or_404(Chore, pk = chore_id)
    return render(request, 'chores/choredetail.html',{'chorelist':list, 'chore':chore})    

def updatechore(request, chorelist_id, chore_id):
    chore = get_object_or_404(Chore, pk = chore_id)
    if 'complete' in request.POST:
        chore.complete = True
    else:
        chore.complete = False
    chore.save()
    return HttpResponseRedirect('/chores/'+ chorelist_id + '/chores/' + chore_id)    


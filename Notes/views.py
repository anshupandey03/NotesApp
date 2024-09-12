from django.shortcuts import render, redirect
from .models import Notes
from .forms import notecreationform, editform

# Create your views here.
def Noteshomepage(request):
    note = Notes.objects.all().values()

    context = {'note':note}

    return render(request,'Notes/mainpage.html', context=context)


def  addnote(request):
    form = notecreationform()
    if request.method == "POST":
        form = notecreationform(request.POST)
        
        if form.is_valid():
            
            form.save()
            return redirect('home-idx')
        else:
            return redirect("add-note")
    
    context = {'noteform' : form }

    return render(request, 'Notes/addnotes.html', context=context)
             


def editnote(request,id):
    note = Notes.objects.get(id=id)
    form = editform(instance=note)
    if request.method == "POST": 
        form = editform(request._post, instance=note)         
        if form.is_valid():
            form.save()
            return redirect('home-idx')
        else:
            return redirect("edit-note")
    context = {'edit_form' : form }
    return render(request, 'Notes/editnotes.html', context=context)

def deletenote(request, id):
    note = Notes.objects.get(id=id)

    note.delete()
    return redirect("home-idx")

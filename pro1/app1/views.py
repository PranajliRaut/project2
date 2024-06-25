from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person
# Create your views here.
def add_person(request):
        form = PersonForm()
        if request.method == "POST":
            form =PersonForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect("/v1/person_form.html")

        return render(request,"app1/person_form.html",{"form":form})

def show_person(request,pk=None):
    template_name ="app1/person_list.html"
    queryset = Person.objects.all()
    return render(request,template_name, {"object_list":queryset})

def update_person(request,pk=None):
    template_name ="app1/person_form.html"
    object =Person.objects.get(pk=pk)
    form = PersonForm(instance=object)
    if request.method =="POST":
        form =PersonForm(request.POST,request.FILES,instance=object)
        if form.is_valid():
            form.save()
            return redirect("/v1/person-list/")
    return render(request,template_name,{"form":form})
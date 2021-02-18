from django.shortcuts import render,redirect
from .forms import StudentsForm
from .models import Students, Suhu
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def std(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("index")
            except:
                pass
    else:
        form =  StudentsForm()
    return render(request, 'main/add.html',{'form':form})    

def index(request):
    return render(request, "main/index.html")

def pdata(request):
    print(request.GET.get('sensor1'))
    sensor12 = request.GET['sensor1']
    sensor22 = request.GET['sensor2']
    # sensor12 = request.GET.get(sensor1,'wowow')
    suhu = Suhu(d_suhu=sensor12,d_hum=sensor22)
    #hum = Suhu(d_hum=sensor22)
    suhu.save()
    #hum.save()
    return render(request, "main/index.html")

def view(request):
    studentKu = Students.objects.all()
    return render(request, "main/view.html", {'StudentsKirim':studentKu })

def dele(request, id):
    sdel = Students.objects.get(id=id)
    sdel.delete()
    return redirect('view') 

def edit(request, id):
    sedit = Students.objects.get(id=id)
    return render(request, "main/edit.html", {'StudentsEdit': sedit})

def saveedit(response, id):
    getid = Students.objects.get(id=id)
    if getid in Students.objects.all():
        if response.method == 'POST':
            dataform = StudentsForm(response.POST)
            if dataform.is_valid():
                m = dataform.cleaned_data["sId"]
                n = dataform.cleaned_data["f_name"]
                o = dataform.cleaned_data["l_name"]
                p = dataform.cleaned_data["email"]
                # t = Students(f_name=n)    #namatabel jeung field nu rek diisi
                # t.save()                #simpen ka database
                t = Students.objects.get(id=id)
                t.sId=m
                t.f_name=n
                t.l_name=o
                t.email=p
                t.save()
            return redirect('view')
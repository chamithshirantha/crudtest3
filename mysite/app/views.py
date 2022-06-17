from django.shortcuts import render,redirect
from .models import Info

from django.template import loader


# Create your views here.
from django.http import HttpResponse


def index(request):

    db = Info.objects.all()
    info = {'data':db}

    return render(request,"index.html",info)


def add(request):
    if request.method == 'POST':
        _fname = request.POST['fname']
        _lname = request.POST['lname']

        db = Info(fname=_fname,lname=_lname)
        db.save()
    else:
        return render(request,"add.html")

    return render(request,"add.html")


def delete(request,id):
    db = Info.objects.filter(id=id).delete()
    return redirect('index')

def update(request,id):
    db = Info.objects.get(id=id)
    tem = loader.get_template('update.html')
    info = {
        'data': db,
    }

    if request.method == 'POST':
        _fname = request.POST['first']
        _lname = request.POST['second']

        updb = Info.objects.get(id=id)
        updb.fname = _fname
        updb.lname = _lname
        updb.save()

        return redirect('index')

    return HttpResponse(tem.render(info, request))

from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def index(req):
    forma=Personforma()
    bd=Person.objects.all()
    print(bd)
    print(Person.objects.get(id=1).name)
    for p in Person.objects.all():
        print(p.name, p.age)
    print('******************')
    print(Person.objects.filter(name='Igor'))

    k1=Product.objects.create(title='confeta',price=50.00, company_id=2)
    k2 = Product.objects.create(title='confetaBIG', price=15.00, company_id=2)
    print(k2.company.name)
    shokoladki=Product.objects.filter(company__name='Mars')
    print(shokoladki.values_list())
    data={'forma':forma,'database':bd}
    return render(req,'index.html',context=data)
    pass
def add1(req):
    man=Person()
    man.name='Igor'
    man.age=22
    man.save()#1

    man2=Person.objects.create(name='Vlad',age=13)#2

    return redirect('home')

def create(req):
    if req.POST:
        man = Person()
        man.name = req.POST.get('name1')
        man.age = req.POST.get('age1')
        man.save()#1
        return redirect('home')

def delete(req,id):
    man=Person.objects.get(id=id)
    man.delete()
    return redirect('home')

def edit(req,id):
    man=Person.objects.get(id=id)
    anketa=Personforma()
    data={'forma':anketa}
    if req.POST:
        man.name=req.POST['name1']
        man.age = req.POST['age1']
        man.save()
        return redirect('home')
    else:
        return render(req,'edit.html',context=data)
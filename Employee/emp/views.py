from django.shortcuts import render,redirect
from emp.models import Employee

def home(request):

    k = Employee.objects.all()

    return render(request, 'home.html',{"emp":k})

def emp_details(request,i):

    e = Employee.objects.get(id=i)

    return render(request, 'emp_details.html',{'emp':e})

def add_emp(request):
    if (request.method == 'POST'):
        name = request.POST.get('ename')
        role = request.POST.get('role')
        sal = request.POST.get('sal')
        adrs = request.POST.get('adrs')

        c = Employee.objects.create(name=name, role=role, salary=sal,address=adrs)
        c.save()
        return redirect('emp:home')
    return render(request,"add_emp.html")

def edit_emp(request,k):
    m = Employee.objects.get(id=k)
    if(request.method == 'POST'):
        m.name = request.POST.get('ename')
        m.role = request.POST.get('role')
        m.sal = request.POST.get('sal')
        m.adrs = request.POST.get('adrs')
        m.save()
        return redirect('emp:home')
    return render(request,'edit_emp.html',{"emp":m})

def delete_emp(request,d):
    k = Employee.objects.get(id=d)
    k.delete()
    return home(request)

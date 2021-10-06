from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Employee
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages
from django.db.models import Count, F, Value, Q, Sum, StdDev, Max, Min, Value
from django.db.models.functions import Length, Upper, Concat
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# part1
@login_required(login_url="/accounts/login/")
def employee_list(request):
    users = Employee.objects.all().order_by('personalCode')
    return render(request, 'employees/employee_list.html', {'users': users})


# part2
@login_required(login_url="/accounts/login/")
def add_employee(request):
    if request.method == 'POST':
        form = forms.AddEmployee(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees:list')
    else:
        form = forms.AddEmployee()
    return render(request, 'employees/add_employee.html', {'form': form})


# part 3
@login_required(login_url="/accounts/login/")
def edit_employee(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'employees/edit_employee.html', {'employee': employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'GET':
        form = forms.AddEmployee(instance=employee)
    elif request.method == 'POST':
        form = forms.AddEmployee(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees:list')

    return render(request, 'employees/edit_employee.html', {'employee': employee, 'form': form})


# part 4
@login_required(login_url="/accounts/login/")
def delete_employee(request):
    messages.add_message(request, messages.INFO, 'اگر کد پرسنلی وجود نداشته باشد و یا فیلد خالی باشد دوباره به این صفحه باز خواهید گشت')
    if request.method == "POST":
        dele = request.POST['srh']
        if dele:
            join = Employee.objects.filter(Q(personalCode__icontains=dele))
            if join:
                join.delete()
                return redirect('employees:list')
            else:
                return render(request, 'employees/delete_employee.html')
        else:
            return render(request, 'employees/delete_employee.html')
    else:
        return render(request, 'employees/delete_employee.html')


# part 5
@login_required(login_url="/accounts/login/")
def search_employee(request):
    messages.add_message(request, messages.INFO, 'اگر اطلاعات وارد شده وجود نداشته باشد و یا فیلد خالی باشد دوباره به این صفحه باز خواهید گشت')
    if request.method == "POST":
        sea = request.POST['srh']

        #C=Concat('name', Value(''), 'family')
        if sea:
            join = Employee.objects.filter(Q(name__icontains=sea) | Q(family__icontains=sea) |
                                           Q(age__icontains=sea) | Q(maritialStatus__icontains=sea))

            if join:
                return render(request, 'employees/search_employee.html', {'search': join})
            else:
                return render(request, 'employees/search_employee.html')
        else:
            return render(request, 'employees/search_employee.html')
    else:
        return render(request, 'employees/search_employee.html')


#part 6
@login_required(login_url="/accounts/login/")
def static_queries(request):

    MarriedEmp =  Employee.objects.filter(maritialStatus='married').count()
    SingleEmp =  Employee.objects.filter(maritialStatus='single').count()
    Income1000000 = Employee.objects.filter(income__gte=1000000).count()
    TotalIncome = Employee.objects.aggregate(Sum('income'))['income__sum']
    StdvIncome = round(Employee.objects.aggregate(StdDev('income'))['income__stddev'],1)

    MostIncomeEmp = Employee.objects.aggregate(Max('income'))
    LeastIncomeEmp = Employee.objects.aggregate(Min('income'))
    MAndLIncomeEmp = Employee.objects.filter(Q(income=MostIncomeEmp['income__max']) | Q(income=LeastIncomeEmp['income__min']))

    Info = [ MarriedEmp , SingleEmp , Income1000000, TotalIncome , StdvIncome]

    return render(request,'employees/static_queries.html', {"Info": Info ,"MAndLIncomeEmp" : MAndLIncomeEmp })

#rests

#http://localhost:8000/employees/myget/Mobina(any name)
def list_by_name(request, name):
    emps = get_object_or_404(Employee, name = name)
    data = {"results": {
    "Name": emps.name,
    "Family": emps.family,
    "Phone": emps.phone,
    "Personal Code": emps.personalCode
    }}
    return JsonResponse(data)


#http://localhost:8000/employees/mydel/married/
@method_decorator(csrf_exempt, name='dispatch')
def del_married_emp( request):
    emps = Employee.objects.filter(maritialStatus='married')
    for e in emps:
        e.delete()

    data = {
        'message': 'The operation to delete the married employees was successful'
    }
    return JsonResponse(data)


#http://localhost:8000/employees/mydel/single/
@method_decorator(csrf_exempt, name='dispatch')
def del_single_emp( request):
    emps = Employee.objects.filter(maritialStatus='single')
    for e in emps:
        e.delete()

    data = {
        'message': 'The operation to delete the single employees was successful'
    }
    return JsonResponse(data)


#http://localhost:8000/employees/myupdate/1234/33/
@method_decorator(csrf_exempt, name='dispatch')
def update_income(request,pc,money):
    emps = Employee.objects.get(personalCode = pc)
    emps.income = money
    emps.save()

    data = {
        'message': 'The operation to update income was successful'
    }
    return JsonResponse(data)


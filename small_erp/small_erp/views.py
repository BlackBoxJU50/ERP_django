from logging import error
from django.http import response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
# pyrefly: ignore [missing-import]
from .forms import usersForms, InventoryForm
from service.models import service
def homePage(request)  :
     data ={
         'title':"Home Page",
         'description':"This is the home page of our small ERP system.",
         'module': 
         [{
             'id':1,
             'name':"HRM",
             'description':"This is the description of HRM."
         },
         {
             'id':2,
             'name':"Finance",
             'description':"This is the description of Finance."
         },
          {
             'id':3,
             'name':"Inventory",
             'description':"This is the description of Inventory."
         }]
     }
     return render(request,"index.html",data)


def aboutUs(request):
    return render(request,"about.html")
def course(request):
    return render(request,"course.html")
def finance(request):
    return render(request,"finance.html")
def inventory(request):
    # servicesData= service.objects.all()
    # print(servicesData)
    # # Read values passed via querystring and show them (no DB)
    # name = request.GET.get('name', '')
    # quantity = request.GET.get('quantity', '')
    # price = request.GET.get('price', '')
    # output = None
    # if name or quantity or price:
    #     output = {'name': name, 'quantity': quantity, 'price': price}
    data ={
        'servicesData':service.objects.all().order_by('name')
    }
    return render(request, "inventory.html", data)


def inventory_form(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            params = {'name': data['name'], 'quantity': data['quantity'], 'price': data['price']}
            url = reverse('inventory') + '?' + urlencode(params)
            return redirect(url)
    else:
        initial = {
            'name': request.GET.get('name', ''),
            'quantity': request.GET.get('quantity', ''),
            'price': request.GET.get('price', ''),
        }
        form = InventoryForm(initial=initial)

    return render(request, "inventory_form.html", {'form': form})
def calShow(request):
    c=''
    error = None
    if request.POST.get('num1')=='' or request.POST.get('num2') == '':
        error = "Please provide both values."
    try:
        if request.method=="POST":
            n1= int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=='+':
                c= n1 + n2
            elif opr=='-':
                c= n1 - n2
            elif opr=='*':
                c= n1 * n2
            elif opr=='/':
                c= n1 / n2
            
    except Exception as e:
        return HttpResponse(e)

    return render(request, "sample_cal.html", {'c':c, 'error':error})

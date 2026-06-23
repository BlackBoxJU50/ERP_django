from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
from .forms import usersForms, InventoryForm
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
    # Read values passed via querystring and show them (no DB)
    name = request.GET.get('name', '')
    quantity = request.GET.get('quantity', '')
    price = request.GET.get('price', '')
    output = None
    if name or quantity or price:
        output = {'name': name, 'quantity': quantity, 'price': price}
    return render(request, "inventory.html", {'output': output})


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
    try:
        if request.method=="POST":
            n1= int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=='+':
                c= n1 + n1
                
    except :
        print(e)

    return render(request, "sample_cal.html")

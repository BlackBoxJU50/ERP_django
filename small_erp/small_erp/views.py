from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
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
        # process submitted form values and pass them to inventory view via querystring
        name = request.POST.get('name', '').strip()
        quantity = request.POST.get('quantity', '').strip()
        price = request.POST.get('price', '').strip()

        params = {'name': name, 'quantity': quantity, 'price': price}
        url = reverse('inventory') + '?' + urlencode(params)
        return redirect(url)

    # GET — render the form and allow pre-filling via querystring
    initial = {
        'name': request.GET.get('name', ''),
        'quantity': request.GET.get('quantity', ''),
        'price': request.GET.get('price', ''),
    }
    return render(request, "inventory_form.html", {'initial': initial})

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
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
    if request.method=="GET":
        output = request.GET.get('output')
    
    return render(request,"inventory.html", {'output': output})


def inventory_form(request):
    from django.shortcuts import redirect

    if request.method == 'POST':
        # process submitted form values
        name = request.POST.get('name', '').strip()
        try:
            quantity = int(request.POST.get('quantity') or 0)
        except ValueError:
            quantity = 0
        try:
            price = float(request.POST.get('price') or 0)
        except ValueError:
            price = 0.0
        print(name, quantity, price)
        return redirect('inventory')

    # GET — render the form and allow pre-filling via querystring
    initial = {
        'name': request.GET.get('name', ''),
        'quantity': request.GET.get('quantity', ''),
        'price': request.GET.get('price', ''),
    }
    return render(request, "inventory_form.html", {'initial': initial})

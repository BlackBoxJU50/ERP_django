from django.http import HttpResponse
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
    return render(request,"inventory.html")


def inventory_form(request):
    if request.method == 'POST':
        # read submitted form values
        n = request.POST.get('name', '').strip()
        try:
            q = int(request.POST.get('quantity', 0) or 0)
        except ValueError:
            q = 0
        try:
            p = float(request.POST.get('price', 0) or 0)
        except ValueError:
            p = 0.0
        print(n, p, q)
        from django.shortcuts import redirect
        return redirect('inventory')

    # GET — allow pre-filling via querystring
    initial = {
        'name': request.GET.get('name', ''),
        'quantity': request.GET.get('quantity', ''),
        'price': request.GET.get('price', ''),
    }
    return render(request, "inventory_form.html", {'initial': initial})

from django.http import HttpResponse



def aboutUs(request):
    return HttpResponse("This is the about us page of our small ERP system.")   
def course(request):
    return HttpResponse("This is the course page of our small ERP system.") 
def courseDetails(request, courseid):
    return HttpResponse(courseid)
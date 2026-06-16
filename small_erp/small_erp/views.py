from django.http import HttpResponse



def aboutUs(request):
    return HttpResponse("<b>This is the about us page of our small ERP system.<b>")
def course(request):
    return HttpResponse("This is the course page of our small ERP system.") 
def courseDetails(request, courseid):
    return HttpResponse(courseid)
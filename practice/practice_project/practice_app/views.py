from django.shortcuts import render,HttpResponse



# Create your views here.
def index(request):
    context={
        'name' : 'Anish'
    }
    return render (request , 'index.html', context)
    # return HttpResponse("This is a homepage")    

def services(request):
    return render (request,'services.html' )    


def contact(request):
    return render (request,'contact.html' )   


def about(request):
    return render (request,'about.html' )
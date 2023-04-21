from django.shortcuts import render
from django.http import response

# Create your views here.
def home(request):
    return render(request,"home.html")

def Menu(request):
    return render(request,"Menu.html")

def chef(request):
    return render(request,"chef.html")

def about(request):
    return render(request,"about.html")


from AppMain.models import addBooks

def Book(request):
    
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        date=request.POST['date']
        person=request.POST['person']

       # if name !='' and email !='' and number !='' and date !='' and person!='':
        data=addBooks(name=name,email=email,person=person,date=date,number=number)
        data.save()
            
    
    return render(request,"Book.html")

def contact(request):
    return render(request,"contact.html")



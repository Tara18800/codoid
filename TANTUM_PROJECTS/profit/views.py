from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def casestudies(request):
    return render(request,'casestudies.html')

def career(request):
    return render(request,'career.html')

def contact(request):
    return render(request, 'contact.html')

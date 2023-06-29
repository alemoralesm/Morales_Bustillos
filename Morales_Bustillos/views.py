from django.shortcuts import render



def index(request):
    return render(request, 'app/index.html')

def Nacionales(request):
    return render(request, 'app/Nacionales.html')




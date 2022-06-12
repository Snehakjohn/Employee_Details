from django.shortcuts import render
from django.http import HttpResponse
from .models import Employe
# Create your views here.
def view_employee(request):
	Employeess = Employe.objects.all()
	#return HttpResponse("<h1>HELLO</h1>")
	return render(request,'first.html',{'Employeess':Employeess})
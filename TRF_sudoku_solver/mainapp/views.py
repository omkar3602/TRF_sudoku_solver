from django.shortcuts import render
from . import sudokusolver
# Create your views here.
def home(request):
    return render(request,'index.html')

def api(request):

    sudokusolver.call_solver()

    return render(request,'index.html')

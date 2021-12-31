from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    inquilino = Inquilino.objects.all()
    return render(request, 'cuentas/index.html', {'inquilino': inquilino })

def departamento(request, pk):
    departamento = Departamento.objects.get(id=pk)
    inq = Inquilino.objects.get(id=pk)
    pago = inq.pagos_set.all()
    context = {'departamento': departamento, 'inq': inq, 'pago': pago}
    return render(request, 'cuentas/departamento.html', context)

def inquilino(request):
    inquilino = Inquilino.objects.all()
    return render(request, 'cuentas/inquilinos.html', {'inquilino': inquilino })

def cargarInquilino(request):
    departamento= Departamento.objects.all()
    return render(request, 'cuentas/cargarinquilino.html', {'departamento': departamento})

def cargarDepartamento(request):
    return render(request, 'cuentas/cargardepartamento.html')

def allPosts(request):
    posts = Post.objects.all()
    return {'posts': posts}
from django.shortcuts import render
from ovinogestApp.models import Ovino,Raca,Manejo,Medicamento,Manutencao,Doenca,Historico,Categoria
from ovinogestApp.forms import  OvinoForm,DoencaForm,CategoriaForm,RacaForm,ManejoForm,ManutencaoForm,MedicamentoForm,HistoricoForm

def new_ovino (request):
    form = OvinoForm (request.POST, request.FILES)
    if request.method == "POST":
        form = OvinoForm (request.POST, request.FILES)
        if form.is_valid: 
            ovino = form.save()
            ovino.save()
            form = OvinoForm()
    
    return render (request,"ovino/new_ovino.html",{"form":form})


def adm_ovino (request):
    ovinos = Ovino.objects.all()
    context = {"ovinos":ovinos}
    return render(request,"ovino/adm_ovino.html",context)


def publico_ovino (request):
    ovinos = Ovino.objects.all()
    context = {"ovinos":ovinos}
    return render(request,"ovino/publico_ovino.html",context)
from django.shortcuts import render, redirect, get_object_or_404
from ovinogestApp.models import Ovino,Raca,Manejo,Medicamento,Manutencao,Doenca,Historico,Categoria
from ovinogestApp.forms import  OvinoForm,DoencaForm,CategoriaForm,RacaForm,ManejoForm,ManutencaoForm,MedicamentoForm,HistoricoForm


def home(reuest):
    return render(reuest, 'ovino/home.html')
def new_ovino (request):
    form = OvinoForm()

    if request.method == 'POST':
        form = OvinoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            obj.save()
            form = OvinoForm()  # Redefine o formulário após o salvamento bem-sucedido

    return render(request, 'ovino/new_ovino.html', {'form': form})


def adm_ovino (request):
    ovinos = Ovino.objects.all()
    context = {"ovinos":ovinos}
    return render(request,"ovino/adm_ovino.html",context)

def editar_ovino(request,id):
    ovino =get_object_or_404(Ovino,pk=id)
    form = OvinoForm (instance=ovino)
    ovinos = Ovino.objects.all()
    if request.method == "POST":
        form = OvinoForm (request.POST, request.FILES, instance=ovino)
        if form.is_valid():
           ovino.save()
           return redirect('publico_ovino')

    return render(request,"ovino/editar_ovino.html",{'form': form, 'ovino': ovino, 'ovinos': ovinos})

def publico_ovino (request):
    ovinos = Ovino.objects.all()
    context = {"ovinos":ovinos}
    return render(request,"ovino/publico_ovino.html",context)

def manutencao(request, id):

    ovino =get_object_or_404(Ovino,pk=id)

    mans = Manutencao.objects.all()
    form = ManutencaoForm(instance=ovino)
    if request.method == 'POST':
        form = ManutencaoForm(request.POST, request.FILES)
        if form.is_valid():
            manutencao = form.save()
            manutencao.save()
            return redirect('publico_ovino')
        else:
            return render(request, "ovino/manutencao_ovino.html", {'form': form, 'ovino': ovino, 'mans': mans})
    else:
        return render(request, "ovino/manutencao_ovino.html", {'form': form, 'ovino': ovino, 'mans': mans})


def new_medicamento(request):
    medicamentos =Medicamento.objects.all()
    form = MedicamentoForm()
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, request.FILES)
        if form.is_valid():
            medicamento = form.save()
            medicamento.save()
            form = MedicamentoForm()

    return render(request, "ovino/medicamento_ovino.html", {'form': form, 'medicamentos': medicamentos})




def man(request, id):
    ovino = get_object_or_404(Ovino, pk=id)
    form = ManutencaoForm(instance=ovino)
    mans = Manutencao.objects.all()
    if request.method == 'POST':
        form = ManutencaoForm(request.POST, request.FILES, instance=ovino)
        if form.is_valid():
            manutencao = form.save(commit=False)
            manutencao.ovino = ovino  # Relacione o objeto ao ovino atual
            manutencao.save()

        else:
            print(form.errors)  # Verifique os erros no console
    else:
        form = ManutencaoForm()

    return render(request, "ovino/manutencao_ovino.html", {'form': form, 'ovino': ovino, 'mans': mans})
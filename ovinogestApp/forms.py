from django import forms
from ovinogestApp.models import Doenca,Categoria,Raca,Manejo,Manutencao,Medicamento,Ovino,Historico

class DoencaForm (forms.ModelForm):
    class Meta: 
        model = Doenca 
        fields = "__all__" 
         
class CategoriaForm (forms.ModelForm):
    class Meta: 
        model = Categoria 
        fields = "__all__"
        
class RacaForm (forms.ModelForm):
    class Meta: 
        model = Raca 
        fields = "__all__" 
          
class ManejoForm (forms.ModelForm):
    class Meta: 
        model = Manejo 
        fields = "__all__" 
         
class ManutencaoForm (forms.ModelForm):
    class Meta: 
        model = Manutencao 
        fields = "__all__"
        
class MedicamentoForm (forms.ModelForm):
    class Meta: 
        model = Medicamento 
        fields = "__all__" 
          
class OvinoForm (forms.ModelForm):
    SEXO = [
        ('M', 'M'),
        ('F', 'F'),

    ]

    class Meta: 
        model = Ovino 
        #fields = "__all__",'
        fields = ['foto_ovino','matricula','nome_ovino','sexo_ovino','data_nasc','data_cad','peso_ovino','id_categoria', 'id_raca' ]
    foto_ovino = forms.ImageField(label='Foto:',required=False)
    matricula = forms.CharField(label='Matricula:',required=False)
    nome_ovino = forms.CharField(label='Nome:',required=False)
    sexo_ovino = forms.ChoiceField(
        label='Sexo:',
        choices= SEXO,
        widget=forms.Select(attrs={'class':'custom-select'}),
        initial='F',
    )
    data_nasc= forms.DateField(label='Data de Nascimento:',required=False)
    data_cad= forms.DateField(label='Data de Cadastro:',required=False)
    peso_ovino = forms.DecimalField(
        label="Peso (kg)",
        max_digits=10,
        decimal_places=3,
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001'})
    )

    id_categoria = forms.IntegerField(label='Categoria:',required=False)
    id_raca = forms.IntegerField(label='Raca:',required=False)


         
class HistoricoForm (forms.ModelForm):
    class Meta: 
        model = Historico
        fields = "__all__" 
                
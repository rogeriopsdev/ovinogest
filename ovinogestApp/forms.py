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
    class Meta: 
        model = Ovino 
        fields = "__all__" 
         
class HistoricoForm (forms.ModelForm):
    class Meta: 
        model = Historico
        fields = "__all__" 
                
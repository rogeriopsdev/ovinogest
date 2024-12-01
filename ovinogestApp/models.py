from django.db import models
import PIL
from PIL import Image

class Doenca (models.Model):
    id_doenca = models.AutoField(primary_key=True)
    nome_doenca = models.CharField(max_length =255, null=False)

    def __str__(self):
        return self.nome_doenca


class Medicamento (models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nome_medicamento = models.CharField(max_length =255, null=False)
    def __str__(self):
        return self.nome_medicamento


class Manejo (models.Model):
    id_manejo = models.AutoField(primary_key=True)
    nome_manejo = models.CharField(max_length =255, null=False)

    def __str__(self):
        return self.nome_manejo
    


class Manutencao (models.Model):
    id_manutencao = models.AutoField(primary_key=True)
    nome_manutencao = models.CharField(max_length =255, null=False)
    id_doenca = models.ForeignKey(Doenca, models.DO_NOTHING, db_column='id_doenca', null=True, blank=True)
    id_medicamento = models.ForeignKey(Medicamento, models.DO_NOTHING, db_column='id_medicamento', null=True, blank=True)
    id_manejo = models.ForeignKey(Manejo, models.DO_NOTHING, db_column='id_manejo', null=True,blank=True)

    def __str__(self):
        return self.nome_manutencao


class Categoria (models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length =255, null=False)
    
    def __str__(self):
        return self.nome_categoria


class Raca (models.Model):
    id_raca = models.AutoField(primary_key=True)
    nome_raca = models.CharField(max_length =255, null=False)

    def __str__(self):
        return self.nome_raca


class Ovino (models.Model):
    id_ovino = models.AutoField(primary_key=True)
    foto_ovino = models.ImageField(blank=True, null=True)
    matricula = models.CharField(max_length=20, unique=True, null=False)
    nome_ovino = models.CharField(max_length=255, null=False)
    sexo_ovino = models.CharField (max_length=1, null=False)
    data_nasc = models.DateField(null=False)
    data_cad =models.CharField(max_length=20, null=False)
    peso_ovino =models.DecimalField(max_digits=10,decimal_places=2,null=False)
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria', null=True, blank=True)
    id_raca = models.ForeignKey(Raca, models.DO_NOTHING, db_column='id_raca', null=True, blank= True)

    def save(self):
        super().save()
        im = Image.open(self.foto_ovino.path)
        novo_tamanho = (100, 100)
        im.thumbnail(novo_tamanho)
        im.save(self.foto_ovino.path)

    def foto_url(self):
        if self.foto_ovino and hasattr(self.foto_ovino, 'url'):
            return self.foto_ovino.url
        else:
            return self.nome_ovino

    def __str__(self):
        return self.nome_ovino


class Historico (models.Model):
    id_historico = models.AutoField(primary_key=True)
    nome_historico = models.CharField(max_length=255, null=False)
    data_historico = models.CharField(max_length=20, null=False)
    id_ovino = models.ForeignKey(Ovino, models.DO_NOTHING, db_column='id_ovino', null=True, blank=True) 
    id_manutencao = models.ForeignKey(Manutencao, models.DO_NOTHING, db_column='id_manutencao', null=True, blank=True)

    def __str__(self):
        return self.nome_historico








from django.db import models
import PIL
from PIL import Image
from datetime import datetime


class Doenca(models.Model):
    id_doenca = models.AutoField(primary_key=True)
    nome_doenca = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome_doenca


from django.db import models





class Manejo(models.Model):
    TIPO = [
     ('VAC', 'Vacinação'),
     ('ALI','Alimentação'),
     ('PES', 'Pesagem'),
    ('TRA', 'Tratamento'),
    ('REP', 'Reprodução'),
     ('OUT', 'Outro'),
    ]
    tipo = models.CharField(
        max_length=3,
        choices=TIPO,
        default="VAC",
        verbose_name="Tipo de Manejo"
    )  # Tipo de manejo realizado
    descricao = models.TextField(blank=True, null=True)  # Detalhes adicionais do manejo
    data_manejo = models.DateField()  # Data em que o manejo foi realizado
    responsavel = models.CharField(max_length=255, blank=True, null=True)  # Nome do responsável pelo manejo
    observacoes = models.TextField(blank=True, null=True)  # Observações gerais
    atualizado_em = models.DateTimeField(auto_now=True)  # Data de última atualização

    def __str__(self):
        return self.tipo


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome_categoria


class Raca(models.Model):
    id_raca = models.AutoField(primary_key=True)
    nome_raca = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome_raca


class Ovino(models.Model):
    id_ovino = models.AutoField(primary_key=True)
    foto_ovino = models.ImageField(blank=True, null=True)
    matricula = models.CharField(max_length=20, unique=True, null=False)
    nome_ovino = models.CharField(max_length=255, null=False)
    sexo_ovino = models.CharField(max_length=1, null=False)
    data_nasc = models.DateField(null=False)
    data_cad = models.DateField(null=False)
    peso_ovino = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria', null=True, blank=True)
    id_raca = models.ForeignKey(Raca, models.DO_NOTHING, db_column='id_raca', null=True, blank=True)

    def save(self):
        super().save()
        im = Image.open(self.foto_ovino.path)
        novo_tamanho = (200, 200)
        im.thumbnail(novo_tamanho)
        im.save(self.foto_ovino.path)

    def foto_url(self):
        if self.foto_ovino and hasattr(self.foto_ovino, 'url'):
            return self.foto_ovino.url
        else:
            return self.nome_ovino

    def __str__(self):
        return self.nome_ovino



class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, unique=True)  # Nome do medicamento
    descricao = models.TextField(blank=True, null=True)  # Descrição ou observação
    principio_ativo = models.CharField(max_length=255, blank=True, null=True)  # Componente ativo
    dosagem = models.CharField(max_length=100, blank=True, null=True)  # Ex.: 500mg, 10ml
    forma_farmaceutica = models.CharField(max_length=100, blank=True, null=True)  # Ex.: Comprimido, Líquido
    indicacao = models.TextField(blank=True, null=True)  # Indicações de uso
    contraindicacoes = models.TextField(blank=True, null=True)  # Contraindicações
    modo_de_uso = models.TextField(blank=True, null=True)  # Como administrar o medicamento
    fabricante = models.CharField(max_length=255, blank=True, null=True)  # Nome do fabricante
    lote = models.CharField(max_length=100, blank=True, null=True)  # Lote do medicamento
    validade = models.DateField(blank=True, null=True)  # Data de validade
    estoque_atual = models.PositiveIntegerField(default=0)  # Quantidade em estoque
    unidade_medida = models.CharField(
        max_length=50,
        choices=[
            ('mg', 'Miligrama'),
            ('ml', 'Mililitro'),
            ('un', 'Unidade')
        ],
        default='mg'
    )  # Unidade de medida para estoque
    criado_em = models.DateTimeField(auto_now_add=True)  # Data de criação do registro
    atualizado_em = models.DateTimeField(auto_now=True)  # Data de última atualização

    def __str__(self):
        return self.nome

class Manutencao(models.Model):
    id_manutencao = models.AutoField(primary_key=True)
    id_ovino = models.ForeignKey(Ovino, models.DO_NOTHING, db_column='id_ovino', null=True, blank=True)
    nome_manutencao = models.CharField(max_length=255, null=False)
    desc_manutencao = models.TextField(null=True)
    data_manutencao = models.DateField(null=False)
    id_doenca = models.ForeignKey(Doenca, models.DO_NOTHING, db_column='id_doenca', null=True, blank=True)
    id_medicamento = models.ForeignKey(Medicamento, models.DO_NOTHING, db_column='id_medicamento', null=True,
                                       blank=True)
    id_manejo = models.ForeignKey(Manejo, models.DO_NOTHING, db_column='id_manejo', null=True, blank=True)

    def __str__(self):
        return self.nome_manutencao


class Historico(models.Model):
    id_historico = models.AutoField(primary_key=True)
    nome_historico = models.CharField(max_length=255, null=False)
    data_historico = models.CharField(max_length=20, null=False)
    id_ovino = models.ForeignKey(Ovino, models.DO_NOTHING, db_column='id_ovino', null=True, blank=True)
    id_manutencao = models.ForeignKey(Manutencao, models.DO_NOTHING, db_column='id_manutencao', null=True, blank=True)

    def __str__(self):
        return self.nome_historico

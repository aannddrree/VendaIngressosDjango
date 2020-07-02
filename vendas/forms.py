from django import forms
from vendas.models import Torcedor, Ingresso, Compra


class TorcedorForm(forms.ModelForm):
    class Meta:
        model = Torcedor
        fields = ['cpf', 'nome', 'idade']
        labels = {'cpf': 'CPF', 'nome': 'Nome', 'idade': 'Idade'}


class IngressoForm(forms.ModelForm):
    class Meta:
        model = Ingresso
        fields = ['preco', 'setor', 'clubeA', 'clubeB', 'estadio']
        labels = {'preco': 'Preço', 'setor': 'Setor', 'clubeA': 'Clube A', 'clubeB': 'Clube B', 'estadio': 'Estádio'}


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['torcedor', 'ingresso']
        labels = {'torcedor': 'Torcedor', 'ingresso': 'Ingresso'}

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.fields['ingresso'].queryset = Ingresso.objects.filter(status='Disponível')

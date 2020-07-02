from django.shortcuts import render, redirect
from vendas.models import Torcedor, Ingresso, Compra
from vendas.forms import TorcedorForm, IngressoForm, CompraForm


def menu(request):
    return render(request, 'menu.html')


def list_torcedor(request):
    torcedores = Torcedor.objects.all()
    return render(request, 'torcedor.html', {'torcedores': torcedores})


def create_torcedor(request):
    form = TorcedorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_torcedor')

    return render(request, 'torcedor-form.html', {'form': form})


def update_torcedor(request, id):
    torcedor = Torcedor.objects.get(id=id)
    form = TorcedorForm(request.POST or None, instance=torcedor)

    if form.is_valid():
        form.save()
        return redirect('list_torcedor')

    return render(request, 'torcedor-form.html', {'form': form, 'torcedor': torcedor})


def delete_torcedor(request, id):
    torcedor = Torcedor.objects.get(id=id)

    if request.method == 'POST':
        torcedor.delete()
        return redirect('list_torcedor')

    return render(request, 'torcedor-delete-confirm.html', {'torcedor': torcedor})


def list_ingresso(request):
    ingressos = Ingresso.objects.all()
    return render(request, 'ingresso.html', {'ingressos': ingressos})


def create_ingresso(request):
    form = IngressoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_ingresso')

    return render(request, 'ingresso-form.html', {'form': form})


def update_ingresso(request, id):
    ingresso = Ingresso.objects.get(id=id)
    form = IngressoForm(request.POST or None, instance=ingresso)

    if form.is_valid():
        form.save()
        return redirect('list_ingresso')

    return render(request, 'ingresso-form.html', {'form': form, 'ingresso': ingresso})


def delete_ingresso(request, id):
    ingresso = Ingresso.objects.get(id=id)

    if request.method == 'POST':
        ingresso.delete()
        return redirect('list_ingresso')

    return render(request, 'ingresso-delete-confirm.html', {'ingresso': ingresso})


def list_compra(request):
    compras = Compra.objects.all()
    torcedores = Torcedor.objects.all()
    ingressos = Ingresso.objects.all()

    return render(request, 'compra.html', {'compras': compras, 'torcedores': torcedores, 'ingressos': ingressos})


def create_compra(request):
    form = CompraForm(request.POST or None)

    if form.is_valid():
        idIngresso = int(form.data['ingresso'])
        ingresso = Ingresso.objects.get(id=idIngresso)
        ingresso.status = "Indisponível"
        ingresso.save()
        form.save()
        return redirect('list_compra')

    return render(request, 'compra-form.html', {'form': form})

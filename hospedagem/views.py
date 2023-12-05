from django.shortcuts import render, get_object_or_404, redirect
from .models import Hospedagem
from .forms import HospedagemForm


def hospedagem_editar(request, id):
    hospedagem = get_object_or_404(Hospedagem, id=id)

    if request.method == "POST":
        form = HospedagemForm(request.POST, instance=hospedagem)

        if form.is_valid():
            form.save()
            return redirect("hospedagem_listar")
    else:
        form = HospedagemForm(instance=hospedagem)

    return render(request, "hospedagem/form.html", {"form": form})


def hospedagem_remover(request, id):
    hospedagem = get_object_or_404(Hospedagem, id=id)
    hospedagem.delete()
    # procure um url com o nome 'lista_hospedagem'
    return redirect("hospedagem_listar")


def hospedagem_criar(request):
    if request.method == "POST":
        form = HospedagemForm(request.POST)
        if form.is_valid():
            form.save()
            form = HospedagemForm()
            return redirect("hospedagem_listar")
    else:
        form = HospedagemForm()

    return render(request, "hospedagem/form.html", {"form": form})


def hospedagem_listar(request):
    hospedagens = Hospedagem.objects.all()
    context = {"hospedagens": hospedagens}
    return render(request, "hospedagem/hospedagens.html", context)


def hospedagem_detalhar(request, id):
    hospedagem = get_object_or_404(Hospedagem, id=id)
    context = {"hospedagem": hospedagem}
    return render(request, "hospedagem/detalhar.html", context)


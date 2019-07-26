from django.shortcuts import render
from .models import Pessoa

def mostrar_formulario_cadastro(request):
  if request.method == 'POST':
    pessoa = Pessoa()
    pessoa.nome = request.POST['nome']
    pessoa.cpf = request.POST['cpf']
    pessoa.email = request.POST['email']
    pessoa.telefone = request.POST['telefone']
    pessoa.genero = request.POST['genero']
    pessoa.save()
  return render(request, 'index.html')

def mostrar_pessoas(request):
  pessoas = Pessoa.objects.all()

  return render(request, 'pessoas.html', {'dados': pessoas})
from django.shortcuts import render
from .models import Estacionamento
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    return render(request, "todos/home.html")

class todoListarView(ListView):
    model = Estacionamento
    context_object_name = 'todo_listar'

class todoCriarView(CreateView):
    model = Estacionamento
    fields = ["nomeCliente", "placaVeiculo", "tipoVeiculo", "hrSaida"]
    success_url = reverse_lazy('todo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Cadastrar Cliente '
        return context

class todoAtualizarView(UpdateView):
    model = Estacionamento
    fields = ["nomeCliente", "placaVeiculo", "tipoVeiculo", "hrSaida"]
    success_url = reverse_lazy('todo_listar')

    def form_valid(self, form):
        # Manter o valor original de 'hrEntrada'
        form.instance.hrEntrada = self.get_object().hrEntrada
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Atualizar Cadastro do Cliente'
        return context

class todoDeletarView(DeleteView):
    model = Estacionamento
    success_url = reverse_lazy('todo_listar')
    template_name = "todos/todoConfirmDelete.html"    

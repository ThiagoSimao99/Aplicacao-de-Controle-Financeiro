from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Sum
from datetime import date, timedelta
from .models import Grupo, ContaPagar
from .forms import GrupoForm, ContaPagarForm

# --- GRUPOS ---

class GrupoListView(ListView):
    model = Grupo
    template_name = 'financeiro/grupo_list.html'
    context_object_name = 'grupos'

class GrupoCreateView(CreateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'financeiro/grupo_form.html'
    success_url = reverse_lazy('grupo-list')

class GrupoUpdateView(UpdateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'financeiro/grupo_form.html'
    success_url = reverse_lazy('grupo-list')

class GrupoDeleteView(DeleteView):
    model = Grupo
    template_name = 'financeiro/grupo_confirm_delete.html'
    success_url = reverse_lazy('grupo-list')

class GrupoDetailView(DetailView):
    model = Grupo
    template_name = 'financeiro/grupo_detail.html'
    context_object_name = 'grupo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Filtro de Mês e Ano
        hoje = date.today()
        mes = int(self.request.GET.get('mes', hoje.month))
        ano = int(self.request.GET.get('ano', hoje.year))

        # Data usada para navegação
        data_atual = date(ano, mes, 1)
        
        # Calcular mês anterior
        if mes == 1:
            mes_anterior = 12
            ano_anterior = ano - 1
        else:
            mes_anterior = mes - 1
            ano_anterior = ano
            
        # Calcular próximo mês
        if mes == 12:
            mes_proximo = 1
            ano_proximo = ano + 1
        else:
            mes_proximo = mes + 1
            ano_proximo = ano

        # Filtrar contas do grupo para o mês/ano selecionado
        contas = self.object.contas.filter(
            data_vencimento__month=mes,
            data_vencimento__year=ano
        ).order_by('data_vencimento')

        # Totais
        total_previsto = contas.aggregate(Sum('valor'))['valor__sum'] or 0
        total_pago = contas.filter(pago=True).aggregate(Sum('valor'))['valor__sum'] or 0
        total_pendente = total_previsto - total_pago

        context.update({
            'contas': contas,
            'mes_atual': mes,
            'ano_atual': ano,
            'data_atual': data_atual,
            'mes_anterior': mes_anterior,
            'ano_anterior': ano_anterior,
            'mes_proximo': mes_proximo,
            'ano_proximo': ano_proximo,
            'total_previsto': total_previsto,
            'total_pago': total_pago,
            'total_pendente': total_pendente,
            'today': date.today(),
        })
        return context

# --- CONTAS A PAGAR ---

class ContaPagarCreateView(CreateView):
    model = ContaPagar
    form_class = ContaPagarForm
    template_name = 'financeiro/contapagar_form.html'
    
    def get_initial(self):
        initial = super().get_initial()
        # Preenche o grupo se passado na URL
        grupo_id = self.kwargs.get('grupo_id')
        if grupo_id:
            initial['grupo'] = get_object_or_404(Grupo, pk=grupo_id)
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupo_id = self.kwargs.get('grupo_id')
        if grupo_id:
            context['grupo'] = get_object_or_404(Grupo, pk=grupo_id)
        return context

    def get_success_url(self):
        return reverse('grupo-detail', kwargs={'pk': self.object.grupo.pk})

class ContaPagarUpdateView(UpdateView):
    model = ContaPagar
    form_class = ContaPagarForm
    template_name = 'financeiro/contapagar_form.html'

    def get_success_url(self):
        return reverse('grupo-detail', kwargs={'pk': self.object.grupo.pk})

class ContaPagarDeleteView(DeleteView):
    model = ContaPagar
    template_name = 'financeiro/contapagar_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('grupo-detail', kwargs={'pk': self.object.grupo.pk})

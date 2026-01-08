from django.urls import path
from .views import (
    GrupoListView, GrupoCreateView, GrupoUpdateView, GrupoDeleteView, GrupoDetailView,
    ContaPagarCreateView, ContaPagarUpdateView, ContaPagarDeleteView
)
from .views_auth import CustomLoginView, RegisterView, logout_view

urlpatterns = [
    # Autenticação
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('cadastro/', RegisterView.as_view(), name='register'),
    
    # Grupos (Espaços)
    path('', GrupoListView.as_view(), name='grupo-list'),
    path('grupo/novo/', GrupoCreateView.as_view(), name='grupo-create'),
    path('grupo/<int:pk>/', GrupoDetailView.as_view(), name='grupo-detail'),
    path('grupo/<int:pk>/editar/', GrupoUpdateView.as_view(), name='grupo-update'),
    path('grupo/<int:pk>/excluir/', GrupoDeleteView.as_view(), name='grupo-delete'),

    # Contas a Pagar
    # Nota: Criar conta vinculada a um grupo
    path('grupo/<int:grupo_id>/nova-conta/', ContaPagarCreateView.as_view(), name='contapagar-create'),
    
    # Editar/Excluir conta (já tem o ID da conta, não precisa do grupo na URL, mas a view redireciona pro grupo)
    path('conta/<int:pk>/editar/', ContaPagarUpdateView.as_view(), name='contapagar-update'),
    path('conta/<int:pk>/excluir/', ContaPagarDeleteView.as_view(), name='contapagar-delete'),
]

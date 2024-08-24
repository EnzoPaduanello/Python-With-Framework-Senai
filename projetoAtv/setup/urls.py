from django.contrib import admin
from django.urls import include, path
from todos.views import home, todoListarView, todoCriarView, todoAtualizarView, todoDeletarView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", todoListarView.as_view(template_name="todos/todoListar.html"), name='todo_listar'),
    path("cadastrar/", todoCriarView.as_view(template_name="todos/todoForm.html"), name='todo_criar'),
    path("atualizar/<int:pk>", todoAtualizarView.as_view(template_name="todos/todoForm.html"), name='todo_atualizar'),
    path("excluir/<int:pk>", todoDeletarView.as_view(), name='todo_excluir'),
    path("__debug__/", include("debug_toolbar.urls")),
]

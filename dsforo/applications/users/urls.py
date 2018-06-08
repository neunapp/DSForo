# django
from django.conf.urls import include, url

# local
from . import views

app_name="users_app"

urlpatterns = [
    # urls para registrar usuarios
    url(
        r'^nuevo-usuario/$',
        views.UserCreateView.as_view(),
        name='user_add'
    ),
    #url para login de usuarios
    url(
        r'^login/$',
        views.LogIn.as_view(),
        name='user_login'
    ),
    #url para cerrar sesion
    url(
        r'^salir/$',
        views.LogoutView.as_view(),
        name='logout'
    ),
    #url para panel de usuarios
    url(
        r'^panel/$',
        views.PanelView.as_view(),
        name='panel'
    ),
    #url para actualizar datos de usuario
    url(
        r'^modificar-datos-usuario/$',
        views.UserUpdateView.as_view(),
        name='user_update'
    ),
]

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
        name='register'
    ),
    #url para login de usuarios
    url(
        r'^login/$',
        views.LogIn.as_view(),
        name='login'
    ),
    #url para verificar codigo de usuario
    url(
        r'^salir/$',
        views.LogoutView.as_view(),
        name='logout'
    ),
    url(
        r'^verificar-user/(?P<pk>\d+)/usuario-dsforo/(?P<codigo>[-\w]+)/ds-verificacion-codigo/email-verification/$',
        views.VerificarUserView.as_view(),
        name='verificar'
    ),
    #url para resetear password
    url(
        r'^recuperar-password/$',
        views.ResetPassword.as_view(),
        name='reset'
    ),
    # url para panel de usuarios
    url(
        r'^panel/$',
        views.PanelView.as_view(),
        name='panel'
    ),
    url(
        r'^panel-tikets/$',
        views.PanelTiketView.as_view(),
        name='panel-tikets'
    ),
    #url para actualizar datos de usuario
    url(
        r'^modificar/(?P<pk>\d+)/datos-de-usuario$',
        views.UserUpdateView.as_view(),
        name='update'
    ),
]

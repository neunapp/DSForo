from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#
from django.contrib.sitemaps.views import sitemap
#
#
from django.conf.urls import handler404, handler500
#
# from applications.home.sitemap import (
#     CanchaSitemap,
#     DistritoSitemap,
#     ZoneSitemap,
#     Sitemap
# )
#
from applications.home import views

urlpatterns_main = [
    url(r'^admin/', admin.site.urls),
    #urls para home
    url(r'^', include('applications.home.urls')),
    # #urls para cancha
    url(r'^', include('applications.entradas.urls')),
    # #urls para zona
    url(r'^', include('applications.tiket.urls')),
    # #urls para museo
    # url(r'^', include('applications.museo.urls')),
    # #urls para users
    url(r'^', include('applications.users.urls')),

    #
    url(r'^captcha/', include('captcha.urls')),
    #url para editor de texto
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#objeto site map que genera xml
# sitemaps = {
#     'site':Sitemap(
#         [
#             'home_app:index'
#         ]
#     ),
#     'cancha': CanchaSitemap,
#     'zona': ZoneSitemap,
#     'distrito': DistritoSitemap,
# }
#
# #urls para sitemap
# urlpatterns_sitemap = [
#     #sitemap
#     url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
#     name='django.contrib.sitemaps.views.sitemap')
# ]

#url prncipal
# urlpatterns = urlpatterns_main + urlpatterns_sitemap

urlpatterns = urlpatterns_main

# handler404 = views.Error404View.as_view()
# handler500 = views.Error500View.as_view()

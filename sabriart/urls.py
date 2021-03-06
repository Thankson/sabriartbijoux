"""grafica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url#, patterns
from django.contrib import admin
from sito import views
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage, name='home'),
    url(r'^product/$', views.ProductView, name='product'),
    url(r'^product/(?P<post_id>\d+)/$', views.ProductFilterView, name='product-filter'),
    url(r'^news/$', views.news, name='news'),
    url(r'^news/(?P<post_id>\d+)/$', views.newsFilter, name='news-filter'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^detail/(?P<post_id>\d+)/$', views.DetailView, name='dettaglio'),
    url(r'^success/$', views.success, name='success'),
    url(r'^language/(?P<language>[a-z\-]+)/$', views.language),

]

# see: https://docs.djangoproject.com/en/1.11/ref/views/
# & https://www.cnblogs.com/virusswb/archive/2011/12/23/2299218.html
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

# if settings.DEBUG:
#         urlpatterns += [
#             #REMOVE IT in production phase
#             url(r'^media/(?P<path>.*)$', django.views.static.serve,{'document_root': settings.MEDIA_ROOT}),
#         ]

# if settings.DEBUG:
#         urlpatterns += patterns('',
#                                 #REMOVE IT in production phase
#                                 (r'^media/(?P<path>.*)$', 'django.views.static.serve',
#                                 {'document_root': settings.MEDIA_ROOT})
#           )
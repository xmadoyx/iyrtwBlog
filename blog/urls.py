from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from articles.views import articles_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/' , views.about),
    path('articles/' , include('articles.urls')),
    path('accounts/',include('accounts.urls')),
    path('', articles_list),
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

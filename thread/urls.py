from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from home.views import *

urlpatterns = [
  path('', news_home, name='home'),
  path('delete/<id>/', news_delete, name='delete'),
  path('edit/<id>/', news_edit, name='edit'),
  path('publish/', news_publish, name='publish'),
  path('update/', news_update, name='update'),
  path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
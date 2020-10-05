from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [	
path('',views.index, name='index'),
path('<int:id>',views.display, name='display'),
# re_path(r'.*',views.index, name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
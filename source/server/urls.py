from django.contrib import admin
from django.urls import url

from arquivo.views import ArquivoUploadAPIView
from healthcheck.views import HealthcheckAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^healthcheck', HealthcheckAPIView.as_view()),
    url(r'^api/v1/arquivo', ArquivoUploadAPIView.as_view())
    
]

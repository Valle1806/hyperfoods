# urls.py 
from django.urls import path
from django.views.generic.base import TemplateView

from .views import (
    Frontend
)

urlpatterns = [
path("", Frontend.as_view()),
path('service-worker.js', TemplateView.as_view(template_name="service-worker.js", 
    content_type='application/javascript'), name='service-worker.js'),
]
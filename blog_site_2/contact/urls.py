from django.urls import path, include
from .views import contact

app_name = 'contact'

urlpatterns = [
    path('', contact, name='index'),
    path('api/', include('contact.api.urls'))
]
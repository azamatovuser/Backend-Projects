from django.urls import path, include

app_name = 'account'

urlpatterns = [
    path('', include('apps.account.v1.urls'))
]
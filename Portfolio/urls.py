from django.contrib import admin
from django.urls import path    
from testPort.views import Pages
from testPort.views import Welcome
from testPort.apis import RegistrationAPI
from testPort.apis import LoginAPI
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', Welcome.as_view(), name='welcome'),
    path('<str:page_type>/', Pages.as_view(), name='pages'),
    path('api/register/', RegistrationAPI.as_view(), name='RegistrationAPI'),
    path('api/login/', LoginAPI.as_view(), name='RegistrationAPI')
]  
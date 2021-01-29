
from django.urls import path, include
from . import views
##Original
#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

urlpatterns = [
    path('', views.index, name ='index'),

]
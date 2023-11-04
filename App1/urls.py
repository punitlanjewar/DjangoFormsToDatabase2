from django.urls import path
from App1 import views


urlpatterns = [
    path('', views.home_fun),
    path('add_bike', views.bike_fun, name='add_bike'),
    path('display', views.disp_fun, name='display'),
    path('update/<int:id>', views.update_fun, name='update'),
    path('delete/<int:id>', views.del_fun, name='delete'),
]
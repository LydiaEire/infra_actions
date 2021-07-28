import django.urls

from . import views

app_name = 'infra_app'

urlpatterns = [
    django.urls.path('', views.index, name='index'),
    django.urls.path('second_page/', views.second_page, name='second_page'),

]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
path('<int:inc_count>/', views.next_data, name='next_data'),
    path('tokens/<int:inc_count>/<selected_tokens>', views.process_data, name='process_data'),
]
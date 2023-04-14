from django.urls import path

from task1_app.views import add_view, substract_view, multiply_view, divide_view


urlpatterns = [
    path('add/', add_view),
    path('substract/', substract_view),
    path('multiply/', multiply_view),
    path('divide/', divide_view),
]
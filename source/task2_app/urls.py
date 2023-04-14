from django.urls import path

from task2_app.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
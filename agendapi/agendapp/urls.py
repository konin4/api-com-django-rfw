from django.conf.urls import url, include
from . import views

# urlpatterns = [
#     url(r'^agenda/$', views.AgendaList.as_view(), name='agenda-list')
# ]

urlpatterns = [
    url('agenda/', views.AgendaList.as_view()),
]
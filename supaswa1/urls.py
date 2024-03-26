from django.urls import path
from supaswa1 import views

urlpatterns = [
    path('update/', views.IotDataView.as_view()),
    path('IotDataView1/', views.IotDataView1.as_view()),
    path('IotDataView2/', views.IotDataView2.as_view()),
    path('APPData/', views.APPData.as_view()),
]

# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path("", views.index, name="index"),
# ]
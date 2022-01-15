from django.urls import path
from . import views

urlpatterns = [ 
    # path('', views.index, name='index'),
    path('train/', views.Train),
    path('prediction/<str:text>/', views.Prediction),
    path("",views.ListDataAPIView.as_view(),name="crud_list"),
    path("create/", views.CreateDataAPIView.as_view(),name="crud_create"),
    path("update/<int:pk>/",views.UpdateDataAPIView.as_view(),name="update_crud"),
    path("delete/<int:pk>/",views.DeleteDataAPIView.as_view(),name="delete_crud")
]
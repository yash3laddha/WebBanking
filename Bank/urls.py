from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Customer/', views.custTable, name='cust'),
    path('Customer/<int:Acc>/', views.trans, name='trans'),
    path('transhis/', views.update_bal_req, name='transhis'),
    path('transhistory/', views.transfer_his, name='transhistory')
]
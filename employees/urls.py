from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('employee_list/', views.employee_list, name="list"),
    path('employee_list/add_employee/', views.add_employee, name="add"),
    path('employee_list/edit_employee/<int:id>', views.edit_employee, name="edit"),
    path('employee_list/update/<int:id>', views.update, name="update"),
    path('employee_list/delete_employee/', views.delete_employee, name="delete"),
    path('employee_list/search_employee/', views.search_employee, name="search"),
    path('employee_list/static_queries/', views.static_queries, name="query"),
    #rest
    path('myget/<str:name>/', views.list_by_name, name="list_by_name"),
    path('mydel/married/', views.del_married_emp, name="del_married_emp"),
    path('mydel/single/', views.del_single_emp, name="del_single_emp"),
    path('myupdate/<int:pc>/<int:money>/', views.update_income, name="update_income"),
]

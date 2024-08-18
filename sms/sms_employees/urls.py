from django.urls import path
from sms_employees import views
from django.utils import timezone

urlpatterns = [
    path('', views.EmployeeListView.as_view()),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/profile/', views.EmployeeListView.as_view()),
    
    path('show_employee/', views.EmployeeListView.as_view(), name='employee_list'),
    path('new_employee/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('<int:pk>', views.EmployeeDetailView.as_view(), name='employee_detail'),
]
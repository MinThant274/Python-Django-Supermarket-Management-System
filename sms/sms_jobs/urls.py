from django.urls import path
from sms_jobs import views

urlpatterns = [
    path('', views.JobListView.as_view()),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/profile/', views.JobListView.as_view()),

	path('show_job/', views.JobListView.as_view(), name='job_list'),
    path('new_job/', views.JobCreateView.as_view(), name='job_create'),
    path('<int:pk>', views.JobDetailView.as_view(), name='job_detail'),
    path('<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),
    path('<int:pk>/edit/', views.JobUpdateView.as_view(), name='job_update'),
]
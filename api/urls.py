from django.urls import path

from . import views

urlpatterns = [
    path("", views.ping_pong_view),

    path('projects/', views.get_projects_view),
    
    path('project/<int:pk>', views.get_project_view)

]

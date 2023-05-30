from django.urls import path
from .views import DepartmentListCreateView, DepartmentRUDView, PersonnelListCreateView, PersonnelRUDView


urlpatterns = [
    path('departments/',DepartmentListCreateView.as_view())
]
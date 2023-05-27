from rest_framework.viewsets import ModelViewSet
from .serializers import(
    Department, DepartmentSerializer,
    Personnel, PersonnelSerializer
)
from personnel.permissions import IsSuperuser

class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    

class PersonnelView(ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = [IsSuperuser]
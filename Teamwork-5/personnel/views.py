from rest_framework.viewsets import ModelViewSet
from .serializers import(
    Department, DepartmentSerializer,
    Personnel, PersonnelSerializer
)


class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    

class PersonnelView(ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
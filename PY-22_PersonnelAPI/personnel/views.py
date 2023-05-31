from django.shortcuts import render
from .serializers import DepartmentSerializer, PersonnelSerializer, Personnel, Department,DepartmentPersonnelSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PersonnelListCreateView(ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer


class PersonnelRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer


class DepartmentPersonnelView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentPersonnelSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned department to a given one,
        by filtering against a `department` query parameter in the URL.
        """
        department = self.kwargs['department']
        if department is not None:
            return Department.objects.filter(name__iexact=department)
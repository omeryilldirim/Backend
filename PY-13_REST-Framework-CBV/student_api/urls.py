from django.urls import path

from .views import (
    StudentListCreate,
    StudentDetailUpdateDelete,
    StudentGPPD,
    StudentGenericListCreate,
    StudentListCreateAPIView,
    StudentRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('student_list_create/', StudentListCreate.as_view()),
    path('student_detail_update_delete/<int:pk>', StudentDetailUpdateDelete.as_view()),
    path('student_gppd/', StudentGPPD.as_view()),
    path('student_gppd/<int:pk>', StudentGPPD.as_view()),
    path('student_generic_list_create/', StudentGenericListCreate.as_view()),
    path('student_list_create_api/', StudentListCreateAPIView.as_view()),
    path('student_get_put_delete_api/<int:pk>', StudentRetrieveUpdateDestroyAPIView.as_view()),
]


# ----------------------------------------------------------------
# Router for ModalViewSet
# ----------------------------------------------------------------
from rest_framework.routers import DefaultRouter
from .views import StudentModelViewSet

router = DefaultRouter()
router.register('students', StudentModelViewSet)
# router.register('another', AnotherModelViewSet)
urlpatterns += router.urls

from rest_framework.routers import DefaultRouter
from .views import DepartmentView, PersonnelView

router = DefaultRouter()
router.register('department', DepartmentView)
router.register('', PersonnelView)
urlpatterns = router.urls

from rest_framework.viewsets import ModelViewSet

from .serializers import Todo, TodoSerializer

from rest_framework.pagination import PageNumberPagination
from .paginations import CustomPageNumberPagination, CustomLimitOffsetPagination, CustomCursorPagination

class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = CustomCursorPagination
    # pagination_class = CustomLimitOffsetPagination
    # pagination_class = CustomPageNumberPagination
    
    # # Alternative

    # pagination_class = PageNumberPagination
    # PageNumberPagination.page_size = 25
    # PageNumberPagination.page_query_param = 'sayfa'
    # PageNumberPagination.page_size_query_param = 'sayfada_kaç_adet'


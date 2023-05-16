from rest_framework.viewsets import ModelViewSet

from .serializers import Todo, TodoSerializer

from rest_framework.pagination import PageNumberPagination
from .paginations import CustomPageNumberPagination, CustomLimitOffsetPagination, CustomCursorPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class TodoView(ModelViewSet):
    queryset = Todo.objects.all().order_by('-id') # default ordering
    serializer_class = TodoSerializer
    #### LOCAL PAGINATION SETTING
    # pagination_class = CustomCursorPagination
    # pagination_class = CustomLimitOffsetPagination
    pagination_class = CustomPageNumberPagination

    #### FİLTRELEME MODÜLLERİ
    # local filter setting
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # filter birebir eşleştirme
    filterset_fields = ['is_done', 'priority'] # django_filters module

    # search
    search_fields = ['title', 'id', 'description']

    # ordering
    ordering_fields = ['id', 'priority', 'is_done']

    
    # # Alternative

    # pagination_class = PageNumberPagination
    # PageNumberPagination.page_size = 25
    # PageNumberPagination.page_query_param = 'sayfa'
    # PageNumberPagination.page_size_query_param = 'sayfada_kaç_adet'
    '''
    #### Manuel Filtreleme
    
    def get_queryset(self):
        title = self.request.query_params.get('title') # urlden gelen parametreleri almak için 
        if title is None:
            return super().get_queryset()
        else:
            return self.queryset.filter(title__contains=title)
    '''
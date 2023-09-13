from .models import Poster
from .serializers import PosterSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination


class StandardPageNumberPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 50    # 前端控制时最多不能超过50
    page_query_param = 'page'  # 前端指定第几页时的名字
    page_size_query_param = 'page_size'  # 每页多少条的关键字


class PosterViewSet(ModelViewSet):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer
    # 指定权限
    permission_classes = [IsAuthenticatedOrReadOnly]
    # 对于put和delete，要额外进行判断，即只能修改或删除自己的poster

    filter_backends = [OrderingFilter]
    # 指定排序字段
    ordering_fields = ['date']

    pagination_class = StandardPageNumberPagination

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination

class userLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 5

class userPageNumberPagination(PageNumberPagination):
    page_size = 1

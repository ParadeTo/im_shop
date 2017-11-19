# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size' # 每页大小
    page_query_param = "page"
    max_page_size = 100 # 每页最大的记录
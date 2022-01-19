from rest_framework.pagination import PageNumberPagination


class DataPagination(PageNumberPagination):
    page_size = 2

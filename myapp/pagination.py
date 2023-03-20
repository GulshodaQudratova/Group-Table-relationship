from rest_framework.pagination import LimitOffsetPagination , PageNumberPagination
from rest_framework.response import Response
class CustomPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 3
    limit_query_param = 'chegara'
    offset_query_param = 'danbuyogi'
# class CustomPagination(PageNumberPagination):
    # page_size =2
    # page_query_param = 'sahifa'
    # def get_paginated_response(self, data):
    #     return Response({
    #         'next': self.get_next_link(),
    #         'previous': self.get_previous_link(),
    #         'all_posts': self.page.paginator.count,
    #         'page_post': len(self.page.object_list),
    #         'page_number':self.page.number,
    #         'all_pages_count':self.page.paginator.num_pages,
    #         'results': data
    #     })
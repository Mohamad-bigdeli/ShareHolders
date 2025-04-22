from __future__ import annotations

from datetime import datetime

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    MultiMatchSearchFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework import generics, status
from rest_framework.response import Response

from core.paginations import CustomPagination

from ...documents import ShareholdersDocument
from ...models import ShareholdersHistory
from ...services import DailyChanges, MonthlyChanges, WeeklyChanges
from ...tasks import daily_changes_task, weekly_changes_task, monthly_changes_task

# from rest_framework.permissions import IsAuthenticated
from .serializers import (
    ShareholderChangeSerializer,
    ShareholdersDocumentSerializer,
    ShareholdersListSerializer,
)


class ShareholdersListAPIView(generics.GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ShareholdersListSerializer
    pagination_class = CustomPagination
    queryset = ShareholdersHistory.objects.all()
    
    @method_decorator(cache_page(60 * 15))
    def get(self, request, *args, **kwargs):
        try:
            symbol = self.kwargs['symbol']
        except KeyError:
            return Response({"error": "پارامتر نماد اجباری است"}, status=status.HTTP_400_BAD_REQUEST)

        queryset = ShareholdersHistory.objects.filter(symbol=symbol)
        
        if not queryset.exists(): 
            return Response({"error": "نماد وجود ندارد یا داده‌ای برای آن ثبت نشده است"}, status=status.HTTP_404_NOT_FOUND)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class ShareholdersDocumentViewSet(DocumentViewSet):
#     # permission_classes = [IsAuthenticated]
#     document = ShareholdersDocument
#     serializer_class = ShareholdersDocumentSerializer

#     filter_backends = [
#         SearchFilterBackend,
#         SuggesterFilterBackend,
#         FilteringFilterBackend,
#         MultiMatchSearchFilterBackend
#     ] 

#     search_fields = (
#         'shareholder_name',
#         'symbol',
#     )
#     multi_match_search_fields = {
#         "symbol": {"boost": 4},
#         "shareholder_name": {"boost": 3},
#     }
#     multi_match_options = {
#         "fuzziness": "AUTO",
#         "prefix_length": 2,
#         "max_expansions": 50,
#     }
    
#     filter_fields = {
#         'shareholder_name': 'shareholder_name.raw',
#         'symbol': 'symbol.raw',
#     }

#     suggester_fields = {
#         'shareholder_name_suggest': {
#             'field': 'shareholder_name.suggest',
#             'suggesters': ['completion'],
#         },
#         'symbol_suggest': {
#             'field': 'symbol.suggest',
#             'suggesters': ['completion'],
#         },
#     }

#     fuzzy_search_fields = (
#         'shareholder_name.fuzzy',
#         'symbol.fuzzy',
#     )

class ShareholdersDailyChangesApiView(generics.GenericAPIView):

    serializer_class = ShareholderChangeSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    queryset = ShareholdersHistory.objects.all()

    @method_decorator(cache_page(60 * 15))
    def get(self, request, *args, **kwargs):
        
        try:
            symbol = self.kwargs['symbol']
        except KeyError:
            return Response({"error": "پارامتر نماد اجباری است"}, status=status.HTTP_400_BAD_REQUEST)

        current_date = datetime.now().date()

        try:
            changes_data = daily_changes_task.delay(symbol=symbol, current_date=current_date)
        except Exception as e:
            return Response({"error": f"خطا در محاسبه تغییرات: {e!s}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = ShareholderChangeSerializer(data=changes_data, many=True)
        if serializer.is_valid():
            paginated_data = self.paginate_queryset(serializer.data)
            return self.get_paginated_response(paginated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShareholdersWeeklyChangesApiView(generics.GenericAPIView):

    serializer_class = ShareholderChangeSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    queryset = ShareholdersHistory.objects.all()

    @method_decorator(cache_page(60 * 15))
    def get(self, request, *args, **kwargs):
        
        try:
            symbol = self.kwargs['symbol']
        except KeyError:
            return Response({"error": "پارامتر نماد اجباری است"}, status=status.HTTP_400_BAD_REQUEST)

        current_date = datetime.now().date()

        try:
            changes_data = weekly_changes_task.delay(symbol=symbol, current_date=current_date)
        except Exception as e:
            return Response({"error": f"خطا در محاسبه تغییرات: {e!s}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = ShareholderChangeSerializer(data=changes_data, many=True)
        if serializer.is_valid():
            paginated_data = self.paginate_queryset(serializer.data)
            return self.get_paginated_response(paginated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShareholdersMonthlyChangesApiView(generics.GenericAPIView):

    serializer_class = ShareholderChangeSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    queryset = ShareholdersHistory.objects.all()

    @method_decorator(cache_page(60 * 15))
    def get(self, request, *args, **kwargs):
        
        try:
            symbol = self.kwargs['symbol']
        except KeyError:
            return Response({"error": "پارامتر نماد اجباری است"}, status=status.HTTP_400_BAD_REQUEST)

        current_date = datetime.now().date()

        try:
            changes_data = monthly_changes_task.delay(symbol=symbol, current_date=current_date)
        except Exception as e:
            return Response({"error": f"خطا در محاسبه تغییرات: {e!s}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = ShareholderChangeSerializer(data=changes_data, many=True)
        if serializer.is_valid():
            paginated_data = self.paginate_queryset(serializer.data)
            return self.get_paginated_response(paginated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
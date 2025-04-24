from __future__ import annotations

from datetime import datetime

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.postgres.search import SearchVector
from rest_framework import generics, status
from rest_framework.response import Response

from core.paginations import CustomPagination

from ...models import ShareholdersHistory
from ...tasks import daily_changes_task, weekly_changes_task, monthly_changes_task

# from rest_framework.permissions import IsAuthenticated
from .serializers import (
    ShareholderChangeSerializer,
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
            task_result = daily_changes_task.delay(symbol=symbol, current_date=current_date)
            changes_data = task_result.get()
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
            task_result = weekly_changes_task.delay(symbol=symbol, current_date=current_date)
            changes_data = task_result.get()
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
            task_result = monthly_changes_task.delay(symbol=symbol, current_date=current_date)
            changes_data = task_result.get()
        except Exception as e:
            return Response({"error": f"خطا در محاسبه تغییرات: {e!s}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = ShareholderChangeSerializer(data=changes_data, many=True)
        if serializer.is_valid():
            paginated_data = self.paginate_queryset(serializer.data)
            return self.get_paginated_response(paginated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShareholdersSearchApiView(generics.GenericAPIView):
    
    # permission_classes = [IsAuthenticate]
    serializer_class = ShareholdersListSerializer
    pagination_class = CustomPagination
    queryset = ShareholdersHistory.objects.all()

    @method_decorator(cache_page(60 * 15))
    def get(self, request, *args, **kwargs):
        try:
            query = self.kwargs['query']
        except KeyError:
            return Response({"error": "پارامتر نماد یا نام سهامدار و یا شناسه سهامدار برای جستجو اجباری است"}, status=status.HTTP_400_BAD_REQUEST)

        search_vector = SearchVector("symbol", "shareholder_name", "shareholder_id")
        queryset = ShareholdersHistory.objects.annotate(search=search_vector).filter(search=query)

        if not queryset.exists():
            return Response({"detail":"نتیجه ای برای جستجو یافت نشد"}, status=status.HTTP_404_NOT_FOUND)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
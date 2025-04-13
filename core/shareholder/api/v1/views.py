from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from .serializers import ShareholdersListSerializer
from ...models import Shareholder
from rest_framework.response import Response
from rest_framework import status
from core.paginations import CustomPagination

class ShareholdersListAPIView(generics.GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ShareholdersListSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        try:
            symbol = self.kwargs['symbol']
        except KeyError:
            return Response({"error": "پارامتر نماد اجباری است"}, status=status.HTTP_400_BAD_REQUEST)

        queryset = Shareholder.objects.filter(symbol=symbol)
        
        if not queryset.exists(): 
            return Response({"error": "نماد وجود ندارد یا داده‌ای برای آن ثبت نشده است"}, status=status.HTTP_404_NOT_FOUND)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
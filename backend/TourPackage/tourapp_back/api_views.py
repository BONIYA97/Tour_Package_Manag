from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from .models import Package
from .serializers import EnquirySerializer, ScheduleSerializer

class EnquiryCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PackageSchedulesAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        package = get_object_or_404(Package, pk=pk)
        schedules = package.schedules.order_by('from_date')
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)

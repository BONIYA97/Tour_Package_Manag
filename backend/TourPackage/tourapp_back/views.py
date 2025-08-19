from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Package, Enquiry
from .serializers import PackageSerializer, EnquirySerializer

@api_view(['GET'])
def package_list(request):
    packages = Package.objects.all()
    serializer = PackageSerializer(packages, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def package_detail(request, pk):
    try:
        package = Package.objects.get(pk=pk)
    except Package.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PackageSerializer(package, context={'request': request})
    return Response(serializer.data)

@api_view(['POST'])
def enquiry_create(request):
    serializer = EnquirySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Banner
from .serializers import BannerSerializer

class BannerListAPIView(APIView):
    def get(self, request):
        banners = Banner.objects.all()
        serializer = BannerSerializer(banners, many=True, context={'request': request})
        return Response(serializer.data)

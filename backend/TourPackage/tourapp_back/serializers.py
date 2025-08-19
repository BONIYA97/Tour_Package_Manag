from rest_framework import serializers
from .models import Package, Schedule, Enquiry, Banner

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer(many=True, read_only=True)
    photo = serializers.ImageField(use_url=True)
    class Meta:
        model = Package
        fields = '__all__'

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'title', 'image']
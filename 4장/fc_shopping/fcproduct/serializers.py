from rest_framework import serializers
from .models import Fcproduct

class FcproductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fcproduct
        fields = '__all__'
from rest_framework import serializers
from crud.models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = "__all__"
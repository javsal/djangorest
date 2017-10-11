from rest_framework import serializers
from .models import PlayerList, DistrictList

class DistrictListSerializer(serializers.ModelSerializer):

    class Meta:
        model=DistrictList
        fields=('id', 'name')
        read_only_fields=('date_created', 'date_modified')


   
class PlayerListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    home_district = DistrictListSerializer(required=False)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = PlayerList
        fields = ('id', 'name', 'age', 'gender', 'palyer_type', 'home_district',  'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
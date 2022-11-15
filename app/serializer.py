from rest_framework import serializers
from .models  import BotUsers
class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUsers
        fields = "__all__"
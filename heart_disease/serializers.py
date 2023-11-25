from rest_framework import serializers


class UserInputSerializer(serializers.Serializer):
    age = serializers.IntegerField(min_value=0, max_value=120)
    sex = serializers.IntegerField(min_value=0, max_value=1)
    cp = serializers.IntegerField(min_value=0, max_value=3)
    trestbps = serializers.IntegerField(min_value=0)
    chol = serializers.IntegerField(min_value=0)
    fbs = serializers.IntegerField(min_value=0, max_value=1)
    restecg = serializers.IntegerField(min_value=0, max_value=2)
    thalach = serializers.IntegerField(min_value=0)
    exang = serializers.IntegerField(min_value=0, max_value=1)
    oldpeak = serializers.FloatField(min_value=0)
    slope = serializers.IntegerField(min_value=0, max_value=2)
    ca = serializers.IntegerField(min_value=0, max_value=3)
    thal = serializers.IntegerField(min_value=0, max_value=3)

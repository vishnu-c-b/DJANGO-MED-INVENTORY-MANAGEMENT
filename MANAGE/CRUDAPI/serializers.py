from rest_framework import serializers
from .forms import CreateUserForm,LoginForm,Create,Update,Search
from .models import Medicine
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'
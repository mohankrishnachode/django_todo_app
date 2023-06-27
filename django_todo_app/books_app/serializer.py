from rest_framework import serializers
from .models import Books
# Create your tests here.
class BookSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id','author','title','created']

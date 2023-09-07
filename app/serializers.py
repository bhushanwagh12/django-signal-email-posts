from rest_framework import serializers
from .models import Post,User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def create(self,validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self,instance,validate_data):
        instance.title = validate_data.get('title',instance.title)
        instance.body = validate_data.get('body',instance.description)
        instance.author = validate_data.get('author',instance.active)
        instance.save()
        return instance
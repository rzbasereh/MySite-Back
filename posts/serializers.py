from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title','slug', 'content','modified','created','status')

        
    
    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
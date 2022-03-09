from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    ("draft","Draft"),
    ("publish","Publish")
)

class Post(models.Model): 
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    modified = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
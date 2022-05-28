from django.db import models
from django.forms import SlugField
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=36)
    slug=models.SlugField()
    
class BlogPost(models.Model):
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    category=models.ManyToManyField(Category)
    title= models.CharField(max_length=100)
    slug=models.SlugField()
    published=models.BooleanField(default=False)
    date=models.DateField(blank=True,null=True)
    content=models.TextField()
    description=models.TextField()
    
    """    def publishString(self):
        if self.published:
            return "L'article est publié"
        return "L'article est inacessible"
    """
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        
        super().save(*args,**kwargs)
        

"""
from blog.models import Category
#creer
a = BlogPost(title="les base de django", slug="", content="",description="")
a.save()
Category.objects.create(name="Django",slug="django")
#acceder
BlogPost.objects.all()
BlogPost.objects.get(pk=3)
#modifier
b = BlogPost.objects.get(pk=1)
b.content = "ce article parle de python"
#suppr
b=BlogPost.objects.all().delete()
b[:10].delete()
b[0].delete()
#filter
BlogPost.objects.filter(published=True)
BlogPost.objects.filter(date__year="2021")
"""



 

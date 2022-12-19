from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,verbose_name='Yazar',on_delete=models.CASCADE)
    title=models.CharField(max_length=150,verbose_name='Başlık')
    content=RichTextField(verbose_name='Açıklama')
    date_time=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(null=True,blank=True)
    slug=models.SlugField(unique=True,editable=False)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'slug':self.slug})

    def get_create_url(self):
        return reverse('create')

    def get_update_url(self):
        return reverse('update',kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('delete',kwargs={'slug':self.slug})

    def get_unique_slug(self):
        slug=slugify(self.title.replace('ı','i'))
        unique_slug=slug
        counter=1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug='{}-{}'.format(slug,counter)
            counter+=1
        return unique_slug

    
    def save(self,*args,**kwargs):
        self.slug=self.get_unique_slug()
        return super(Post,self).save(*args,**kwargs)





        
    class Meta:
        ordering=['-date_time','id']



class Comment(models.Model):
    post=models.ForeignKey('myapp.Post',related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=150,verbose_name='İsim')
    content=models.TextField(verbose_name='Yorum')

    created_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_date','id']
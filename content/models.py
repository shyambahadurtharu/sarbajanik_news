from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class NewsStatus(models.TextChoices):
    PUBLIC = ("public", "Public")
    PRIVATE = ("private", "Private")
class PositionStatus(models.TextChoices):
    NORMAL = ("normal", "Normal")
    FIRST = ("first", "First")
    SECOND = ("second", "Second")
    THIRD = ("third", "Third")
    FORTH = ("forth", "Forth")
class ProvinceStatus(models.TextChoices):
    ALL = ("all", "All")
    ONE = ("one", "One")
    SECOND = ("second", "Second")
    THIRD = ("third", "Third")
    FORTH = ("forth", "Forth")
    FIFTH = ("fifth", "Fifth")
    SIX = ("six", "Six")
    SEVEN = ("SEVEN", "Seven")
class Category(models.Model):
    category_name=models.TextField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.category_name
    
class News(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    sub_description = models.TextField( blank=True, null=True)
    description = RichTextField()
    picture = models.ImageField(upload_to="news_image/", blank=True, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)

    news_postion = models.CharField(
        max_length=100,
        choices=PositionStatus.choices,
        default=PositionStatus.NORMAL
    )
    province = models.CharField(
        max_length=100,
        choices=ProvinceStatus.choices,
        default=ProvinceStatus.ALL
    )
    status = models.CharField(
        max_length=100,
        choices=NewsStatus.choices,
        default=NewsStatus.PRIVATE
    )

    
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "Newss"

    def __str__(self):
        return str(self.id)
    
    @property
    def like_count(self):
        return self.like_set.filter(is_liked=True).count()
    @property   
    def comment_count(self):
        return self.comment_set.count()
    
class Like(models.Model):
    is_liked = models.BooleanField(default=False)
    post = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    
   
    
class Comment(models.Model):
    text = models.CharField(max_length=150)
    post = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
class Organization(models.Model):
    org_name = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to="logo_image/", blank=True, null=False)
    address = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twiter = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    linkdin = models.CharField(max_length=100, blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.id)
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=False)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return str(self.id)

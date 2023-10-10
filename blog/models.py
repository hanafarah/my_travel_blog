from django.conf import settings
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')

    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevent posts from being deleted
        related_name='posts',  # "This" on the user model
        null=False
    )
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
    )
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published',
    )
    slug = models.SlugField(
        null=False,
        unique_for_date='published',  # Slug is unique for publication date
    )
    topics = models.ManyToManyField('Topic', related_name='posts')
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def publish(self):
        self.status = self.PUBLISHED
        self.published = timezone.now()


class Topic(models.Model):
    name = models.CharField(max_length=355,
        unique=True)

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
# Core Django imports.
import uuid
from django.utils.html import mark_safe
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField()
    image = models.ImageField(default='category-default.jpg',
                              upload_to='category_images')
    approved = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="80" />' %
                         (self.image))

    image_tag.short_description = 'Image'

    class Meta:
        unique_together = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:category_articles', kwargs={'slug': self.slug})

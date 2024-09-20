from django.db import models

# Create your models here.


class Categories(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    reviews_at = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Events(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    reviews_at = models.IntegerField(default=0)
    price = models.FloatField()
    date = models.DateField()
    place = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

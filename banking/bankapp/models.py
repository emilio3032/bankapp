from django.db import models

# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.URLField()

    class Meta:
        ordering=('name',)
        verbose_name='district'
        verbose_name_plural='districts'

    def __str__(self):
        return '{}'.format(self.name)

class Branch(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'

    def __str__(self):
        return '{}'.format(self.name)



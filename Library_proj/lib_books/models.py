from __future__ import unicode_literals

from django.db import models


class Library(models.Model):
    lib_type = models.CharField(max_length=255)

    def __str__(self):
        return self.lib_type


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    year_pub = models.IntegerField()
    library = models.ForeignKey(Library, default='', on_delete=models.CASCADE)


    class Meta:
        ordering = ['year_pub',]

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

            


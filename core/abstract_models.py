from django.db import models


class SingletonAbstract(models.Model):
    """ An abstract model for forcing models to be singleton. """
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_object(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        abstract = True

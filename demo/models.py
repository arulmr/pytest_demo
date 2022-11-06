from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return F'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    @property
    def full_name(self):
        return F'{self.first_name} {self.last_name}'

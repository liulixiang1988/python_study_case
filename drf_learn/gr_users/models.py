from django.db import models
from django.contrib.auth.models import User

class GRUser(models.Model):
    first_name = models.TextField('姓', max_length=100)
    last_name = models.TextField('名', max_length=100)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

from django.db import models
#from django.utils.encoding import  smart_unicode


# Create your models here.
class SignUp(models.Model):
    first_name = models.CharField('姓', max_length=120, null=True, blank=True)
    last_name = models.CharField('名', max_length=120, null=True, blank=True)
    email = models.EmailField('邮箱')
    timestamp = models.DateTimeField('注册时间', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('更新时间', auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.email)#smart_unicode(self.email)

    class Meta:
        verbose_name = '注册'
        verbose_name_plural = '注册'

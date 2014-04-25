from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('类别', max_length=128, unique=True)
    views = models.IntegerField('查看', default=0)
    likes = models.IntegerField('喜欢', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = '类别'


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField('标题', max_length=128, blank=False, null=False)
    url = models.URLField('链接')
    views = models.IntegerField('查看', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '页面'
        verbose_name_plural = '页面'


class UserProfile(models.Model):
    #关联用户
    user = models.OneToOneField(User)

    website = models.URLField('网址', blank=True)
    picture = models.ImageField('头像', upload_to='profile_images', blank=True)

    class Meta:
        verbose_name = '用户说明'
        verbose_name_plural = '用户说明'

    def __str__(self):
        return self.user.username
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets


#serializer定义了如何展示API
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


#ViewSets定义了View的行为
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Routers提供了如何路由
router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drf_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)

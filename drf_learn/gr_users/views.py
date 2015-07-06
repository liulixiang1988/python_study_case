# -*- coding:utf-8 -*-

from rest_framework.response import Response
from rest_framework.decorators import api_view

from gr_users.models import GRUser
from gr_users.serializers import GRUserSerializer


@api_view(['GET'])
# @permission_classes((permissions.IsAuthenticated, ))
def get_user(request, **kwargs):
    pk = request.data['pk']
    user = GRUser.objects.get(pk=pk)
    serializers = GRUserSerializer(user)
    return Response(serializers.data)

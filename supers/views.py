from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Super


@api_view(['GET', 'POST'])
def supers_list(request):

    if request.method == 'GET':
        type_name = request.query_params.get('type')
        print(type_name)
        supers = Super.objects.all()
        if type_name:
            supers = supers.filter(super_type__type=type_name)
        else:
            heroes = Super.objects.filter(super_type__type='hero')
            villains = Super.objects.filter(super_type__type='villain')
            custom_response = {'heroes': SupersSerializer(heroes, many=True).data, 'villains': SupersSerializer(villains, many=True).data}
            print(custom_response)
            return Response(custom_response)
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)

    if request.method == 'GET':
        serializer = SupersSerializer(super)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

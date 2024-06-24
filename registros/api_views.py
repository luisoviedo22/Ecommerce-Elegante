from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from registros.models import Usuario
from registros.serializers import UsuarioSerializers

@api_view(['GET', 'POST'])
def usuario_list(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializers(usuarios, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UsuarioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloAPIView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerialiser
    
    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'uses HTTP methods as functions (get,put,pathch,post,delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
                    ]
        
        return Response({'message':'Hello','an_apiview':an_apiview})
    
    
    def post(self,request):
        
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'Message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'message':'PATCH'})
    def delete(self,request,pk=None):
        """Delete an onject"""
        return Response({'method':'delete'})

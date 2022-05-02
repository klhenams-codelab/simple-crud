from cgi import print_directory
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser


from crud.serializers.file import FileUploadSerializer
from crud.tasks import csv_to_db_task



class UploadFileAPIView(generics.CreateAPIView):
    parser_classes = [FormParser, MultiPartParser]
    serializer_class = FileUploadSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        csv_to_db_task.delay(obj.pk)
        return Response(status=status.HTTP_201_CREATED)
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser


from crud.serializers.file import FileUploadSerializer
from crud.utils.importer import csv_to_db



class UploadFileAPIView(generics.CreateAPIView):
    parser_classes = [FormParser, MultiPartParser]
    serializer_class = FileUploadSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        request.upload_handlers.pop(0)
        file = self._file_upload(request,  *args, **kwargs)
        csv_to_db(file)
        return Response(status=status.HTTP_201_CREATED)
    
    
    def _file_upload(self, request,  *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data['file']
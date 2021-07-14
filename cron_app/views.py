from django.shortcuts import render
from .models import Students
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
class StudentView(viewsets.ViewSet):
    def returnData():
        stu=Students.objects.all()
        serializer=StudentSerializer(stu,many=True,context={"request": request})
        print("scheduler called")
        return Response(serializer.data)
    @method_decorator(csrf_exempt)
    def list(self,request):
        stu=Students.objects.all()
        serializer=StudentSerializer(stu,many=True,context={"request": request})
        return Response(serializer.data,status.HTTP_200_OK)

    @method_decorator(csrf_exempt)
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'New Student Registerd'},status=status.HTTP_201_CREATED)
        else:
            return Response({'msg':'Student is not created'},status.HTTP_400_BAD_REQUEST)

    @method_decorator(csrf_exempt)
    def retrieve(self,request,pk=None):
            queryset = Students.objects.all()
            stu = get_object_or_404(queryset, pk=pk)
            serializer = StudentSerializer(stu,context={"request": request})
            return Response(serializer.data,status=status.HTTP_200_OK)

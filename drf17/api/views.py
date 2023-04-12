from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print("---- List ----")
        print("Basename: " , self.basename)
        print("Action: " , self.action)
        print("Detail: " , self.detail)
        print("Suffix: " , self.suffix)
        print("Name: " , self.name)
        print("Description: " , self.description)
        print("------------------>>>>>>>>>>>>>")
        """---- List ----
        Basename:  student
        Action:  list
        Detail:  False
        Suffix:  List
        Name:  None
        Description:  None
        ------------------>>>>>>>>>>>>>"""
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print("---- Retrieve ----")
        print("Basename: " , self.basename)
        print("Action: " , self.action)
        print("Detail: " , self.detail)
        print("Suffix: " , self.suffix)
        print("Name: " , self.name)
        print("Description: " , self.description)
        print("------------------>>>>>>>>>>>>>")
        """---- Retrieve ----
        Basename:  student
        Action:  retrieve
        Detail:  True
        Suffix:  Instance
        Name:  None
        Description:  None"""


        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        print("---- Create ----")
        print("Basename: " , self.basename)
        print("Action: " , self.action)
        print("Detail: " , self.detail)
        print("Suffix: " , self.suffix)
        print("Name: " , self.name)
        print("Description: " , self.description)
        print("------------------>>>>>>>>>>>>>")

        """---- Create ----
        Basename:  student
        Action:  create
        Detail:  False
        Suffix:  List
        Name:  None
        Description:  None
        ------------------>>>>>>>>>>>>>"""

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        print("---- update ----")
        print("Basename: " , self.basename)
        print("Action: " , self.action)
        print("Detail: " , self.detail)
        print("Suffix: " , self.suffix)
        print("Name: " , self.name)
        print("Description: " , self.description)
        print("------------------>>>>>>>>>>>>>")
        """
        ---- update ----
        Basename:  student
        Action:  update
        Detail:  True
        Suffix:  Instance
        Name:  None
        Description:  None
        ------------------>>>>>>>>>>>>>
        """
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk):
        print("---- Partial update ----")
        print("Basename: " , self.basename)
        print("Action: " , self.action)
        print("Detail: " , self.detail)
        print("Suffix: " , self.suffix)
        print("Name: " , self.name)
        print("Description: " , self.description)
        print("------------------>>>>>>>>>>>>>")
        """---- Partial update ----
        Basename:  student
        Action:  partial_update
        Detail:  True
        Suffix:  Instance
        Name:  None
        Description:  None
        ------------------>>>>>>>>>>>>>"""


        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        print("---- Destroy ----")
        print("Basename: " , self.basename)
        print("Action: " , self.action)
        print("Detail: " , self.detail)
        print("Suffix: " , self.suffix)
        print("Name: " , self.name)
        print("Description: " , self.description)
        print("------------------>>>>>>>>>>>>>")
        """---- Destroy ----
        Basename:  student
        Action:  destroy
        Detail:  True
        Suffix:  Instance
        Name:  None
        Description:  None
        ------------------>>>>>>>>>>>>>"""


        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted'})



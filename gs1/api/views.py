from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.

# Model Object- single student data

def student_detail(request, val):
    stu = Student.objects.get(id=val)
    #print(stu)
    serializer = StudentSerializer(stu)
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data, content_type='application/json')
    #return JsonResponse(serializer.data)

# queryset --- all student data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    #return JsonResponse(serializer.data, safe=False) # by default safe=True, but will throw error because serializer.data is not dict here




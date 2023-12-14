from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Application1.serializers import EmployeeSerializer
from Application1.models import Employees

@csrf_exempt
def EmployeeApi(request,id=0):
    if request.method=='GET':
        employee=Employees.objects.all()
        employees_serializer=EmployeeSerializer(employee,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employees_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employees_data=JSONParser().parse(request)
        employee=Employees.objects.get(id=id)
        employees_data_serializer=EmployeeSerializer(employee,data=employees_data)
        if employees_data_serializer.is_valid():
            employees_data_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employees.objects.get(id=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)
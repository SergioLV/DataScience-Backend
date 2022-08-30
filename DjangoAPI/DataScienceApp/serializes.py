'''
This section allows to transform django's models into JSON structures
'''

from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

#class DepartmentSerializer(serializers.ModelSerializer):
#    class Meta:
#        model=Departments
#        fields=('DepartmentId', 'DepartmentName')
#
#class EmployeeSerializer(serializers.ModelSerializer):
#    class Meta:
#        model=Employees
#        fields=('EmployeeId', 'EmployeeName','Department', 'DateOfJoining', 'PhotoFileName')
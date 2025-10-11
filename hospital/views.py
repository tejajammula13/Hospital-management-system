<<<<<<< HEAD
from rest_framework import viewsets, filters
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes=[DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['specialization','contact_number']
    search_fields = ['name', 'specialization']
    ordering_fields = ['name','specialization']
    ordering = ['name']

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['age','gender',"is_active"]
    search_fields = ['name']
    ordering_fields = ['name']
    #ordering = ['name']
    permission_classes=[DjangoModelPermissions]


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    permission_classes=[DjangoModelPermissions]
    filterset_fields = ['appointment_date']
    ordering_fields = ['appointment_date']

=======
from rest_framework import viewsets, filters
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes=[DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['specialization']
    search_fields = ['name', 'specialization']

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','age']
    permission_classes=[DjangoModelPermissions]


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes=[DjangoModelPermissions]
    filterset_fields = ['appointment_date']

>>>>>>> d2692dd19244e7c85cd7ca2f684633d8dbe204e0

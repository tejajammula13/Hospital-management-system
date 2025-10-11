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


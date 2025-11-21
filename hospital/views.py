from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Doctor, Patient, Appointment

from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer

from .permissions import (
    IsAdmin,
    IsDoctor,
    IsReceptionist,
    IsAdminOrDoctorOrReceptionist,
    IsAdminOrReceptionist,
)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['specialization', 'contact_number']
    search_fields = ['name', 'specialization']
    ordering_fields = ['name', 'specialization']

    def get_queryset(self):
        user = self.request.user

        # Admin → can see all doctors
        if user.is_superuser or user.groups.filter(name='Admin').exists():
            return Doctor.objects.all()

        # Doctor → can see only their own profile
        elif user.groups.filter(name='Doctor').exists():
            return Doctor.objects.filter(name=user.username)

        # Receptionist → can view all doctors
        elif user.groups.filter(name='Receptionist').exists():
            return Doctor.objects.all()

        return Doctor.objects.none()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAdminOrDoctorOrReceptionist()]
        elif self.request.method == 'POST':
            return [IsAdmin()]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdmin()]
        return super().get_permissions()


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['age', 'gender', 'is_active','name']
    search_fields = ['name']
    ordering_fields = ['name']

    def get_queryset(self):
        user = self.request.user

        # Admin → can view all patients
        if user.is_superuser or user.groups.filter(name='Admin').exists():
            return Patient.objects.all()

        # Receptionist → can view all (for managing appointments)
        elif user.groups.filter(name='Receptionist').exists():
            return Patient.objects.all()

        # Doctor → can view all
        elif user.groups.filter(name='Doctor').exists():
            return Patient.objects.all()

        return Patient.objects.none()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAdminOrDoctorOrReceptionist()]
        elif self.request.method == 'POST':
            return [IsAdminOrReceptionist()]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdmin()]
        return super().get_permissions()

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['appointment_date']
    ordering_fields = ['appointment_date']

    def get_queryset(self):
        user = self.request.user

        
        if user.is_superuser or user.groups.filter(name='Admin').exists():
            return Appointment.objects.all()

        
        elif user.groups.filter(name='Doctor').exists():
            try:
                return Appointment.objects.filter(doctor=user.doctor_profile)
            except Doctor.DoesNotExist:
                return Appointment.objects.none()

        
        elif user.groups.filter(name='Receptionist').exists():
            return Appointment.objects.all()

        return Appointment.objects.none()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAdminOrDoctorOrReceptionist()]
        elif self.request.method == 'POST':
            return [IsAdminOrReceptionist()]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdmin()]
        return super().get_permissions()

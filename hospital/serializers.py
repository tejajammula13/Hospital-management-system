<<<<<<< HEAD
from rest_framework import serializers
from .models import Doctor, Patient, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()
    doctor_name = serializers.SerializerMethodField()
    class Meta:
        model = Appointment
        fields = ["id","appointment_date",'appointment_time','symptoms','created_time',
                  'updated_time','patient_name','doctor_name']

    def get_patient_name(self,obj):
        return obj.patient.name
    
    def get_doctor_name(self,obj):
        return obj.doctor.name


    def validate(self, data):
        doctor = data['doctor']
        date = data['appointment_date']
        time = data['appointment_time']

        if Appointment.objects.filter(
            doctor=doctor,
            appointment_date=date,
            appointment_time=time
            ).exists():
            raise serializers.ValidationError(
                f"{doctor.name} is already booked at {time} on {date}.")

        return data
=======
from rest_framework import serializers
from .models import Doctor, Patient, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
>>>>>>> d2692dd19244e7c85cd7ca2f684633d8dbe204e0

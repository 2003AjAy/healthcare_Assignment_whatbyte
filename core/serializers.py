from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping

class PatientSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('id','owner','created_at')

class DoctorSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.email')
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ('id','created_at','created_by')

class MappingSerializer(serializers.ModelSerializer):
    assigned_by = serializers.ReadOnlyField(source='assigned_by.email')
    patient_detail = PatientSerializer(source='patient', read_only=True)
    doctor_detail = DoctorSerializer(source='doctor', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ('id', 'patient', 'patient_detail', 'doctor', 'doctor_detail', 'assigned_by', 'created_at')
        read_only_fields = ('id','assigned_by','created_at')

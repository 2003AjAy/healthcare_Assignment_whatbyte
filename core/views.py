from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import PatientSerializer, DoctorSerializer, MappingSerializer
from .permissions import IsOwnerOrReadOnly

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # only patients created by the authenticated user
        return Patient.objects.filter(owner=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Doctor.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class MappingViewSet(viewsets.ModelViewSet):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # show mappings related to patients owned by the user
        return PatientDoctorMapping.objects.filter(patient__owner=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        patient = serializer.validated_data['patient']
        # make sure user owns the patient
        if patient.owner != self.request.user:
            return Response({'detail': 'You can only assign doctors to your own patients.'}, status=status.HTTP_403_FORBIDDEN)
        serializer.save(assigned_by=self.request.user)

    # map GET /api/mappings/<patient_id>/ to get doctors for that patient
    @action(detail=False, methods=['get'], url_path=r'(?P<patient_id>\d+)')
    def doctors_for_patient(self, request, patient_id=None):
        mappings = self.get_queryset().filter(patient__id=patient_id)
        serializer = self.get_serializer(mappings, many=True)
        return Response(serializer.data)

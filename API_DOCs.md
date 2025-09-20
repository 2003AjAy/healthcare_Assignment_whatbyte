# Healthcare Backend API Documentation

## Authentication
- POST /api/auth/token/ → Get JWT token
- POST /api/auth/token/refresh/ → Refresh JWT token

## Patients
- GET /api/patients/ → List patients
- POST /api/patients/ → Create patient
- GET /api/patients/{id}/ → Retrieve patient
- PUT /api/patients/{id}/ → Update patient
- DELETE /api/patients/{id}/ → Delete patient

## Doctors
- GET /api/doctors/ → List doctors
- POST /api/doctors/ → Create doctor
- GET /api/doctors/{id}/ → Retrieve doctor
- PUT /api/doctors/{id}/ → Update doctor
- DELETE /api/doctors/{id}/ → Delete doctor

## Mapping (Patient-Doctor)
- GET /api/mappings/ → List mappings
- POST /api/mappings/ → Create mapping

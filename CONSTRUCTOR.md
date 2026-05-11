```md
# TELEMEDICINE PROJECT INSTRUCTIONS

## IMPORTANT

DO NOT create new Django apps or unnecessary directories.

Work ONLY with the current project structure.

DO NOT refactor the architecture.

DO NOT convert the project into enterprise architecture.

ONLY implement the minimum functionality required for the system to work correctly.

---

# REQUIRED STACK

- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Swagger with drf-spectacular

---

# CURRENT PROJECT STRUCTURE

api/
authentication/
medical/
transactions/
users/

Do NOT create additional apps unless technically required for functionality.

---

# GOAL

Complete a functional telemedicine REST API.

---

# EXISTING MODELS

## medical/models.py

The file should contain:

- Speciality
- Doctor
- DoctorSchedule
- Patient
- Appointment
- MedicalRecord
- Prescription
- PrescriptionDetail
- Medication
- ClinicalFile

Use proper ForeignKey and OneToOneField relationships.

Do NOT duplicate information.

Do NOT use CharField for relationships.

---

# FUNCTIONAL REQUIREMENTS

## JWT Authentication

Required endpoints:

- login
- register
- refresh token

Use SimpleJWT.

---

# MINIMUM CRUD REQUIREMENTS

Implement functional CRUD endpoints for:

- doctors
- patients
- appointments
- medications

Use only:

- serializers.py
- views.py
- urls.py

Do NOT create additional abstraction layers.

---

# REQUIRED BUSINESS LOGIC

Appointment scheduling must:

- prevent past appointments
- prevent double-booking doctors
- validate doctor availability

This logic can be implemented directly inside serializers.py or views.py.

Creating services.py is NOT required.

---

# SWAGGER

Configure drf-spectacular.

The following endpoints must work:

/api/schema/
/api/docs/

---

# POSTGRESQL

Use .env variables for database connection.

---

# IMPORTANT CODE RULES

Keep the code SIMPLE.

NO overengineering.

NO Clean Architecture.

NO DDD.

NO Repository Pattern.

NO microservices.

Functional academic project first.

---

# ALLOWED ADDITIONS

Only add the following files if strictly necessary:

- missing urls.py
- missing serializers.py
- migrations

Avoid adding new directories.

---

# PRIORITY ORDER

1. Functionality
2. Basic testing success
3. Working endpoints
4. JWT authentication working
5. Swagger documentation working

Elegant architecture is NOT the priority.
```

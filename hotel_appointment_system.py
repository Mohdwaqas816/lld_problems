from enum import Enum

class AppointmentStatus(Enum):
    BOOKED = "BOOKED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"



class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Patient(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def __str__(self):
        return f"Patient({self.user_id}, {self.name})"
    
class Doctor(User):
    def __init__(self, user_id, name, specialization):
        super().__init__(user_id, name)
        self.specialization = specialization
        self.available_slots = []
        self.appointments = []

    def add_slot(self, slot):
        self.available_slots.append(slot)

    def get_available_slots(self):
        return [slot for slot in self.available_slots if not slot.is_booked]

    def __str__(self):
        return f"Doctor({self.name}, {self.specialization})"
    
class TimeSlot:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.is_booked = False

    def book(self):
        self.is_booked = True

    def free(self):
        self.is_booked = False

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

class Appointment:
    def __init__(self, patient, doctor, timeslot):
        self.patient = patient
        self.doctor = doctor
        self.timeslot = timeslot
        self.status = AppointmentStatus.BOOKED

    def cancel(self):
        self.status = AppointmentStatus.CANCELLED
        self.timeslot.free()

    def complete(self):
        self.status = AppointmentStatus.COMPLETED

    def __str__(self):
        return f"{self.patient.name} with {self.doctor.name} at {self.timeslot}"
    

class AppointmentManager:
    def __init__(self):
        self.appointments = []

    def book_appointment(self, patient, doctor, timeslot):
        if timeslot.is_booked:
            print("Slot already booked")
            return None
        appointment = Appointment(patient, doctor, timeslot)
        timeslot.book()
        doctor.appointments.append(appointment)
        self.appointments.append(appointment)
        print("Appointment booked successfully")
        return appointment

    def cancel_appointment(self, appointment):
        if appointment.status == AppointmentStatus.CANCELLED:
            print("Already cancelled")
            return
        appointment.cancel()
        print("Appointment cancelled")

    def get_doctor_appointments(self, doctor):
        return doctor.appointments
    
class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def list_doctors(self):
        for doctor in self.doctors:
            print(doctor)

class DoctorService:
    def __init__(self, doctors):
        self.doctors = doctors

    def search_by_specialization(self, specialization):
        result = []
        for doctor in self.doctors:
            if doctor.specialization.lower() == specialization.lower():
                result.append(doctor)
        return result
    
if __name__ == "__main__":

    hospital = Hospital("City Hospital")

    # Create doctors
    doctor1 = Doctor(1, "Dr Smith", "Cardiologist")
    doctor2 = Doctor(2, "Dr John", "Dentist")

    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)

    # Add slots
    slot1 = TimeSlot("10:00", "10:30")
    slot2 = TimeSlot("10:30", "11:00")

    doctor1.add_slot(slot1)
    doctor1.add_slot(slot2)

    # Create patient
    patient1 = Patient(1, "Rahul")
    hospital.add_patient(patient1)

    # Search doctor
    search_service = DoctorService(hospital.doctors)

    cardiologists = search_service.search_by_specialization("Cardiologist")

    print("Available Cardiologists:")
    for doc in cardiologists:
        print(doc)

    # Book appointment
    manager = AppointmentManager()

    appointment = manager.book_appointment(
        patient1,
        doctor1,
        slot1
    )

    print(appointment)

    # View doctor appointments
    print("\nDoctor Appointments:")

    for appt in manager.get_doctor_appointments(doctor1):
        print(appt)

    # Cancel appointment
    manager.cancel_appointment(appointment)

    print("Appointment status:", appointment.status)
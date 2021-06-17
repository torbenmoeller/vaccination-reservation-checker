from enum import auto, Enum


class Reservation(Enum):
    available = "Reservations are available"
    not_available = "Reservations are not available"

"""
Car Rental Management System (Assignment 5)
Author: Example Solution
"""

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Dict, Optional
import itertools


# -------------------------
# Utility ID generators
# -------------------------
def _id_generator(prefix: str):
    """Closure to generate simple incremental IDs with a prefix."""
    counter = itertools.count(1)
    while True:
        yield f"{prefix}{next(counter):04d}"


_vehicle_id_gen = _id_generator("V")
_customer_id_gen = _id_generator("C")
_booking_id_gen = _id_generator("B")


# -------------------------
# Vehicle (Abstract Base)
# -------------------------
class Vehicle(ABC):
    """Abstract base for vehicles in the fleet."""

    total_fleet_count = 0  

    def __init__(self, make: str, model: str, year: int, base_rate_per_day: float, odometer: float = 0.0):
        self._vehicle_id = next(_vehicle_id_gen)
        self._make = make
        self._model = model
        self._year = year
        self._base_rate_per_day = float(base_rate_per_day)
        self._is_available = True
        self._odometer = float(odometer)
        Vehicle.total_fleet_count += 1

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @property
    def is_available(self):
        return self._is_available

    def rent_out(self):
        if not self._is_available:
            raise RuntimeError("Vehicle is already rented.")
        self._is_available = False

    def return_vehicle(self, miles_driven: float = 0.0):
        """Mark vehicle as returned and update odometer."""
        self._odometer += float(miles_driven)
        self._is_available = True

    @abstractmethod
    def calculate_rental_price(self, days: int, **kwargs) -> float:
        """Calculate price for a given rental period. Implemented by subclasses."""
        pass

    @abstractmethod
    def display_info(self) -> str:
        """Return a short string describing the vehicle."""
        pass

    def __str__(self):
        return self.display_info()


# -------------------------
# Specific vehicle types
# -------------------------
class Car(Vehicle):
    """Passenger car."""

    def __init__(self, make, model, year, base_rate_per_day, seats=5, odometer=0.0):
        super().__init__(make, model, year, base_rate_per_day, odometer)
        self.seats = int(seats)

    def calculate_rental_price(self, days: int, gps: bool = False, child_seat: bool = False) -> float:
        if days < 1:
            raise ValueError("Days must be >= 1")
        extras_per_day = 0.0
        if gps:
            extras_per_day += 5.0
        if child_seat:
            extras_per_day += 3.0
        price = (self._base_rate_per_day + extras_per_day) * days
        if days >= 7:
            price *= 0.90  # 10% discount
        return round(price, 2)

    def display_info(self) -> str:
        avail = "Available" if self._is_available else "Rented"
        return f"Car {self.vehicle_id}: {self._make} {self._model} ({self._year}), seats={self.seats}, {avail}"


class Van(Vehicle):
    """Cargo van."""

    def __init__(self, make, model, year, base_rate_per_day, cargo_volume: float, odometer=0.0):
        super().__init__(make, model, year, base_rate_per_day, odometer)
        self.cargo_volume = float(cargo_volume)

    def calculate_rental_price(self, days: int, insurance: bool = True) -> float:
        if days < 1:
            raise ValueError("Days must be >= 1")
        price = (self._base_rate_per_day * 1.25) * days
        if insurance:
            price += 15.0 * days
        if self.cargo_volume >= 15 and days >= 5:
            price *= 0.92
        return round(price, 2)

    def display_info(self) -> str:
        avail = "Available" if self._is_available else "Rented"
        return f"Van {self.vehicle_id}: {self._make} {self._model} ({self._year}), cargo={self.cargo_volume}m³, {avail}"


class Motorcycle(Vehicle):
    """Motorcycle."""

    def __init__(self, make, model, year, base_rate_per_day, engine_cc: int, odometer=0.0):
        super().__init__(make, model, year, base_rate_per_day, odometer)
        self.engine_cc = int(engine_cc)

    def calculate_rental_price(self, days: int, helmet_included: bool = True) -> float:
        if days < 1:
            raise ValueError("Days must be >= 1")
        price = self._base_rate_per_day * days
        if not helmet_included:
            price += 2.0 * days
        if days >= 10:
            price *= 0.95
        return round(price, 2)

    def display_info(self) -> str:
        avail = "Available" if self._is_available else "Rented"
        return f"Motorcycle {self.vehicle_id}: {self._make} {self._model} ({self._year}), {self.engine_cc}cc, {avail}"


# -------------------------
# Customer class
# -------------------------
class Customer:
    """Represents a customer."""

    def __init__(self, name: str, phone: str, email: str):
        self._customer_id = next(_customer_id_gen)
        self.name = name
        self._phone = phone
        self.email = email
        self.registered_on = datetime.now()

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def phone(self):
        return self._phone

    def display_info(self) -> str:
        return f"Customer {self._customer_id}: {self.name}, {self.email}, phone={self._phone}"


# -------------------------
# Booking class
# -------------------------
class Booking:
    """Represents a booking."""

    def __init__(self, vehicle: Vehicle, customer: Customer, start_date: datetime, end_date: datetime, price_estimate: float):
        if end_date < start_date:
            raise ValueError("end_date must be >= start_date")
        self._booking_id = next(_booking_id_gen)
        self.vehicle = vehicle
        self.customer = customer
        self.start_date = start_date
        self.end_date = end_date
        self._price = float(price_estimate)
        self.is_active = True
        self.created_on = datetime.now()
        self.vehicle.rent_out()

    @property
    def booking_id(self):
        return self._booking_id

    @property
    def price(self):
        return self._price

    def close_booking(self, return_date: datetime, miles_driven: float = 0.0) -> float:
        if not self.is_active:
            raise RuntimeError("Booking already closed.")
        self.vehicle.return_vehicle(miles_driven)
        self.is_active = False

        expected_days = (self.end_date - self.start_date).days + 1
        actual_days = (return_date - self.start_date).days + 1
        extra_days = max(0, actual_days - expected_days)
        final_price = self._price
        if extra_days > 0:
            final_price += self.vehicle.calculate_rental_price(extra_days)
        if miles_driven > 100:
            extra_miles = miles_driven - 100
            final_price += round(extra_miles * 0.20, 2)
        self._price = round(final_price, 2)
        return self._price

    def display_info(self) -> str:
        status = "Active" if self.is_active else "Closed"
        return (f"Booking {self.booking_id}: vehicle={self.vehicle.vehicle_id}, "
                f"cust={self.customer.customer_id}, {self.start_date.date()} -> {self.end_date.date()}, "
                f"price={self._price}, status={status}")


# -------------------------
# RentalCompany Manager
# -------------------------
class RentalCompany:
    """Manager class."""

    total_revenue = 0.0

    def __init__(self, company_name: str):
        self.company_name = company_name
        self.vehicles: Dict[str, Vehicle] = {}
        self.customers: Dict[str, Customer] = {}
        self.bookings: Dict[str, Booking] = {}

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles[vehicle.vehicle_id] = vehicle
        print(f"[INFO] Added {vehicle}")

    def list_vehicles(self, only_available: bool = False):
        items = [v for v in self.vehicles.values() if (not only_available) or v.is_available]
        for v in items:
            print(v.display_info())
        if not items:
            print("No vehicles to show.")

    def find_vehicle_by_id(self, vid: str) -> Optional[Vehicle]:
        return self.vehicles.get(vid)

    def register_customer(self, name: str, phone: str, email: str) -> Customer:
        c = Customer(name, phone, email)
        self.customers[c.customer_id] = c
        print(f"[INFO] Registered {c.display_info()}")
        return c

    def find_customer_by_id(self, cid: str) -> Optional[Customer]:
        return self.customers.get(cid)

    def make_booking(self, vehicle_id: str, customer_id: str, start: datetime, end: datetime, **price_kwargs) -> Booking:
        vehicle = self.find_vehicle_by_id(vehicle_id)
        if vehicle is None:
            raise ValueError("Vehicle not found.")
        if not vehicle.is_available:
            raise RuntimeError("Vehicle not available.")
        customer = self.find_customer_by_id(customer_id)
        if customer is None:
            raise ValueError("Customer not found.")
        days = (end - start).days + 1
        price_estimate = vehicle.calculate_rental_price(days, **price_kwargs)
        booking = Booking(vehicle, customer, start, end, price_estimate)
        self.bookings[booking.booking_id] = booking
        print(f"[INFO] Booking created: {booking.display_info()}")
        return booking

    def return_vehicle(self, booking_id: str, return_date: datetime, miles_driven: float = 0.0) -> float:
        booking = self.bookings.get(booking_id)
        if booking is None:
            raise ValueError("Booking not found.")
        final_price = booking.close_booking(return_date, miles_driven)
        RentalCompany.total_revenue += final_price
        print(f"[INFO] Booking closed: {booking.display_info()}")
        return final_price

    def active_bookings(self):
        return [b for b in self.bookings.values() if b.is_active]

    def print_report(self):
        print("===== Rental Company Report =====")
        print(f"Company: {self.company_name}")
        print(f"Fleet size: {len(self.vehicles)} (total created: {Vehicle.total_fleet_count})")
        print(f"Customers: {len(self.customers)}")
        print(f"Active bookings: {len(self.active_bookings())}")
        print(f"Total revenue (collected): ${RentalCompany.total_revenue:.2f}")
        print("=================================")


# -------------------------
# Demo / CLI
# -------------------------
def demo_setup(company: RentalCompany):
    company.add_vehicle(Car("Toyota", "Corolla", 2020, 40.0, seats=5, odometer=12000))
    company.add_vehicle(Car("Honda", "City", 2019, 38.0, seats=5, odometer=23000))
    company.add_vehicle(Van("Ford", "Transit", 2018, 80.0, cargo_volume=16.0, odometer=70000))
    company.add_vehicle(Motorcycle("Yamaha", "MT-15", 2022, 25.0, engine_cc=155, odometer=5000))
    alice = company.register_customer("Alice Johnson", "555-0101", "alice@example.com")
    bob = company.register_customer("Bob Singh", "555-0202", "bob@example.com")
    return company, alice, bob


def sample_run():
    print("=== Sample Run ===")
    company = RentalCompany("FastWheels Rentals")
    company, alice, bob = demo_setup(company)

    print("\nAvailable vehicles:")
    company.list_vehicles(only_available=True)

    start = datetime.now().date()
    start_dt = datetime.combine(start, datetime.min.time())
    end_dt = start_dt + timedelta(days=2)
    car_id = next(v.vehicle_id for v in company.vehicles.values() if isinstance(v, Car) and v.is_available)
    booking = company.make_booking(car_id, alice.customer_id, start_dt, end_dt, gps=True)

    print("\nActive bookings:")
    for b in company.active_bookings():
        print(b.display_info())

    return_date = start_dt + timedelta(days=4)
    final_price = company.return_vehicle(booking.booking_id, return_date, miles_driven=150)
    print(f"\nFinal price for booking {booking.booking_id}: ${final_price}")

    company.print_report()
    print("=== End Sample ===")


def main_cli():
    comp = RentalCompany("MyRentalCo")
    demo_setup(comp)
    print("\nWelcome to", comp.company_name)
    menu = """
Choose an action:
1) List all vehicles
2) List available vehicles
3) Register customer
4) Make booking
5) Return vehicle
6) Show active bookings
7) Company report
0) Exit
"""
    while True:
        print(menu)
        choice = input("Enter choice: ").strip()
        if choice == "0":
            print("Thank you! ")
            break
        try:
            if choice == "1":
                comp.list_vehicles()
            elif choice == "2":
                comp.list_vehicles(only_available=True)
            elif choice == "3":
                name = input("Name: "); phone = input("Phone: "); email = input("Email: ")
                comp.register_customer(name, phone, email)
            elif choice == "4":
                vid = input("Vehicle ID: ")
                cid = input("Customer ID: ")
                sd = input("Start date (YYYY-MM-DD): ")
                ed = input("End date (YYYY-MM-DD): ")
                sd_dt = datetime.strptime(sd.strip(), "%Y-%m-%d")
                ed_dt = datetime.strptime(ed.strip(), "%Y-%m-%d")
                extras = {}
                vehicle = comp.find_vehicle_by_id(vid)
                if vehicle is None:
                    print("Vehicle not found.")
                    continue
                if isinstance(vehicle, Car):
                    gps = input("GPS? (y/n): ").lower().startswith("y")
                    child = input("Child seat? (y/n): ").lower().startswith("y")
                    extras = {"gps": gps, "child_seat": child}
                elif isinstance(vehicle, Van):
                    ins = input("Insurance? (y/n): ").lower().startswith("y")
                    extras = {"insurance": ins}
                elif isinstance(vehicle, Motorcycle):
                    helm = input("Helmet included? (y/n): ").lower().startswith("y")
                    extras = {"helmet_included": helm}
                booking = comp.make_booking(vid, cid, sd_dt, ed_dt, **extras)
                print("Created:", booking.display_info())
            elif choice == "5":
                bid = input("Booking ID: ")
                rd = input("Return date (YYYY-MM-DD): ")
                miles = float(input("Miles driven during rental: "))
                rd_dt = datetime.strptime(rd.strip(), "%Y-%m-%d")
                total = comp.return_vehicle(bid, rd_dt, miles)
                print(f"Total charged: ${total:.2f}")
            elif choice == "6":
                for b in comp.active_bookings():
                    print(b.display_info())
                if not comp.active_bookings():
                    print("None")
            elif choice == "7":
                comp.print_report()
            else:
                print("Unknown option.")
        except Exception as e:
            print("[ERROR]", e)


if __name__ == "__main__":
    main_cli()

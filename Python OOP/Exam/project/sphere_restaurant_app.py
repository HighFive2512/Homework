from typing import List
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient


class SphereRestaurantApp:
    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int) -> str:
        if waiter_type not in ["FullTimeWaiter", "HalfTimeWaiter"]:
            return f"{waiter_type} is not a recognized waiter type."

        if waiter_name in [waiter.name for waiter in self.waiters]:
            return f"{waiter_name} is already on the staff."

        if waiter_type == "FullTimeWaiter":
            waiter = FullTimeWaiter(waiter_name, hours_worked)
        else:
            waiter = HalfTimeWaiter(waiter_name, hours_worked)

        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str) -> str:
        if client_type not in ["RegularClient", "VIPClient"]:
            return f"{client_type} is not a recognized client type."

        if client_name in [client.name for client in self.clients]:
            return f"{client_name} is already a client."

        if client_type == "RegularClient":
            client = RegularClient(client_name)
        else:
            client = VIPClient(client_name)

        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str) -> str:
        waiter = next((w for w in self.waiters if w.name == waiter_name), None)
        if waiter is None:
            return f"No waiter found with the name {waiter_name}."

        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float) -> str:
        client = next((c for c in self.clients if c.name == client_name), None)
        if client is None:
            return f"{client_name} is not a registered client."

        points_earned = client.earning_points(order_amount)
        return f"{client_name} earned {points_earned} points from the order."

    def apply_discount_to_client(self, client_name: str) -> str:
        client = next((c for c in self.clients if c.name == client_name), None)
        if client is None:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount_percentage, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

    def generate_report(self) -> str:
        total_earnings = sum(w.calculate_earnings() for w in self.waiters)
        total_client_points = sum(c.points for c in self.clients)
        clients_count = len(self.clients)

        waiter_details = "\n".join(f"Name: {w.name}, Total earnings: ${w.calculate_earnings():.2f}" for w in sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True))

        return f"$$ Monthly Report $$\nTotal Earnings: ${total_earnings:.2f}\nTotal Clients Unused Points: {total_client_points}\nTotal Clients Count: {clients_count}\n** Waiter Details **\n{waiter_details}"


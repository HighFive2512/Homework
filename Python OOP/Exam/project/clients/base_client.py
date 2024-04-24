from abc import ABC, abstractmethod


class BaseClient(ABC):
    def __init__(self, name: str, membership_type: str):
        if not name.strip():
            raise ValueError("Client name should be determined!")
        self.name = name

        if membership_type not in ["Regular", "VIP"]:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.membership_type = membership_type

        self.points = 0

    @abstractmethod
    def earning_points(self, order_amount: int) -> int:
        pass

    @abstractmethod
    def apply_discount(self) -> tuple[int, int]:
        pass

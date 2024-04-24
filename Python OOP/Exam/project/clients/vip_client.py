from project.clients.base_client import BaseClient

class VIPClient(BaseClient):
    def __init__(self, name: str):
        super().__init__(name, "VIP")

    def earning_points(self, order_amount: int) -> int:
        earned_points = int(order_amount // 5)
        self.points += earned_points
        return earned_points

    def apply_discount(self) -> tuple[int, int]:
        if self.points >= 100:
            discount_percentage = 10
            used_points = 100
        elif 50 <= self.points < 100:
            discount_percentage = 5
            used_points = 50
        else:
            discount_percentage = 0
            used_points = 0

        self.points -= used_points
        return discount_percentage, self.points

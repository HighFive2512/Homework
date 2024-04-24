from project.waiters.base_waiter import BaseWaiter

class HalfTimeWaiter(BaseWaiter):
    HOURLY_WAGE = 12.0

    def calculate_earnings(self) -> float:
        return self.hours_worked * HalfTimeWaiter.HOURLY_WAGE

    def report_shift(self) -> str:
        return f"{self.name} worked a half-time shift of {self.hours_worked} hours."

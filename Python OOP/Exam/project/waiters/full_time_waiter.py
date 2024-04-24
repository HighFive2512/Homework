from project.waiters.base_waiter import BaseWaiter

class FullTimeWaiter(BaseWaiter):
    HOURLY_WAGE = 15.0

    def calculate_earnings(self) -> float:
        return self.hours_worked * FullTimeWaiter.HOURLY_WAGE

    def report_shift(self) -> str:
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."

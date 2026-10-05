class Trousers:
    """Класс для расчета параметров брюк."""

    def __init__(self, size: int, fabric_price: float, fitting_cost: float = 350.0, base_work_cost: float = 2200.0):
        self.size = size
        self.fabric_price = fabric_price
        self.fitting_cost = fitting_cost
        self.base_work_cost = base_work_cost

    def calculate_fabric_consumption(self) -> float:
        # Базовый расход на 48 размер — 1.3 м, коэф. масштабирования 2.5% за размер
        base_meters = 1.3
        factor = 1.0 + (self.size - 48) * 0.025
        return round(base_meters * factor, 2)

    def calculate_total_cost(self) -> float:
        fabric_cost = self.calculate_fabric_consumption() * self.fabric_price
        return round(fabric_cost + self.fitting_cost + self.base_work_cost, 2)

    def get_info(self) -> dict:
        return {
            "item": "Брюки",
            "size": self.size,
            "fabric_consumption_m": self.calculate_fabric_consumption(),
            "fabric_price_per_m": self.fabric_price,
            "fitting_cost": self.fitting_cost,
            "work_cost": self.base_work_cost,
            "total_cost": self.calculate_total_cost()
        }
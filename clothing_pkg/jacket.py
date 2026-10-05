class Jacket:
    """Класс для расчета параметров пиджака."""

    def __init__(self, size: int, fabric_price: float, fitting_cost: float = 600.0, base_work_cost: float = 3500.0):
        self.size = size
        self.fabric_price = fabric_price
        self.fitting_cost = fitting_cost
        self.base_work_cost = base_work_cost

    def calculate_fabric_consumption(self) -> float:
        # Базовый расход на 48 размер — 1.8 м, с ростом размера добавляем по 3% за размер
        base_meters = 1.8
        factor = 1.0 + (self.size - 48) * 0.03
        return round(base_meters * factor, 2)

    def calculate_total_cost(self) -> float:
        fabric_cost = self.calculate_fabric_consumption() * self.fabric_price
        return round(fabric_cost + self.fitting_cost + self.base_work_cost, 2)

    def get_info(self) -> dict:
        return {
            "item": "Пиджак",
            "size": self.size,
            "fabric_consumption_m": self.calculate_fabric_consumption(),
            "fabric_price_per_m": self.fabric_price,
            "fitting_cost": self.fitting_cost,
            "work_cost": self.base_work_cost,
            "total_cost": self.calculate_total_cost()
        }
from .jacket import Jacket
from .trousers import Trousers

class ThreePieceSuit:
    """Класс для расчета костюма-тройки (пиджак, брюки, жилет)."""

    def __init__(self, size: int, fabric_price: float, fitting_cost: float = 1200.0, base_work_cost: float = 7000.0):
        self.size = size
        self.fabric_price = fabric_price
        self.fitting_cost = fitting_cost
        self.base_work_cost = base_work_cost
        # Включаем компоненты для расчета
        self.jacket_part = Jacket(size, fabric_price)
        self.trousers_part = Trousers(size, fabric_price)

    def calculate_fabric_consumption(self) -> float:
        # Пиджак + брюки + жилет (~0.9 м с поправкой)
        vest_factor = 1.0 + (self.size - 48) * 0.02
        vest_meters = 0.9 * vest_factor
        total = self.jacket_part.calculate_fabric_consumption() + self.trousers_part.calculate_fabric_consumption() + vest_meters
        return round(total, 2)

    def calculate_total_cost(self) -> float:
        fabric_cost = self.calculate_fabric_consumption() * self.fabric_price
        return round(fabric_cost + self.fitting_cost + self.base_work_cost, 2)

    def get_info(self) -> dict:
        return {
            "item": "Костюм-тройка",
            "size": self.size,
            "fabric_consumption_m": self.calculate_fabric_consumption(),
            "fabric_price_per_m": self.fabric_price,
            "fitting_cost": self.fitting_cost,
            "work_cost": self.base_work_cost,
            "total_cost": self.calculate_total_cost()
        }
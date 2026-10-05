from openpyxl import Workbook
from clothing_pkg import Jacket, Trousers, ThreePieceSuit

def save_to_excel(results: list, filename: str = "clothing_report.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Расчет пошива"

    headers = [
        "Изделие",
        "Размер",
        "Расход ткани (м)",
        "Цена ткани (руб/м)",
        "Стоимость фурнитуры (руб)",
        "Работа (руб)",
        "Итоговая стоимость (руб)"
    ]
    ws.append(headers)

    for item in results:
        ws.append([
            item["item"],
            item["size"],
            item["fabric_consumption_m"],
            item["fabric_price_per_m"],
            item["fitting_cost"],
            item["work_cost"],
            item["total_cost"]
        ])

    wb.save(filename)
    print(f"\n[OK] Результаты сохранены в файл: {filename}")

def main():
    calculations = []
    print("=" * 55)
    print("  Калькулятор расхода ткани и расчета стоимости пошива")
    print("=" * 55)

    while True:
        print("\nВыберите тип изделия:")
        print("1. Пиджак")
        print("2. Брюки")
        print("3. Костюм-тройка")
        print("0. Выход и сохранение отчёта")

        choice = input("Введите пункт меню: ").strip()
        if choice == "0":
            break

        if choice not in ("1", "2", "3"):
            print("Неверный пункт. Попробуйте еще раз.")
            continue

        try:
            size = int(input("Введите размер одежды (например, 44 - 60): "))
            price = float(input("Введите стоимость 1 метра ткани (руб): "))
            if size <= 0 or price <= 0:
                print("Значения должны быть больше нуля.")
                continue
        except ValueError:
            print("Ошибка: нужно ввести числовое значение.")
            continue

        if choice == "1":
            order = Jacket(size=size, fabric_price=price)
        elif choice == "2":
            order = Trousers(size=size, fabric_price=price)
        else:
            order = ThreePieceSuit(size=size, fabric_price=price)

        info = order.get_info()
        calculations.append(info)

        print("\n--- Результат расчёта ---")
        print(f"Изделие: {info['item']}")
        print(f"Размер: {info['size']}")
        print(f"Требуемый метраж ткани: {info['fabric_consumption_m']} м")
        print(f"Стоимость фурнитуры: {info['fitting_cost']} руб.")
        print(f"Стоимость пошива (работа): {info['work_cost']} руб.")
        print(f"Итоговая цена: {info['total_cost']} руб.")

    if calculations:
        save_choice = input("\nСохранить расчёты в Excel (.xlsx)? (y/n): ").strip().lower()
        if save_choice in ("y", "yes", "д", "да"):
            save_to_excel(calculations)
    else:
        print("Расчётов не было. Программа завершена.")

if __name__ == "__main__":
    main()
# Проект FitLife - MVP версия 1.0

try:
    # 1. Знакомство
    user_name = input("Введите ваше имя: ").strip()
    if not user_name:
        print("Имя не может быть пустым.")
        exit()

    user_age = int(input("Введите ваш возраст (целое число): "))

    # 2. Сбор данных
    user_weight = float(input("Введите ваш вес в кг (например, 70.5): "))
    user_height = float(input("Введите ваш рост в метрах (например, 1.75): "))
except ValueError:
    print("Ошибка: вы ввели не число там, где нужно число. ""Запустите программу заново.")
    exit()

# 3. Логика расчетов
bmi = user_weight / (user_height ** 2)
water_needed = (user_weight * 30) / 1000

bmi_rounded = round(bmi, 1)
water_rounded = round(water_needed, 1)

# 4. Вывод красивого результата
print(f"\nПривет, {user_name}!")
print(f"Ваш возраст: {user_age} лет")
print(f"Ваш ИМТ: {bmi_rounded}")
print(f"Рекомендуемая норма воды: {water_rounded:.1f} л в день")

print("Расчет окончен. Будьте здоровы!")

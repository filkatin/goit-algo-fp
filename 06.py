# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_calories = 0
    selected_items = []
    
    for item, details in sorted_items:
        if budget >= details["cost"]:
            budget -= details["cost"]
            total_calories += details["calories"]
            selected_items.append(item)
    
    return selected_items, total_calories


# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    # Список назв страв і їхні вартості та калорійності
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    
    n = len(names)
    # Ініціалізація таблиці DP
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнюємо таблицю DP
    for i in range(1, n + 1):
        for b in range(1, budget + 1):
            if costs[i - 1] <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][b] = dp[i - 1][b]

    # Визначаємо обрані страви
    total_calories = dp[n][budget]
    selected_items = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_items.append(names[i - 1])
            b -= costs[i - 1]

    return selected_items, total_calories


# Приклад використання
budget = 100

# Жадібний алгоритм
greedy_selection, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_selection)
print("Загальна калорійність:", greedy_calories)

# Алгоритм динамічного програмування
dp_selection, dp_calories = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Вибрані страви:", dp_selection)
print("Загальна калорійність:", dp_calories)

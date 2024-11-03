import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків двох кубиків
def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}  # Ініціалізація підрахунку сум

    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total_sum = roll1 + roll2
        sums_count[total_sum] += 1

    # Обчислення ймовірностей
    probabilities = {s: count / num_rolls for s, count in sums_count.items()}
    return probabilities

# Виконання симуляції
num_rolls = 1000000  # Велика кількість кидків для точності
probabilities = simulate_dice_rolls(num_rolls)

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36
}

print("Імовірності сум за методом Монте-Карло та аналітичні дані:")
for s in range(2, 13):
    monte_carlo_prob = probabilities[s] * 100
    analytical_prob = analytical_probabilities[s] * 100
    print(f"Сума {s}: Монте-Карло - {monte_carlo_prob:.2f}% Аналітична - {analytical_prob:.2f}%")

# Створення графіку
sums = list(probabilities.keys())
simulation_probs = [probabilities[s] * 100 for s in sums]
analytical_probs = [analytical_probabilities[s] * 100 for s in sums]

plt.figure(figsize=(10, 6))
plt.bar(sums, simulation_probs, alpha=0.6, label="Метод Монте-Карло", color='blue')
plt.plot(sums, analytical_probs, color='red', marker='o', label="Аналітичні розрахунки")
plt.xlabel("Сума чисел на кубиках")
plt.ylabel("Імовірність (%)")
plt.title("Імовірності сум при киданні двох кубиків")
plt.legend()
plt.show()

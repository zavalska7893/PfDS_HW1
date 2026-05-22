import random

# 1. Створення масиву 3x3 з випадкових чисел від 1 до 100
print("Двовимірний масив 3x3")

matrix = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]

print("\nВихідний масив:")
for row in matrix:
    print(row)

# 2. Сума всіх елементів
total = sum(matrix[i][j] for i in range(3) for j in range(3))
print(f"\nСума всіх елементів: {total}")

# 3. Максимальне та мінімальне значення з індексами
max_val = matrix[0][0]
min_val = matrix[0][0]
max_idx = (0, 0)
min_idx = (0, 0)

for i in range(3):
    for j in range(3):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_idx = (i, j)
        if matrix[i][j] < min_val:
            min_val = matrix[i][j]
            min_idx = (i, j)

print(f"\nМаксимальне значення: {max_val}, індекс: [{max_idx[0]}, {max_idx[1]}]")
print(f"Мінімальне значення: {min_val}, індекс: [{min_idx[0]}, {min_idx[1]}]")

# 4. Сортування кожного рядка
print("\nМасив після сортування кожного рядка:")
sorted_matrix = [sorted(row) for row in matrix]
for row in sorted_matrix:
    print(row)
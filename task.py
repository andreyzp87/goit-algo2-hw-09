import random
import math


def sphere_function(x):
    return sum(xi ** 2 for xi in x)


def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current = [random.uniform(min_val, max_val) for min_val, max_val in bounds]
    current_value = func(current)

    for _ in range(iterations):
        neighbor = [
            x + random.gauss(0, 0.1)
            for x in current
        ]

        neighbor = [
            min(max(x, min_val), max_val)
            for x, (min_val, max_val) in zip(neighbor, bounds)
        ]

        neighbor_value = func(neighbor)

        if neighbor_value < current_value:
            if abs(neighbor_value - current_value) < epsilon:
                break

            current = neighbor
            current_value = neighbor_value

    return current, current_value


def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best = [random.uniform(min_val, max_val) for min_val, max_val in bounds]
    best_value = func(best)

    for _ in range(iterations):
        candidate = [random.uniform(min_val, max_val) for min_val, max_val in bounds]
        candidate_value = func(candidate)

        if candidate_value < best_value:
            if abs(candidate_value - best_value) < epsilon:
                break

            best = candidate
            best_value = candidate_value

    return best, best_value


def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current = [random.uniform(min_val, max_val) for min_val, max_val in bounds]
    current_value = func(current)

    best = current[:]
    best_value = current_value

    for _ in range(iterations):
        if temp < epsilon:
            break

        neighbor = [
            x + random.gauss(0, 0.1) * temp
            for x in current
        ]

        neighbor = [
            min(max(x, min_val), max_val)
            for x, (min_val, max_val) in zip(neighbor, bounds)
        ]

        neighbor_value = func(neighbor)

        delta_e = neighbor_value - current_value

        if (delta_e < 0) or (random.random() < math.exp(-delta_e / temp)):
            current = neighbor
            current_value = neighbor_value

            if current_value < best_value:
                if abs(current_value - best_value) < epsilon:  # Перевірка на збіжність
                    break
                best = current[:]
                best_value = current_value

        temp *= cooling_rate

    return best, best_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
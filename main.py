from dynamic_array.dynamic_array import DynamicArray

if __name__ == '__main__':
    aa = DynamicArray()
    aa.append(10000)

    student = 7

    def run_experiment(n_elements, initial_capacity, strategy):
        array = DynamicArray(initial_capacity, strategy, student)

        total_unused = 0
        count = 0

        for idx in range(n_elements):
            array.append(idx)
            total_unused += array.get_unused()
            count += 1

        avg_unused = total_unused / count
        avg_unused_percent = (avg_unused / n_elements) * 100

        return {
            'resize_count': array.resize_count,
            'avg_unused': avg_unused,
            'avg_unused_percent': avg_unused_percent,
            'final_unused': array.get_unused()
        }

    # Запускаємо експерименти
    print("n_elements | init_cap | strategy | resizes | avg_unused | avg_%")
    print("-" * 70)

    for n in [10_000, 100_000, 1_000_000]:
        for cap in [8, 32, 128]:
            for strat in [1, 2, 3]:
                result = run_experiment(n, cap, strat)
                print(f"{n:10} | {cap:8} | {strat:8} | {result['resize_count']:7} | "
                      f"{result['avg_unused']:10.1f} | {result['avg_unused_percent']:6.2f}%")

    print("\n" + "="*70)
    print("ТЕСТИ ДОДАТКОВИХ ФУНКЦІЙ")
    print("="*70)

    # Тест len()
    test_arr = DynamicArray()
    for j in range(10):
        test_arr.append(j * 10)

    print(f"\n1. len(arr) = {len(test_arr)} (очікується: 10)")

    # Тест arr[index]
    print(f"2. arr[3] = {test_arr[3]} (очікується: 30)")

    # Тест arr[index] = value
    test_arr[3] = 999
    print(f"3. Після arr[3] = 999: arr[3] = {test_arr[3]} (очікується: 999)")

    # Тест ітерації
    print("4. Ітерація через for:")
    print("   ", end="")
    for value in test_arr:
        print(value, end=" ")
    print("\n   (очікується: 0 10 20 999 40 50 60 70 80 90)")

    print("\n Всі тести завершено!")
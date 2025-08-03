from sorts import *


def test_sorting_algorithms():
    test_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = sorted(test_array)  # Встроенная сортировка Python для сравнения

    print(f"Исходный массив: {test_array}")
    print(f"Ожидаемый результат: {sorted_array}\n")

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort
    }

    for name, algorithm in algorithms.items():
        arr = test_array.copy()
        result = algorithm(arr)
        print(f"{name}: {result} {'✓' if result == sorted_array else '✗'}")


if __name__ == "__main__":
    test_sorting_algorithms()
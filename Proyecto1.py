
import time
import random

# Algoritmo de ordenamiento - Bubble Sort (Ordenamiento Burbuja)
# Complejidad de Tiempo: O(n^2)
# Complejidad de Espacio: O(1)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Algoritmo de ordenamiento - Quick Sort (Ordenamiento Rápido)
# Complejidad de Tiempo: O(n log n)
# Complejidad de Espacio: O(n)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Algoritmo de ordenamiento - Counting Sort (Ordenamiento por Cuenta)
# Complejidad de Tiempo: O(n + k) donde k es el rango de los números en la lista
# Complejidad de Espacio: O(k)
def counting_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    count = [0] * (max_num - min_num + 1)
    for num in arr:
        count[num - min_num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr += [i + min_num] * count[i]
    return sorted_arr

# Algoritmo de ordenamiento - Bucket Sort (Ordenamiento por Banderas)
# Complejidad de Tiempo: O(n^2) en el peor caso, pero puede ser lineal en promedio
# Complejidad de Espacio: O(n)
def bucket_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    buckets = [[] for _ in range((max_num - min_num) // 10 + 1)]  # Ajusta el número de baldes
    for num in arr:
        index = (num - min_num) // 10
        buckets[index].append(num)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += sorted(bucket)
    return sorted_arr

# Función para generar una matriz aleatoria de un tamaño dado
def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]  # Limita el rango a 1-100

# Función para generar una matriz casi ordenada de un tamaño dado
def generate_almost_sorted_array(size):
    array = [i for i in range(1, size + 1)]
    # Intercambiar algunos elementos para hacerlos casi ordenados
    for _ in range(size // 10):
        i, j = random.randint(0, size - 1), random.randint(0, size - 1)
        array[i], array[j] = array[j], array[i]
    return array

# Función para generar una matriz inversamente ordenada de un tamaño dado
def generate_reverse_sorted_array(size):
    return [i for i in range(size, 0, -1)]

# Función para realizar pruebas de benchmarking
def benchmark_algorithm(sort_function, array):
    start_time = time.time()
    sort_function(array)
    end_time = time.time()
    return end_time - start_time

# Tamaños de entrada
sizes = [10000, 50000, 100000, 150000]

# Algoritmos de ordenamiento
sorting_algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Quick Sort", quick_sort),
    ("Counting Sort", counting_sort),
    ("Bucket Sort", bucket_sort)
]

# Patrones de entrada
input_patterns = [
    ("Datos Aleatorios", generate_random_array),
    ("Datos Casi Ordenados", generate_almost_sorted_array),
    ("Datos Inversamente Ordenados", generate_reverse_sorted_array)
]


# Realizar pruebas de benchmarking para cada patrón y tamaño de entrada
for pattern_name, generate_data in input_patterns:
    print(f"\n{pattern_name}\n{'=' * (len(pattern_name) + 2)}")
    
    for size in sizes:
        print(f"\nTamaño de entrada: {size}")
        array = generate_data(size)

        for algorithm_name, algorithm_function in sorting_algorithms:
            array_copy = array.copy()
            time_taken = benchmark_algorithm(algorithm_function, array_copy)
            print(f"{algorithm_name}: {time_taken:.6f} segundos")

    print("\n" + "="*40 + "\n")

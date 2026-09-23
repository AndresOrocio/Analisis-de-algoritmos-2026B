##########################################################
#ordenamientos
##########################################################


def selection_sort(lista):
    """
    Ordenamiento por selección.
    Complejidad: O(N^2)
    """
    arr = lista.copy()
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def bubble_sort_brute_force(lista):
    """
    Ordenamiento Burbuja por fuerza bruta.
    Complejidad: O(N^2)
    """
    arr = lista.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def insertion_sort(lista):
    """
    Ordenamiento por Inserción.
    Complejidad: O(N^2)
    """
    arr = lista.copy()

    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = clave

    return arr


def gnome_sort(lista):
    """
    Ordenamiento Gnome.
    Complejidad promedio: O(N^2)
    """
    arr = lista.copy()
    i = 0
    n = len(arr)

    while i < n:
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

    return arr


def stooge_sort_rec(arr, l, h):
    """
    Función recursiva auxiliar para Stooge Sort.
    """
    if l >= h:
        return

    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]

    if h - l + 1 > 2:
        t = (h - l + 1) // 3

        stooge_sort_rec(arr, l, h - t)
        stooge_sort_rec(arr, l + t, h)
        stooge_sort_rec(arr, l, h - t)


def stooge_sort(lista):
    """
    Ordenamiento Stooge Sort.
    Complejidad aproximada: O(N^2.7095)
    """
    arr = lista.copy()

    if len(arr) > 0:
        stooge_sort_rec(arr, 0, len(arr) - 1)

    return arr


def exchange_sort(lista):
    """
    Ordenamiento por Intercambio Directo.
    Complejidad: O(N^2)
    """
    arr = lista.copy()
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr
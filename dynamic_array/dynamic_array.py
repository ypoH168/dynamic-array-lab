import ctypes
import math

class DynamicArray:
    def __init__(self, capacity=8, growth_strategy=1, student_number=1):
        self.capacity = capacity  # Розмір альбому
        self.size = 0  # Скільки наліпок вже є
        self.array = (capacity * ctypes.py_object)()  # Сам альбом
        self.growth_strategy = growth_strategy  # Яка стратегія зростання
        self.student_number = student_number  # Номер студента
        self.resize_count = 0  # Лічильник перевиділень

    def append(self, item):
        if self.size == self.capacity:  # Альбом заповнений?
            self._resize()  # Купи новий альбом!

        self.array[self.size] = item  # Додай наліпку
        self.size += 1

    def _resize(self):
        self.resize_count += 1  # Рахуємо перевиділення

        if self.growth_strategy == 1:
            # Стратегія 1: у 2 рази
            new_capacity = self.capacity * 2
        elif self.growth_strategy == 2:
            # Стратегія 2: номер/10 + 1
            growth_factor = 1 + self.student_number / 10
            new_capacity = int(self.capacity * growth_factor)
            if new_capacity == self.capacity:
                new_capacity = self.capacity + 1
        else:  # strategy 3
            # Стратегія 3: змінний коефіцієнт
            growth_factor = 1 + (self.student_number / 10) / math.log2(self.size + 2)
            new_capacity = int(self.capacity * growth_factor)
            if new_capacity == self.capacity:
                new_capacity = self.capacity + 1

        # Створи новий альбом
        new_array = (new_capacity * ctypes.py_object)()

        # Переклей усі наліпки
        for i in range(self.size):
            new_array[i] = self.array[i]

        # Заміни старий альбом новим
        self.array = new_array
        self.capacity = new_capacity

    def get_unused(self):
        return self.capacity - self.size

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def __setitem__(self, index, value):
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        self.array[index] = value

    def __iter__(self):
        for i in range(self.size):
            yield self.array[i]
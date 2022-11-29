import random
from random_words import RandomWords
import time

int_list = [random.randint(0, 1000) for _ in range(5000)]

float_list = [random.uniform(0.1, 100) for _ in range(5000)]

w = RandomWords()
str_list = w.random_words(count=5000)


def bubble_sort(data):
    length = len(data)
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length - iIndex - 1):
            if data[jIndex] > data[jIndex + 1]:
                data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
                swapped = True
        if not swapped:
            break
    # print("Bubble Sort: ", data)


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)


def time_reps_bubble(list_to_sort, reps):
    time_list = []
    for i in range(reps):
        start = time.time()
        bubble_sort(list_to_sort)
        time_list.append(time.time() - start)
    print(f'Mean time to run {type(list_to_sort[0])} = {sum(time_list) / reps}')


def time_reps_quick(list_to_sort, reps):
    time_list = []
    for i in range(reps):
        start = time.time()
        quick_sort(list_to_sort)
        time_list.append(time.time() - start)
    print(f'Mean time to run {type(list_to_sort[0])} = {sum(time_list) / reps}')


print('\nBubble time', '*'*30)
time_reps_bubble(int_list, 100)
time_reps_bubble(float_list, 100)
time_reps_bubble(str_list, 100)


print('\nQuick time', '*'*30)
time_reps_quick(int_list, 100)
time_reps_quick(float_list, 100)
time_reps_quick(str_list, 100)

import random
from random_words import RandomWords

int_list = [random.randint(0, 1000) for _ in range(5000)]
print(len(int_list))

float_list = [random.uniform(0.1, 100) for _ in range(5000)]
print(len(float_list))

w = RandomWords()
str_list = w.random_words(count=5000)
print(len(str_list))

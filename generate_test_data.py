import random

def generate_test_data(n):
    a = []
    for i in range(n):
        a.append(random.randint(0,999999))
    return a
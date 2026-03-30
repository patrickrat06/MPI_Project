
import random
import string

#integer generating

def generate_random_int(size, min_val=0, max_val=10000):
    return [random.randint(min_val, max_val) for _ in range(size)]

def generate_sorted_int(size, min_val=0, max_val=10000):
    return sorted(generate_random_int(size, min_val, max_val))

def generate_reverse_sorted_int(size, min_val=0, max_val=10000):
    return sorted(generate_random_int(size, min_val, max_val), reverse=True)

def generate_almost_sorted_int(size, percent_sorted=0.95, min_val=0, max_val=10000):
    data = sorted(generate_random_int(size, min_val, max_val))
    num_swaps = max(1, int(size * (1 - percent_sorted)))
    for _ in range(num_swaps):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        data[i], data[j] = data[j], data[i]
    return data

def generate_mixed_int(size, min_val=0, max_val=10000):
    half = size // 2
    sorted_half = sorted(generate_random_int(half, min_val, max_val))
    random_half = generate_random_int(size - half, min_val, max_val)
    return sorted_half + random_half

def generate_flat_int(size, num_distinct=5, min_val=0, max_val=5):
    values = [random.randint(min_val, max_val) for _ in range(num_distinct)]
    return [random.choice(values) for _ in range(size)]

#float generating

def generate_random_floats(size, min_val=0.0, max_val=10000.0):
    return [random.uniform(min_val, max_val) for _ in range(size)]

def generate_sorted_floats(size, min_val=0.0, max_val=10000.0):
    return sorted(generate_random_floats(size, min_val, max_val))

def generate_reverse_sorted_floats(size, min_val=0.0, max_val=10000.0):
    return sorted(generate_random_floats(size, min_val, max_val), reverse=True)

#string generating

def generate_random_strings(size, str_len=5):
    chars = string.ascii_lowercase
    return [''.join(random.choices(chars, k=str_len)) for _ in range(size)]

def generate_sorted_strings(size, str_len=5):
    return sorted(generate_random_strings(size, str_len))

def generate_reverse_sorted_strings(size, str_len=5):
    return sorted(generate_random_strings(size, str_len), reverse=True)

#dictionary for runner.py

INT_GENERATORS = {"random_int": generate_random_int,
                "sorted_int": generate_sorted_int,
                "reverse_sorted_int": generate_reverse_sorted_int,
                "almost_sorted_int": generate_almost_sorted_int,
                "mixed_int": generate_mixed_int,
                "flat_int": generate_flat_int}

FLOAT_GENERATORS = {"random_float": generate_random_floats,
                    "sorted_float": generate_sorted_floats,
                    "reverse_float": generate_reverse_sorted_floats}

STRING_GENERATORS = {"random_string": generate_random_strings,
                    "sorted_string": generate_sorted_strings,
                    "reverse_string": generate_reverse_sorted_strings}

#test

if __name__ == "__main__":
    for name, fn in INT_GENERATORS.items():
        sample = fn(10)
        print(f"{name:15} -> {sample}")
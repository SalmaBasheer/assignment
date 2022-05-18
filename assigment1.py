


def is_prime(n):
    
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def cons(n):
    
    initial = [True] * n
    initial[0] = initial[1] = False
    for (i, prime) in enumerate(initial):
        if prime:
            yield i
            for index in range(i * i, n, i):
                initial[index] = False

def make_prime_partitions(min_size):
    
    primes = cons(1000000)
    prime_sequence = [next(primes) for _ in range(min_size)]
    start_point = 0
    while start_point < len(prime_sequence):
        for i in range(start_point, min_size):
            yield prime_sequence[start_point: i + 1]
        start_point=start_point +1


def check_partitions(min_size=1000, max_total=1000000):
    """Assumes min_size is the minimum size of the initial prime sequence to generate
    and max total is the maximum total of consecutive prime sequences generated.
    generates sequences that sum up to less than max total."""
    prime_partitions = make_prime_partitions(min_size)
    for sequence in prime_partitions:
        if len(sequence) > min_size // 2:
            total = sum(sequence)
            if is_prime(total) and total <= max_total:
                yield sequence                


if __name__ == '__main__':
    all_sequences = check_partitions()
    longest_sequence = max(all_sequences, key=len)
    print(f'Maximum length: {len(longest_sequence)}')
    print(f'Maximum sum: {sum(longest_sequence)}')
               
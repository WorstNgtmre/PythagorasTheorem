def pythagoras_search(limit: int) -> list:
    triples = []
    for c in range(1, limit):
        for a in range(1, c):
            b = ((c ** 2) - (a ** 2)) ** 0.5
            if b == int(b) and a < b < c:
                triple = (a, int(b), c)
                triples.append(triple)

    return triples

def factorize(i: int):
    i_factors = []
    for n in range(1,i):
        if i % n == 0:
            i_factors.append(n)
    return i_factors

def gcd(triple: tuple) -> int:
    a,b,c = triple
    a_factors = factorize(a)
    b_factors = factorize(b)
    c_factors = factorize(c)
    common_factors = [f for f in a_factors if f in b_factors and f in c_factors]
    return max(common_factors) if common_factors else 1

def find_primitive_triples(triples: list) -> list:
    primitive_triples = []
    for triple in triples:
        if gcd(triple) == 1:
            primitive_triples.append(triple)
    return primitive_triples
        

while True:
    try:
        limit = int(input("Enter a limit for Pythagorean triples (or 0 to exit): "))
        if limit == 0:
            break
        triples = pythagoras_search(limit)
        print(f"Pythagorean triples up to {limit}: {triples}")
        print(f"Of which are primitives: {find_primitive_triples(triples)}")

    except ValueError:
        print("Please enter a valid integer.")
def is_quadratic_residue(z, p):
    return pow(z, (p - 1) // 2, p) == 1

def find_square_roots(z, p):
    roots = []
    for i in range(1, p):
        if (i * i) % p == z:
            roots.append(i)
    return roots

def main():
    p = 11
    print("Diem O")
    for x in range(p):
        z = (x ** 3 + x + 6) % p
        if is_quadratic_residue(z, p):
            print(f"Điểm trên E với x = {x}:")
            y_roots = find_square_roots(z, p)
            for y in y_roots:
                print(f"({x},{y})")
        else:
            print(f"Không có điểm trên E với x = {x}")

if __name__ == "__main__":
    main()


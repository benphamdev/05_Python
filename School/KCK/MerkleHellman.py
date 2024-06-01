def find_subset_sum(superincreasing_sequence, target_sum):
    n = len(superincreasing_sequence)
    subset = [0] * n
    for i in range(n - 1, -1, -1):
        if target_sum >= superincreasing_sequence[i]:
            subset[i] = 1
            target_sum -= superincreasing_sequence[i]
        elif target_sum == 0:
            break
    if target_sum != 0:
        return None
    return subset

def main():
    try:
        target_sum = int(input("s : "))
        superincreasing_sequence = list(map(int, input("Nhập dãy số nguyên superincreasing, cách nhau bởi dấu cách: ").split()))
        superincreasing_sequence.sort()  # Sắp xếp dãy số nguyên superincreasing
        subset = find_subset_sum(superincreasing_sequence, target_sum)
        if subset:
            for i, num in enumerate(subset):
                if num:
                    print(superincreasing_sequence[i], end=" ")
            print()
        else:
            print("Không tìm thấy subset có tổng bằng", target_sum)
    except ValueError:
        print("Vui lòng nhập giá trị số hợp lệ.")

if __name__ == "__main__":
    main()


# s : 53
# Nhập dãy số nguyên superincreasing, cách nhau bởi dấu cách: 17 38 73 4 11 1
# 4 11 38
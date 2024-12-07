def read_reports_from_file(filepath: str) -> list[list[int]]:

    reports = []
    with open(filepath, "r") as file:
        for line in file:
            array = line.strip().split()
            int_array = [int(num) for num in array]
            reports.append(int_array)
    return reports


reports = read_reports_from_file("./2.txt")


# reports = [
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9],
# ]

set_range = {1, 2, 3}


def safe(array: list[int]) -> bool:

    inc = array[1] > array[0]
    for i in range(1, len(array)):
        diff = array[i] - array[i - 1]
        abs_diff = abs(array[i] - array[i - 1])
        if abs_diff not in set_range:
            return False

        if inc and diff <= 0:
            return False
        if not inc and diff >= 0:
            return False
    return True


def rmSafe(array: list[int]) -> bool:

    for i in range(len(array)):
        if safe(array[:i] + array[i + 1 :]):
            return True
    return False


def part1() -> int:

    res = 0
    for level in reports:
        if safe(level):
            res += 1

    return res


def part2() -> int:

    res = 0
    for level in reports:
        if safe(level) or rmSafe(level):
            res += 1

    return res


print(part1())
print(part2())

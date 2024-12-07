
def check_safe(report: list) -> bool:
    # report must be incresing or decreasing
    # adjacent levels differ by at least one and at most three

    # note: we check if we need inc or dec by the first two levels
    # foo will be 1 if we need to check for decreasing, it will be -1 otherwise
    foo = 1 if report[0] > report[1] else -1
    for i in range(len(report) - 1):
        level_diff = report[i] - report[i+1]
        if abs(level_diff) < 1 or abs(level_diff) > 3:
            return False
        if foo * level_diff < 0:
            return False
    return True


def parse_input(file_path: str) -> list():
    with open(file_path, 'r') as fd:
        raw_lines = fd.readlines()
        reports = []
        for line in raw_lines:
            reports.append(list(map(lambda x: int(x), line.split(' '))))
    return reports

if __name__ == '__main__':
    reports = parse_input('./input.txt')
    total = 0
    for report in reports:
        if check_safe(report):
            total += 1
        else:
            for i in range(len(report)):
                if check_safe(report[:i] + report[i+1:]):
                    total += 1
                    break
    print(total)
            


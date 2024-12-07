import re

def apply_reg(data: str):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    res = re.findall(pattern, data)
    T = 0
    for r in res:
        n1, n2 = list(map(lambda x: int(x), re.findall(r"\d{1,3}", r)))
        T += (n1 * n2)
    return T


def parse_input(file_path: str) -> list():
    with open(file_path, 'r') as fd:
        data = fd.read()
    return data.strip()

if __name__ == '__main__':
    data = parse_input('./input.txt')
    res = apply_reg(data)
    print(res)

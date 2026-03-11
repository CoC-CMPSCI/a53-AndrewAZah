import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_main_1():
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # begin=3, end=10: evens 4+6+8+10 = 28
    regex_test([r'28'], lines)


@pytest.mark.T2
def test_main_2():
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # begin=-5, end=-2: evens -4+(-2) = -6
    regex_test([r'-6'], lines)


@pytest.mark.T3
def test_main_3():
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # begin=1, end=1: no evens, sum = 0
    regex_test([r'\b0\b'], lines)


@pytest.mark.T4
def test_main_4():
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # begin=2, end=12: evens 2+4+6+8+10+12 = 42
    regex_test([r'42'], lines)

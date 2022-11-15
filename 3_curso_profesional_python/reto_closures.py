def make_division_by(n: int):
    def divison(x: int) -> int:
        return x/n

    return divison


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print('18/54 es: ')
    print(division_by_18(54))


if __name__ == '__main__':
    run()

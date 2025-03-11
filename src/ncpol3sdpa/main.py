class Variable: ...


class Problem: ...


class Constraints: ...


def main():
    x = Variable("x")
    y = Variable("y")

    p = Problem(2 * max(x * y))
    c1 = Constraints()
    c2 = Constraints()
    p.add_constraint(c1)
    p.add_constraint(c2)
    p.solve()


if __name__ == "__main__":
    main()

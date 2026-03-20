from ast import Tuple
from dataclasses import dataclass


# data Expr = Var | Node Expr Char Expr
class Expr:
    pass


@dataclass
class Var(Expr):
    def __str__(self) -> str:
        return "a"


@dataclass
class Node(Expr):
    left: Expr
    op: str
    right: Expr

    def __str__(self) -> str:
        return f"({self.left}{self.op}{self.right})"


def parseOp(expr: str) -> tuple[str, str] | None:
    if expr and expr[0] in "*/+-":
        return (expr[0], expr[1:])
    else:
        return None


def parseExpr(expr: str, lista=[]) -> tuple[Expr, str, list] | None:

    if expr == "":
        return None
    if expr[0] == "a":
        lista.insert(0, "E -> a")
        return (Var(), expr[1:], lista)
    if expr[0] == "(":
        result = parseExpr(expr[1:])
        match result:
            case None:
                return None
            case (e1, resto1, _):
                result2 = parseOp(resto1)
                match result2:
                    case None:
                        return None
                    case (op, resto2):
                        lista.insert(0, f"Op -> {op}")
                        result3 = parseExpr(resto2)
                        match result3:
                            case None:
                                return None
                            case (e2, resto3, _):
                                if resto3[0] == ")":
                                    lista.insert(0, "E -> (E Op E)")
                                    return (Node(e1, op, e2), resto3[1:], lista)
                                else:
                                    return None
    else:
        return None


def main():
    while True:
        expr = input("Digite a expressão a ser analisada: ")
        parsed = parseExpr(expr)
        if parsed is None:
            print("Expressão inválida!\n")
        else:
            expression, rest, transactions = parsed
            if rest.strip() != "":
                print("Expressão inválida!\n")
            else:
                print(f"Expressão a ser analisada: {expression}\n")
                for trans in transactions:
                    print(f"{trans}\n")


if __name__ == "__main__":
    main()

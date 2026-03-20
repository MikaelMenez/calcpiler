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


def parseExpr(expr: str) -> tuple[Expr, str] | None:
    if expr == "":
        return None
    if expr[0] == "a":
        return (Var(), expr[1:])
    if expr[0] == "(":
        result = parseExpr(expr[1:])
        match result:
            case None:
                return None
            case (e1, resto1):
                result2 = parseOp(resto1)
                match result2:
                    case None:
                        return None
                    case (op, resto2):
                        result3 = parseExpr(resto2)
                        match result3:
                            case None:
                                return None
                            case (e2, resto3):
                                if resto3[0] == ")":
                                    return (
                                        Node(e1, op, e2),
                                        resto3[1:],
                                    )
                                else:
                                    return None
    else:
        return None

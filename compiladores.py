#!/usr/bin/env python3
import sys


class TokenType:
    TK_ID = "ID"
    TK_NUM = "NUM"
    TK_PLUS = "+"
    TK_MINUS = "-"
    TK_MULT = "*"
    TK_LPAREN = "("
    TK_RPAREN = ")"
    TK_EOF = "EOF"
    TK_INVALID = "INVALID"


class Token:
    def __init__(self, ttype, lexeme):
        self.type = ttype
        self.lexeme = lexeme

    def __repr__(self):
        return f"Token(type={self.type}, lexeme='{self.lexeme}')"


def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        ch = expr[i]

        if ch.isspace():
            i += 1
            continue

        if ch == "+":
            tokens.append(Token(TokenType.TK_PLUS, ch))
            i += 1
        elif ch == "-":
            tokens.append(Token(TokenType.TK_MINUS, ch))
            i += 1
        elif ch == "*":
            tokens.append(Token(TokenType.TK_MULT, ch))
            i += 1
        elif ch == "(":
            tokens.append(Token(TokenType.TK_LPAREN, ch))
            i += 1
        elif ch == ")":
            tokens.append(Token(TokenType.TK_RPAREN, ch))
            i += 1

        elif ch.isdigit():
            start = i
            while i < len(expr) and expr[i].isdigit():
                i += 1
            lexeme = expr[start:i]
            tokens.append(Token(TokenType.TK_NUM, lexeme))

        elif ch.isalpha() or ch == "_":
            start = i
            while i < len(expr) and (expr[i].isalnum() or expr[i] == "_"):
                i += 1
            lexeme = expr[start:i]
            tokens.append(Token(TokenType.TK_ID, lexeme))
        else:
            tokens.append(Token(TokenType.TK_INVALID, ch))
            i += 1

    tokens.append(Token(TokenType.TK_EOF, "EOF"))
    return tokens


tokens = []
current = 0
error_count = 0


def get_next_token():
    global current
    if current < len(tokens):
        return tokens[current]
    return Token(TokenType.TK_EOF, "EOF")


def is_at_end():
    return get_next_token().type == TokenType.TK_EOF


def match(expected_type):
    global current
    t = get_next_token()
    if t.type == expected_type:
        current += 1
    else:
        msg = f"Esperado '{expected_type}'"
        panic(msg)


def error(msg):
    global error_count
    t = get_next_token()
    print(f"Erro sintático: {msg}. Token atual: '{t.lexeme}'", file=sys.stderr)
    error_count += 1


def panic(msg):
    error(msg)
    global current
    sync_tokens = {
        TokenType.TK_PLUS,
        TokenType.TK_MINUS,
        TokenType.TK_MULT,
        TokenType.TK_LPAREN,
        TokenType.TK_RPAREN,
        TokenType.TK_EOF,
    }
    while not is_at_end():
        if get_next_token().type in sync_tokens:
            break
        current += 1


def token_name(ttype):
    return ttype


def parse_exp():
    """exp -> termo { soma termo }"""
    parse_term()
    while True:
        t = get_next_token()
        if t.type == TokenType.TK_PLUS or t.type == TokenType.TK_MINUS:
            consume_current_token()
            parse_term()
        else:
            break


def parse_term():
    """termo -> fator { mult fator }"""
    parse_factor()
    while True:
        t = get_next_token()
        if t.type == TokenType.TK_MULT:
            consume_current_token()
            parse_factor()
        else:
            break


def parse_factor():
    """fator -> (exp) | número | ID"""
    t = get_next_token()
    if t.type == TokenType.TK_LPAREN:
        match(TokenType.TK_LPAREN)
        parse_exp()
        match(TokenType.TK_RPAREN)
    elif t.type == TokenType.TK_NUM:
        match(TokenType.TK_NUM)
    elif t.type == TokenType.TK_ID:
        match(TokenType.TK_ID)
    else:
        panic("Esperado ID ou NUM ou '('")


def consume_current_token():
    global current
    current += 1


def main():
    global tokens, current, error_count

    expr = "(string + 3"

    tokens = tokenize(expr)

    current = 0
    error_count = 0

    parse_exp()

    if not is_at_end():
        panic("Tokens não consumidos ao final da expressão")

    if error_count == 0:
        print("Expressão sintaticamente correta.")
    else:
        print(f"Ocorreram {error_count} erro(s) sintático(s).")


if __name__ == "__main__":
    main()

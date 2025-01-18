# **Recursive Descent Parser with Error Handling**

This repository contains a **Recursive Descent Parser** implementation with error handling using the **panic mode** strategy. The project processes arithmetic expressions defined by a context-free grammar (CFG) and ensures syntactic validation with robust error recovery mechanisms.

---

## **Repository Details**

### Repository Name:  
`recursive-parser-error-handling`

### Description:  
A Python implementation of a Recursive Descent Parser for arithmetic expressions with panic mode error handling, built for educational purposes.

---

## **Project Overview**

This project focuses on creating a **syntactic analyzer** for simple arithmetic expressions. The parser uses recursive descent parsing and implements **panic mode** error recovery to handle syntactic errors gracefully. 

The **Context-Free Grammar (CFG)** for arithmetic expressions is defined as:

- `exp -> term { '+' term | '-' term }`
- `term -> factor { '*' factor }`
- `factor -> '(' exp ')' | NUM | ID`

---

## **Features**

1. **Tokenization**:
   - Recognizes identifiers (`ID`), numbers (`NUM`), arithmetic operators (`+`, `-`, `*`), parentheses (`(` and `)`), and the end-of-file marker (`EOF`).
   - Handles invalid characters and identifies them as `INVALID`.

2. **Syntactic Analysis**:
   - Validates the structure of expressions based on the CFG rules.
   - Detects and reports syntax errors.

3. **Error Handling**:
   - Implements **panic mode** recovery:
     - Skips tokens until a synchronization point is found.
     - Prevents parser crashes and continues parsing.

4. **Error Reporting**:
   - Provides clear and detailed error messages for easier debugging.

---

## **Usage**

### Prerequisites
- Python 3.6 or higher installed.

### Running the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/Gabriel-Bastos-Rabelo/recursive-parser-error-handling.git
   cd recursive-parser-error-handling
   ```
2. Execute the script:
   ```bash
   python3 parser.py
   ```

3. Modify the input expression in the `main()` function:
   ```python
   expr = "(string + 3)"
   ```

4. Observe the tokenization and parsing results.

---

## **Example Input and Output**

### Input
Expression: `(string + 3)`

### Output
```plaintext
Syntax Error: Expected 'NUM'. Current token: 'string'
1 syntax error(s) encountered.
```

---

## **Code Structure**

- **`TokenType`**: Enumeration of token types (e.g., `ID`, `NUM`, `+`, etc.).
- **`Token`**: Class representing individual tokens (type and lexeme).
- **`tokenize(expr)`**: Lexical analysis function to tokenize an input string.
- **Parsing Functions**:
  - `parse_exp`: Parses an expression.
  - `parse_term`: Parses terms.
  - `parse_factor`: Parses factors.
- **Error Handling**:
  - `panic(msg)`: Skips invalid tokens until a synchronization point is found.
  - `error(msg)`: Reports syntax errors.

---

## **Future Improvements**

- Add support for:
  - Decimal numbers.
  - Division (`/`) and exponentiation (`^`) operators.
  - Custom error messages with token positions.
- Extend the CFG to handle more complex expressions.

---

## **Contributors**
Developed by Gabriel Bastos Rabelo, Gabriel Belo Pereira dos Reis, João Felipe Launé Assunção.

Feel free to submit issues, suggest improvements, or fork the repository for your own experiments!

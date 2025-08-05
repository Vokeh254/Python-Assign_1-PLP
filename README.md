# 🧮 Simple Python Calculator

This is a basic command-line calculator written in Python. It allows users to perform simple arithmetic operations—addition, subtraction, multiplication, and division—between two numbers.

---

## 📋 Features

- Accepts two integer inputs from the user
- Supports four basic operators: `+`, `-`, `*`, `/`
- Handles division by zero gracefully
- Displays the full expression and result
- Provides error messages for invalid operators

---

## 🚀 How to Run

1. Make sure you have Python installed (version 3.x recommended).
2. Save the script in a file, e.g., `calculator.py`.
3. Open a terminal or command prompt.
4. Run the script using:

```bash
python calculator.py
```

---

## 🧑‍💻 Example Usage

```text
Enter the first number: 10
Enter the second number: 5
Enter the operator: *
your result is 10 * 5 = 50
```

---

## ⚠️ Error Handling

- If the user enters `/` and the second number is `0`, the program returns:
  ```
  Error: Division by zero
  ```
- If the user enters an unsupported operator (e.g., `%` or `^`), the program returns:
  ```
  Error: Invalid operator
  ```

---

## 📌 Notes

- All inputs are expected to be integers.
- You can extend the script to support more operators or floating-point numbers.

---

## 📄 License

This project is open-source and free to use for educational or personal purposes.

```

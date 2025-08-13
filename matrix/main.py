def input_matrix():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            value = int(input(f"Enter the value for index {i}{j}: "))
            row.append(value)
        matrix.append(row)

    return matrix


def addition():
    matrix1 = input_matrix()
    matrix2 = input_matrix()

    if not is_row_same(matrix1, matrix2) or not is_column_same(matrix1, matrix2):
        print("Matrices dimensions do not match! Try again.")
        return

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    print("Matrix 1:", matrix1)
    print("Matrix 2:", matrix2)
    print("Resulted Matrix:", result)


def subtraction():
    matrix1 = input_matrix()
    matrix2 = input_matrix()

    if not is_row_same(matrix1, matrix2) or not is_column_same(matrix1, matrix2):
        print("Matrices dimensions do not match! Try again.")
        return

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)

    print("Matrix 1:", matrix1)
    print("Matrix 2:", matrix2)
    print("Resulted Matrix:", result)


def multiplication():
    matrix1 = input_matrix()
    matrix2 = input_matrix()

    if not is_row_same(matrix1, matrix2) or not is_column_same(matrix1, matrix2):
        print("Matrices dimensions do not match! Try again.")
        return

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] * matrix2[i][j])
        result.append(row)

    print("Matrix 1:", matrix1)
    print("Matrix 2:", matrix2)
    print("Resulted Matrix:", result)


def diagonal():
    matrix = input_matrix()

    if not is_square_matrix(matrix):
        print("The matrix is not a square matrix!")
        return

    diagonal_elements = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] != 0:
                print("Matrix is not diagonal as non-diagonal elements are not zero.")
                return
            if i == j:
                diagonal_elements.append(matrix[i][j])

    print("Matrix:", matrix)
    print("Diagonal Elements are:", diagonal_elements)


def trace():
    matrix = input_matrix()

    if not is_square_matrix(matrix):
        print("The matrix is not a square matrix! Please try again.")
        return

    trace_sum = sum(matrix[i][i] for i in range(len(matrix)))

    print("Matrix:", matrix)
    print("Trace of the Matrix:", trace_sum)


# Helper functions (converted from your first code)
def is_row_same(matrix1, matrix2):
    return len(matrix1) == len(matrix2)


def is_column_same(matrix1, matrix2):
    if not matrix1 or not matrix2:
        return False
    for i in range(max(len(matrix1), len(matrix2))):
        if len(matrix1[i]) != len(matrix2[i]):
            return False
    return True


def is_square_matrix(matrix):
    for row in matrix:
        if len(matrix) != len(row):
            return False
    return True

def main():
    while True:
        print("----------------------------------")
        print("------ Welcome To Matrix CLI ------")
        print("-----------------------------------")

        options = [
            "Exit",
            "Addition",
            "Subtraction",
            "Multiplication",
            "Diagonal Check",
            "Trace",
        ]
        for index, option in enumerate(options):
            print(f"{index}. {option}")

        try:
            user_input = int(input("Enter your option: "))
        except ValueError:
            print("Invalid input. Please enter a number.❌")
            continue

        if user_input == 0:
            print("Thank you for using Matrix CLI.😊✨")
            break
        elif user_input == 1:
            addition()
        elif user_input == 2:
            subtraction()
        elif user_input == 3:
            multiplication()
        elif user_input == 4:
            diagonal()
        elif user_input == 5:
            trace()
        else:
            print("Invalid option. Please try again.❌")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()

# Function to take matrix input from the user
def input_matrix():
    # Get number of rows and columns
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    matrix = []
    # Loop through each row
    for i in range(rows):
        row = []
        # Loop through each column to take element input
        for j in range(columns):
            value = int(input(f"Enter the value for index {i}{j}: "))
            row.append(value)
        matrix.append(row)  # Add the row to the matrix

    return matrix  # Return the completed matrix


# Function to perform matrix addition
def addition():
    matrix1 = input_matrix()  # First matrix
    matrix2 = input_matrix()  # Second matrix

    # Check if matrices have the same dimensions
    if not is_row_same(matrix1, matrix2) or not is_column_same(matrix1, matrix2):
        print("Matrices dimensions do not match! Try again.")
        return

    result = []
    # Element-wise addition
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    # Display results
    print("Matrix 1:", matrix1)
    print("Matrix 2:", matrix2)
    print("Resulted Matrix:", result)


# Function to perform matrix subtraction
def subtraction():
    matrix1 = input_matrix()
    matrix2 = input_matrix()

    # Check if matrices have the same dimensions
    if not is_row_same(matrix1, matrix2) or not is_column_same(matrix1, matrix2):
        print("Matrices dimensions do not match! Try again.")
        return

    result = []
    # Element-wise subtraction
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)

    # Display results
    print("Matrix 1:", matrix1)
    print("Matrix 2:", matrix2)
    print("Resulted Matrix:", result)


# Function to perform element-wise multiplication
def multiplication():
    matrix1 = input_matrix()
    matrix2 = input_matrix()

    # Check if matrices have the same dimensions
    if not is_row_same(matrix1, matrix2) or not is_column_same(matrix1, matrix2):
        print("Matrices dimensions do not match! Try again.")
        return

    result = []
    # Element-wise multiplication
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] * matrix2[i][j])
        result.append(row)

    # Display results
    print("Matrix 1:", matrix1)
    print("Matrix 2:", matrix2)
    print("Resulted Matrix:", result)


# Function to check if a matrix is diagonal
def diagonal():
    matrix = input_matrix()

    # Check if matrix is square
    if not is_square_matrix(matrix):
        print("The matrix is not a square matrix!")
        return

    diagonal_elements = []
    # Loop through matrix to check if non-diagonal elements are zero
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] != 0:
                print("Matrix is not diagonal as non-diagonal elements are not zero.")
                return
            if i == j:
                diagonal_elements.append(matrix[i][j])  # Collect diagonal elements

    # Display results
    print("Matrix:", matrix)
    print("Diagonal Elements are:", diagonal_elements)


# Function to calculate the trace (sum of diagonal elements) of a matrix
def trace():
    matrix = input_matrix()

    # Check if matrix is square
    if not is_square_matrix(matrix):
        print("The matrix is not a square matrix! Please try again.")
        return

    # Calculate trace by summing diagonal elements
    trace_sum = sum(matrix[i][i] for i in range(len(matrix)))

    # Display results
    print("Matrix:", matrix)
    print("Trace of the Matrix:", trace_sum)


# Function to check if matrices have the same number of rows
def is_row_same(matrix1, matrix2):
    return len(matrix1) == len(matrix2)


# Function to check if matrices have the same number of columns
def is_column_same(matrix1, matrix2):
    if not matrix1 or not matrix2:
        return False
    for i in range(max(len(matrix1), len(matrix2))):
        if len(matrix1[i]) != len(matrix2[i]):
            return False
    return True


# Function to check if matrix is square (rows == columns)
def is_square_matrix(matrix):
    for row in matrix:
        if len(matrix) != len(row):
            return False
    return True


# Main function to display menu and handle user choices
def main():
    while True:
        # Menu header
        print("----------------------------------")
        print("------ Welcome To Matrix CLI ------")
        print("-----------------------------------")

        # Menu options
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

        # Handle user input for menu selection
        try:
            user_input = int(input("Enter your option: "))
        except ValueError:
            print("Invalid input. Please enter a number.❌")
            continue

        # Execute corresponding function based on user choice
        match user_input:
            case 0:
                print("Thank you for using Matrix CLI.😊✨")
                break
            case 1:
                addition()
            case 2:
                subtraction()
            case 3:
                multiplication()
            case 4:
                diagonal()
            case 5:
                trace()
            case _:
                print("Invalid option. Please try again.❌")

        # Wait for user before showing menu again
        input("\nPress Enter to continue...")


# Run the program
main()

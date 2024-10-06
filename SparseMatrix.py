import os


class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.elements = {}  # Use dictionary to store non-zero elements {(row, col): value}

    def add_element(self, row, col, value):
        if value != 0:
            self.elements[(row, col)] = value  # Add or update non-zero element
        elif (row, col) in self.elements:
            del self.elements[(row, col)]  # Remove element if set to zero

    @staticmethod
    def load_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

                # Validate rows
                if not lines[0].strip().startswith("rows="):
                    raise ValueError("Input file format error: Missing or incorrect 'rows=' declaration")
                numRows = int(lines[0].strip().split('=')[1])

                # Validate columns
                if not lines[1].strip().startswith("cols="):
                    raise ValueError("Input file format error: Missing or incorrect 'cols=' declaration")
                numCols = int(lines[1].strip().split('=')[1])

                matrix = SparseMatrix(numRows, numCols)

                # Process matrix elements
                for line in lines[2:]:
                    line = line.strip()
                    if not line:
                        continue  # Skip empty lines

                    if not (line.startswith('(') and line.endswith(')')):
                        raise ValueError("Input file format error: Matrix element not properly enclosed in parentheses")

                    parts = line[1:-1].split(',')
                    if len(parts) != 3:
                        raise ValueError("Input file format error: Matrix element should have three parts (row, col, value)")

                    try:
                        row, col, value = map(int, map(str.strip, parts))
                    except ValueError:
                        raise ValueError("Input file format error: Matrix element must contain integers")

                    if row >= numRows or col >= numCols:
                        raise ValueError(f"Matrix element error: Element ({row}, {col}) is out of bounds")

                    matrix.set_element(row, col, value)

                return matrix

        except IOError:
            raise IOError(f"Error: Could not read file {file_path}")
        except ValueError as e:
            raise ValueError(f"File parsing error: {e}")

    def get_element(self, row, col):
        return self.elements.get((row, col), 0)  # Return value or 0 if not found

    def set_element(self, row, col, value):
        self.add_element(row, col, value)

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for addition")

        result = SparseMatrix(self.rows, self.cols)

        # Copy all elements from the first matrix
        result.elements = self.elements.copy()

        # Add elements from the second matrix
        for (row, col), value in other.elements.items():
            result.set_element(row, col, result.get_element(row, col) + value)

        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for subtraction")

        result = SparseMatrix(self.rows, self.cols)

        # Copy all elements from the first matrix
        result.elements = self.elements.copy()

        # Subtract elements from the second matrix
        for (row, col), value in other.elements.items():
            result.set_element(row, col, result.get_element(row, col) - value)

        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication")

        result = SparseMatrix(self.rows, other.cols)

        # Iterate only through non-zero elements of the first matrix
        for (row, col), value in self.elements.items():
            # Check if the second matrix has non-zero elements in the corresponding column
            for k in range(other.cols):
                other_value = other.get_element(col, k)
                if other_value != 0:
                    # Update result matrix with product of non-zero elements
                    result.set_element(row, k, result.get_element(row, k) + value * other_value)

        return result

    def save_to_file(self, file_path):
        try:
            with open(file_path, 'w') as writer:
                # Write number of rows and columns
                writer.write(f"rows={self.rows}\n")
                writer.write(f"cols={self.cols}\n")

                # Write each non-zero element
                for (row, col), value in self.elements.items():
                    writer.write(f"({row}, {col}, {value})\n")

        except IOError:
            raise IOError(f"Error: Could not write to file {file_path}")


def main():
    try:
        # Load matrices from files
        matrix1 = SparseMatrix.load_from_file("/home/jade/DSA-Sparse-Matrix/sample_inputs/easy_sample_02_1.txt")
        matrix2 = SparseMatrix.load_from_file("/home/jade/DSA-Sparse-Matrix/sample_inputs/easy_sample_02_2.txt")

        # Get user input for operation
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")

        operation = int(input("Enter your choice (1/2/3): "))

        result = None
        if operation == 1:
            result = matrix1.add(matrix2)
            print("\nAddition Done:")
        elif operation == 2:
            result = matrix1.subtract(matrix2)
            print("\nSubtraction Done:")
        elif operation == 3:
            result = matrix1.multiply(matrix2)
            print("\nMultiplication Done:")
        else:
            print("Invalid operation choice.")
            return

        # Create output directory if it doesn't exist
        output_dir = "./output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Create output.txt file in the output directory
        output_file_path = os.path.join(output_dir, "output.txt")
        result.save_to_file(output_file_path)

        print(f"Result written to {output_file_path}")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

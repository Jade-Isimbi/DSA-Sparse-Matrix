# Sparse Matrix Operations

## Overview
This project implements operations for sparse matrices in Python,the operations supported are **addition**, **subtraction**, and **multiplication**. Sparse matrices are read from input files, and the results are written to output files.

## Directory Structure

```
/DSA-Sparse-Matrix/
│
├── SparseMatrix.py    # Main Python script
├──output/  # Directory for output files
│
└── sample_inputs/    # Directory for input files
```

## Cloning the Repository

To clone the repository, run the following command:

```bash
git clone  https://github.com/Jade-Isimbi/DSA-Sparse-Matrix.git

```


### Input File Format
The input file should define the number of rows and columns followed by the non-zero entries in the matrix. The format should be:

- `row`: The row index where the non-zero value is located.
- `col`: The column index where the non-zero value is located.
- `value`: The actual non-zero value at the given row and column.

**Example Entry:**

```
rows=8433
cols=3180
(0, 381, -694)
(0, 128, -838)
(0, 639, 857)
(0, 165, -933)
(0, 1350, -89)
```
## Usage

### Command-Line Arguments

The script expects two input filenames as command-line arguments.

### Running the Script

Navigate to the `DSA-Sparse-Matrix` directory and run the script with the input filenames:
```bash
cd DSA-Sparse-Matrix
```

```bash
python3 SparseMatrix.py 
```

You will be prompted to select an operation

```bash
Choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
Enter your choice (1/2/3): 
```
After choosing the operation, the script will process the input matrices and perform the chosen operation. The result will be saved in the output directory.

```bash
 Addition Done:
Result written to ./output/output.txt
```
## Error Handling

- The script will raise an error if the input files have incorrect formats.
- The script will check if the files exist in the specified input directory.
- The script will raise an error if the matrix dimensions do not match the requirements for the selected operation.

## Author

This project was developed by Jade ISIMBI TUZINDE . Github: https://github.com/Jade-Isimbi

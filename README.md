## Compilation and Execution

### 1. Compilation

Open a terminal or command prompt and navigate to the directory where your C++ source file (e.g., `my_program.cpp`) is located.

#### Using GCC/G++ (Linux/macOS/Windows with MinGW or Cygwin)

```
g++ my_program.cpp -o my_program
```

This command compiles `my_program.cpp` and creates an executable named `my_program` (or `my_program.exe` on Windows).

#### Using MSVC (Windows, Developer Command Prompt)

```
cl /EHsc my_program.cpp
```

This compiles `my_program.cpp` and creates `my_program.exe`.

### 2. Execution

After successful compilation, run the generated executable from the same terminal or command prompt.

#### On Linux/macOS

```
./my_program
```

#### On Windows

```
my_program.exe
```

or simply

```
my_program
```

# LeetCode Problem Solving

This is my personal repository containing solutions to various LeetCode problems, organized by topic and difficulty.

## Structure

- `LeetCode/Greedy/Easy/` — Solutions to easy greedy problems.
- `LeetCode/Greedy/Easy/output/` — Compiled executables for easy greedy problems.

## Language Support

- All solutions are implemented in **C++**.

## How to Use

- Browse the folders to find solutions by problem number and name.
- C++ source files are located in their respective problem folders.
- Compiled executables are stored in the `output` folder inside each topic/difficulty directory.

## Folder Example

```
LeetCode/
  Greedy/
    Easy/
      409. Longest Palindrome.cpp
      455. Assign Cookies.cpp
      561. Array Partition.cpp
      output/
        409. Longest Palindrome.exe
        455. Assign Cookies.exe
        561. Array Partition.exe
```

## Compiling and Running

### Using MinGW (g++)

Open PowerShell in the folder containing your `.cpp` file and run:

```
g++ -Wall -Wextra -g3 "<source_file.cpp>" -o "output/<executable_name.exe>"
```

**Example:**

```
g++ -Wall -Wextra -g3 "561. Array Partition.cpp" -o "output/561. Array Partition.exe"
```

### Running the Executable (PowerShell)

Navigate to the `output` folder and run:

```
& .\<executable_name.exe>
```

**Example:**

```
& .\561. Array Partition.exe
```

### Using CodeBlocks or Other IDEs

You can also use CodeBlocks or any C++ IDE to compile and run the files. Set the output directory to `output` for consistency.

## Note

This repository is for my personal use and reference. Feel free to browse and use the solutions for learning purposes.

## License

This project is for educational purposes.

# BrainFuck Interpreter
A very simple BrainFuck interpreter written in Python.

### Specifications
- Fixed memory size (30000)
- Exceeding bounds sends you to the other side for both cell value and pointer (if cell is 0 and next operation is - cell value shifts to 255)
- Input is taken during the execution

### Usage
```console
python bf.py <path to your brainfuck code>
```
No error handling is done when reading file.

Please let me know if you notice any misbehaviour.
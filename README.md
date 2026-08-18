# Python OOP, Generators, Iterators and Multithreading
## University Student Code Laboratory

This package is designed for undergraduate university students learning Python object-oriented programming and concurrency.

### Topics
1. Creating Classes and Objects
2. Encapsulation
3. Abstraction
4. Polymorphism
5. Inheritance
6. Static and Instance Methods
7. Constructors
8. Access Modifiers
9. Getters, Setters and Deleters
10. Generator Functions and Iterators
11. Method Overloading
12. Method Overriding
13. Operator Overloading
14. Interfaces in Python
15. Abstract Methods and Abstract Classes
16. Working with Threads
17. Introduction to Multithreading

### Folder Pattern
Every topic folder contains:
- `01_basic.py` – first concept demonstration
- `02_real_world.py` – practical/real-world example
- `03_advanced.py` – stronger university-level example
- `04_leetcode_style.py` – LeetCode-inspired design/algorithm example
- `PRACTICE.md` – exercises for laboratory/tutorial work
- `README.md` – concept notes and execution instructions

### Important Python Notes
- Python does **not** have Java-style private/protected enforcement. `_name` and `__name` are conventions/name-mangling mechanisms.
- Python does **not** support method overloading by parameter signature. Similar behavior is obtained using default values, `*args`, `**kwargs`, `functools.singledispatchmethod`, or explicit type checks.
- Python has no `interface` keyword. Interfaces are commonly modeled using `abc.ABC`, `typing.Protocol`, or duck typing.
- CPU-bound Python threads are constrained by the CPython Global Interpreter Lock (GIL). Threads are nevertheless highly useful for I/O-bound work.

### Running Examples
From a terminal:

```bash
python 01_Creating_Classes_and_Objects/01_basic.py
```

Or run the smoke-test utility:

```bash
python run_all_examples.py
```

No third-party libraries are required.

### LeetCode References
The LeetCode-style files contain original educational implementations inspired by well-known LeetCode design/concurrency problems. They intentionally avoid reproducing full problem statements.

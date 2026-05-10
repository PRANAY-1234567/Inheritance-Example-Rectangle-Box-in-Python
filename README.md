# 📦 Inheritance Example – Rectangle & Box in Python

## 📌 Description

This Python program demonstrates **inheritance** using a `Rectangle` class and a derived `Box` class.
The `Box` class inherits dimensions and methods from `Rectangle` and adds extra functionality like:

* Volume calculation
* Surface area calculation

---

## 🚀 Features

* Demonstrates **single inheritance**
* Uses `super()` constructor
* Calculates:

  * Area of rectangle
  * Perimeter of rectangle
  * Volume of box
  * Surface area of box
  
---

## 🛠️ How It Works

### 1️⃣ Parent Class – `Rectangle`

Contains:

* `length`
* `breadth`

Methods:

* `input_dimensions()`
* `area()`
* `perimeter()`

---

### 2️⃣ Child Class – `Box`

```python id="m7x3lp"
class Box(Rectangle)
```

👉 Inherits all members of `Rectangle`

Adds:

* `height`

Methods:

* `input_height()`
* `volume()`
* `surface_area()`

Uses:

```python id="r9k4zx"
super().__init__()
```

to initialize parent class constructor.

---

## 💻 Code

```python id="v3q8pl"
class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0

    def input_dimensions(self):
        self.length = float(input("Enter the length : "))
        self.breadth = float(input("Enter the breadth : "))

    def area(self):
        a = self.length * self.breadth
        print("Area of rectangle :", a)

    def perimeter(self):
        p = 2 * (self.length + self.breadth)
        print("Perimeter of rectangle :", p)


class Box(Rectangle):   # Inheriting Rectangle class
    def __init__(self):
        super().__init__()
        self.height = 0

    def input_height(self):
        self.height = float(input("Enter the height : "))

    def volume(self):
        v = self.length * self.breadth * self.height
        print("Volume :", v)

    def surface_area(self):
        sa = 2 * self.length * self.height + \
             2 * self.length * self.breadth + \
             2 * self.breadth * self.height

        print("Surface Area :", sa)


class Inh2:
    @staticmethod
    def main():
        box = Box()

        box.input_dimensions()
        box.input_height()

        print("\n\nBase of Box")
        print("--------------------")
        box.area()
        box.perimeter()

        print("\n\nBody of Box")
        print("--------------------")
        box.volume()
        box.surface_area()


# Calling main method
Inh2.main()
```

---

## ▶️ Example Output

```id="s6m2qv"
Enter the length : 10
Enter the breadth : 5
Enter the height : 8


Base of Box
--------------------
Area of rectangle : 50.0
Perimeter of rectangle : 30.0


Body of Box
--------------------
Volume : 400.0
Surface Area : 260.0
```

---

## 🧠 Key Concepts

### ✔ Inheritance

`Box` inherits:

* variables
* methods
  from `Rectangle`

---

### ✔ `super()` Keyword

```python id="y1x8pk"
super().__init__()
```

👉 Calls constructor of parent class

---

### ✔ Reusability

No need to rewrite:

* area()
* perimeter()

---

## 📚 Concepts Used

* Class & Object
* Single Inheritance
* Constructor Inheritance
* `super()` method
* User input
* Mathematical formulas

---

## 📐 Formulas Used

### Rectangle

```python id="h3p7lt"
Area = length × breadth
Perimeter = 2 × (length + breadth)
```

### Box

```python id="v8k2qn"
Volume = length × breadth × height
Surface Area = 2(lb + bh + lh)
```

---

## 🎯 Use Case

This program helps beginners understand:

* Real-world inheritance relationships
* Reusing existing class functionality
* Extending parent class features

---

## 🔧 Future Improvements

* Add cube class
* Add validation for negative dimensions
* Use constructor parameters instead of input
* Add 3D shape hierarchy

---

## 📄 License

This project is open-source and free to use.

<img width="698" height="907" alt="image" src="https://github.com/user-attachments/assets/3cd209ca-d500-4d04-9292-d4262f787fa0" />

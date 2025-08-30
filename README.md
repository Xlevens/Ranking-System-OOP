# 🎓 Student Results Ranking System
A Python-based system to manage, rank, and display student results. 

This project was collaboratively developed by **Syeda Kaneez Fatima, Behroz, Asad, Rizwan,  Zain, and Fatima Shahzad** as part of a team effort.  

<p align="center">
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGE2MGIxZHM2cWloZ3Jka2F2N3h2czF4YzZ5NWlvZWMyeGoxNXFtaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3orif1xSQnwOkYIRjO/giphy.gif" width="400" />
</p>

---

## ✨ Features
- 📊 **Result Management** – Import results from CSV files.  
- 🏆 **Dense Ranking System** – Assigns ranks without skipping (e.g., 1,2,2,3,4,4).  
- 🔎 **Search Functionality** – Quickly find students by enrollment number or name.  
- 📋 **Tabulated Display** – Clean and readable output using the `tabulate` library.  
- 🎨 **Console Introduction** – Centered title and credits, presenting a polished experience.  

---

## 🛠️ Technology Stack
- **Python 3.x**
- [`tabulate`](https://pypi.org/project/tabulate/) – For beautiful console tables
- Standard Python libraries (`csv`, `os`, etc.)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Xlevens/Ranking-System_OOP.git

cd Ranking-System_OOP
```

### 2. Install Dependencies
```bash
pip install tabulate
```

### 3. Run the Program
```bash
python main.py
```
---

## 📂 Project Structure
```

├── main.py                  # Entry point (runs the program)

├── data
    └── results.csv          # Input dataset

├── file_handling/            
    └── __init__.py
    └── File.py              # Looks for the files

├── interface/
    └── App_controller.py    # Checks, Searches, Sorts and Displays the results in tabular form

├── models/            
    └── __init__.py
    └── Students.py          # Stores initial attributes for students info and questions
    └── Students_List.py     # Stores Students info in a list
    └── Teacher.py           # Stores Teacher's Credential i.e name & course code

├── .gitignore               # Necessary to keep compiled files/logs out

└── README.md                # Project documentation

```

---

## 👥 Contributors
- **[Fatima Shahzad](https://github.com/Fatimadev15)**
- **[Behroz](https://github.com/Behroz-9t)**
- **[Rizwan](https://github.com/Xlevens)**  
- **[Syeda Kaneez Fatima](https://github.com/skfatima-codes)**  
- **[Zain](https://github.com/ZainCodes07)**
- **[Asad](https://github.com/Asad101001)**
  
---


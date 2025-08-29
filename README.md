# 🎓 Student Results Ranking System

A Python-based system to manage, rank, and display student results.  
This project was collaboratively developed by **Asad, Rizwan, Syeda Kaneez Fatima, Behroz, Zain, and Fatima Shahzad** as part of a team effort.  

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
.
├── main.py              # Entry point (runs the program)
├── File.py              # Looks for the files
├── App_controller.py    # Checks, Searches, Sorts and Displays the results in tabular form
├── Students.py          # Stores The initial attributes for students info and questions
├── Students_List.py          # Stores Students info in a list
├── Teacher.py           # Stores Teacher's Credential i.e name & course code
├── results.csv          # Input dataset
└── README.md            # Project documentation
```

---

## 👥 Contributors
- **Asad**  
- **Rizwan**  
- **Syeda Kaneez Fatima**  
- **Behroz** 
- **Zain**  
- **Fatima Shahzad**

---

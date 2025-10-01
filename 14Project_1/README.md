# Employee Manager Application Project

In this project, you will build a multi-page employee management application using Tkinter. You will organize your code into multiple files, separate the GUI from the data handling, and allow users to add, view, edit, and delete employee records. All employee data will be saved in a `.txt` file.

---

## Project Requirements

- **Multi-page GUI:** Use Tkinter frames to create separate pages (screens) for different actions.
- **File organization:** Separate your code into multiple files (for example: `main.py`, `employee.py`, `data_handler.py`, and files for each GUI page).
- **Data persistence:** Employee data is saved to and loaded from a `.txt` file.
- **Features:**
  - Welcome/start page with a button to begin.
  - Employee list page showing all employees (name, occupation, salary).
  - "Add Employee" page with fields for name, occupation (dropdown), and salary.
  - "Edit Employee" page to update existing employee info.
  - "Delete Employee" confirmation popup.
  - Buttons to switch between pages and perform actions.
  - The employee list reloads from the file after any change.

---

## Suggested File Structure

```
EmployeeApp/
│
├── main.py
├── employee.py           # Employee class for editing and entering employee data
├── data_handler.py       # Functions for loading/saving/editing/deleting employees
├── gui/
│   ├── __init__.py
│   ├── start_page.py
│   ├── employee_list_page.py
│   ├── add_employee_page.py
│   └── edit_employee_page.py
└── employees.txt         # Data file
```

---

## The Employee Class

Your `Employee` class should be responsible for handling employee data.  
It should include methods for creating, updating, and representing employee information.

**Example:**

```python
# employee.py
class Employee:
    def __init__(self, name, occupation, salary):
        self.name = name
        self.occupation = occupation
        self.salary = salary

    def update(self, name=None, occupation=None, salary=None):
        if name is not None:
            self.name = name
        if occupation is not None:
            self.occupation = occupation
        if salary is not None:
            self.salary = salary

    def to_line(self):
        return f"{self.name},{self.occupation},{self.salary}\n"

    @staticmethod
    def from_line(line):
        name, occupation, salary = line.strip().split(",")
        return Employee(name, occupation, salary)
```

---

## Key Concepts and Tips

- **Frames as Pages:** Use a separate `tk.Frame` for each page. Raise the frame you want to show.
- **Switching Pages:** Write a function in your main app class to switch between frames.
- **Data Handling:** Keep all file reading/writing in `data_handler.py`. Import and use these functions in your GUI files.
- **Updating the List:** Always reload the employee list from the file after adding, editing, or deleting.
- **Confirmation Popups:** Use `tk.Toplevel` or `tk.messagebox` for delete confirmations.
- **Dropdowns:** Use `tk.OptionMenu` or `ttk.Combobox` for occupation selection.

---

## Example: Adding an Employee

```python
# In add_employee_page.py
import tkinter as tk
from data_handler import add_employee

class AddEmployeePage(tk.Frame):
    def __init__(self, master, switch_to_list):
        super().__init__(master)
        # ... create entry fields for name, occupation, salary ...
        # ... create Save button ...
        save_btn = tk.Button(self, text="Save", command=self.save_employee)
        save_btn.pack()

    def save_employee(self):
        # ... get data from entry fields ...
        add_employee(name, occupation, salary)
        self.master.switch_to_list()
```

---

## Homework

**Build the Employee Manager Application:**

1. Set up your project folders and files as shown above.
2. Create the start page with a welcome message and a "Start" button.
3. Build the employee list page that displays all employees and has "Add", "Edit", and "Delete" buttons.
4. Implement the add and edit pages with entry fields and dropdowns.
5. Make sure all data is saved to and loaded from `employees.txt`.
6. Use popups to confirm deletions.
7. Test your app by adding, editing, and deleting employees.

*Bonus: Add search or sorting features, or allow saving more employee details!*

---

**Remember:**  
- Organize your code into multiple files for clarity.
- The `Employee` class should handle all employee data logic.
- Separate GUI and data logic.
- Always reload data after changes to keep the display up to date.
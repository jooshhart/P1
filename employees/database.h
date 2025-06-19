#pragma once
#include <vector>
#include "employee.h"
#include "manager.h"

class EmployeeDatabase {
    std::vector<Employee*> employees;
    int nextId = 1;
public:
    ~EmployeeDatabase();
    void addEmployee();
    void listEmployees() const;
    void editEmployee();
    void removeEmployee();
    Employee* findEmployee(int id);
};
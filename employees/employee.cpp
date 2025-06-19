#include "employee.h"

Employee::Employee(int id, const std::string& name, double salary)
    : id(id), name(name), salary(salary) {}

void Employee::display() const {
    std::cout << "ID: " << id << " | Name: " << name << " | Salary: $" << salary << "\n";
}

int Employee::getId() const { return id; }
void Employee::setName(const std::string& n) { name = n; }
void Employee::setSalary(double s) { salary = s; }
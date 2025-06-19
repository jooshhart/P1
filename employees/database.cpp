#define NOMINMAX
#include "database.h"
#include <ios>
#include <iostream>
#include <limits>
#include <string>
#include <thread>
#include <chrono>
#include "utils.h"

#ifdef max
#undef max
#endif

EmployeeDatabase::~EmployeeDatabase() {
    for (auto emp : employees) delete emp;
}

void EmployeeDatabase::addEmployee() {
    clear_screen();
    std::cout << "Add Employee\n1. Regular Employee\n2. Manager\nChoice: ";
    int type;
    std::cin >> type;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::string name;
    double salary;
    std::cout << "Enter name: ";
    std::getline(std::cin, name);
    std::cout << "Enter salary: ";
    std::cin >> salary;

    if (type == 2) {
        int teamSize;
        std::cout << "Enter team size: ";
        std::cin >> teamSize;
        employees.push_back(new Manager(nextId++, name, salary, teamSize));
    } else {
        employees.push_back(new Employee(nextId++, name, salary));
    }
    std::cout << "Employee added!\n";
    pause(1000);
}

void EmployeeDatabase::listEmployees() const {
    clear_screen();
    std::cout << "Employee List:\n";
    for (const auto& emp : employees) {
        emp->display();
    }
    pause(2000);
}

void EmployeeDatabase::editEmployee() {
    clear_screen();
    std::cout << "Enter Employee ID to edit: ";
    int id;
    std::cin >> id;
    Employee* emp = findEmployee(id);
    if (!emp) {
        std::cout << "Employee not found.\n";
        pause(1000);
        return;
    }
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::string name;
    double salary;
    std::cout << "Enter new name (leave blank to keep current): ";
    std::getline(std::cin, name);
    if (!name.empty()) emp->setName(name);
    std::cout << "Enter new salary (or -1 to keep current): ";
    std::cin >> salary;
    if (salary >= 0) emp->setSalary(salary);

    Manager* mgr = dynamic_cast<Manager*>(emp);
    if (mgr) {
        int teamSize;
        std::cout << "Enter new team size (or -1 to keep current): ";
        std::cin >> teamSize;
        if (teamSize >= 0) mgr->setTeamSize(teamSize);
    }
    std::cout << "Employee updated!\n";
    pause(1000);
}

void EmployeeDatabase::removeEmployee() {
    clear_screen();
    std::cout << "Enter Employee ID to remove: ";
    int id;
    std::cin >> id;
    for (auto it = employees.begin(); it != employees.end(); ++it) {
        if ((*it)->getId() == id) {
            delete *it;
            employees.erase(it);
            std::cout << "Employee removed.\n";
            pause(1000);
            return;
        }
    }
    std::cout << "Employee not found.\n";
    pause(1000);
}

Employee* EmployeeDatabase::findEmployee(int id) {
    for (auto emp : employees) {
        if (emp->getId() == id) return emp;
    }
    return nullptr;
}
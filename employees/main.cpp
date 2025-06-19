#include <iostream>
#include <thread>
#include <chrono>
#include "database.h"
#include "utils.h"

void show_animation(const std::string& msg) {
    for (char c : msg) {
        std::cout << c << std::flush;
        pause(30);
    }
    std::cout << "\n";
}

int main() {
    EmployeeDatabase db;
    int choice;
    while (true) {
        clear_screen();
        show_animation("=== Employee Management Menu ===");
        std::cout << "1. Add Employee\n";
        std::cout << "2. List Employees\n";
        std::cout << "3. Edit Employee\n";
        std::cout << "4. Remove Employee\n";
        std::cout << "5. Exit\n";
        std::cout << "Choose an option: ";
        std::cin >> choice;
        switch (choice) {
            case 1: db.addEmployee(); break;
            case 2: db.listEmployees(); break;
            case 3: db.editEmployee(); break;
            case 4: db.removeEmployee(); break;
            case 5: clear_screen(); show_animation("Goodbye!"); return 0;
            default: std::cout << "Invalid option.\n"; pause(1000);
        }
    }
}
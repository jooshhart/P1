#include "manager.h"
#include <iostream>

Manager::Manager(int id, const std::string& name, double salary, int teamSize)
    : Employee(id, name, salary), teamSize(teamSize) {}

void Manager::display() const {
    std::cout << "ID: " << id << " | Name: " << name << " | Salary: $" << salary
              << " | Team Size: " << teamSize << " (Manager)\n";
}

void Manager::setTeamSize(int size) { teamSize = size; }

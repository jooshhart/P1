#pragma once
#include "employee.h"

class Manager : public Employee {
    int teamSize;
public:
    Manager(int id, const std::string& name, double salary, int teamSize);
    void display() const override;
    void setTeamSize(int size);
};
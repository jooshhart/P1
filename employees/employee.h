#pragma once
#include <string>
#include <iostream>

class Employee {
protected:
    int id;
    std::string name;
    double salary;
public:
    Employee(int id, const std::string& name, double salary);
    virtual ~Employee() = default;
    virtual void display() const;
    int getId() const;
    void setName(const std::string& n);
    void setSalary(double s);
};
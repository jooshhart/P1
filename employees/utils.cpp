#include "utils.h"
#include <thread>
#include <chrono>

#ifdef _WIN32
#include <windows.h>
void clear_screen() { system("cls"); }
#else
#include <unistd.h>
void clear_screen() { system("clear"); }
#endif

void pause(int ms) {
    std::this_thread::sleep_for(std::chrono::milliseconds(ms));
}
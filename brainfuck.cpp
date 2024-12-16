#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>

using namespace std;

vector<int> memory(30000, 0); // Initialize memory with 30,000 cells
int dataPointer = 0;

void interpretBrainfuck(const string& code) {
    unordered_map<int, int> bracketMap;
    stack<int> bracketStack;

    // Preprocess brackets to handle loops
    for (int i = 0; i < code.size(); ++i) {
        if (code[i] == '[') {
            bracketStack.push(i);
        } else if (code[i] == ']') {
            int start = bracketStack.top();
            bracketStack.pop();
            bracketMap[start] = i;
            bracketMap[i] = start;
        }
    }

    for (int i = 0; i < code.size(); ++i) {
        switch (code[i]) {
            case '>':
                ++dataPointer;
                break;
            case '<':
                --dataPointer;
                break;
            case '+':
                ++memory[dataPointer];
                break;
            case '-':
                --memory[dataPointer];
                break;
            case '.':
                cout << static_cast<char>(memory[dataPointer]);
                break;
            case ',':
                memory[dataPointer] = cin.get();
                break;
            case '[':
                if (memory[dataPointer] == 0) {
                    i = bracketMap[i];
                }
                break;
            case ']':
                if (memory[dataPointer] != 0) {
                    i = bracketMap[i];
                }
                break;
        }
    }
}

int main() {
    string code;
    while (getline(cin, code)) {
        interpretBrainfuck(code);
    }
    return 0;
}
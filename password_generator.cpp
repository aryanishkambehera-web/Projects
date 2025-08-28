#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

string generatePassword(int length) {
    string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()";
    string password = "";
    srand(time(0));
    for (int i = 0; i < length; i++) {
        password += chars[rand() % chars.size()];
    }
    return password;
}

string checkStrength(string password) {
    bool hasLower=false, hasUpper=false, hasDigit=false, hasSpecial=false;
    for (char c : password) {
        if (islower(c)) hasLower = true;
        else if (isupper(c)) hasUpper = true;
        else if (isdigit(c)) hasDigit = true;
        else hasSpecial = true;
    }
    if (password.length() >= 12 && hasLower && hasUpper && hasDigit && hasSpecial)
        return "Strong";
    else if (password.length() >= 8)
        return "Moderate";
    else
        return "Weak";
}

int main() {
    int length;
    cout << "Enter password length: ";
    cin >> length;
    string pwd = generatePassword(length);
    cout << "Generated Password: " << pwd << endl;
    cout << "Strength: " << checkStrength(pwd) << endl;
    return 0;
}

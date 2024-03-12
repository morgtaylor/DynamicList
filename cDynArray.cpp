//
//  cDynArray.cpp
//  A1
//
//  Created by Morgan Dickerson.
//

#include <stdio.h>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct Contact {
    std::string firstName;
    std::string lastName;
    std::string street;
    std::string city;
    std::string state;
    std::string zip;
    std::string phone;
    std::string email;
};

int main() {
    std:ifstream inputFile("contacts.csv");
    if (!inputFile.is_open()) {
            std::cerr << "Error opening the file." << std::endl;
            return 1;
        }
    std::vector<Contact> contacts;
    std::string line;
        while (std::getline(inputFile, line)) {
            std::istringstream iss(line);
                    std::string field;

                    Contact contact;
            while (std::getline(iss, field, ',')) {
                contact.firstName
}

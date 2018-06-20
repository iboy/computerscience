//
//  SavingToAFile Extension Task
//  SavingToAFileC++
//
//  Created by Ian Grant on 06/03/2018.
//  Creative Commons ©© 2018 Ian Grant. No rights reserved.
//

#include <iostream> // this handles standard in and output
#include <fstream> // this handles opening and saving to the filesystem.
#include <sstream> // this really helps with concatenating strings and items of different datatypes
#include <string> // strings

using namespace std;

string createUsername(string firstname, string surname, string dob ) {
	// Where is the code for create username?
	// A: See Y9 GenerateUserNameFunction.cpp
}

int main() {
    //variables for registration
    string choice;
    string firstname;
    string username;
    string surname;
    string dob;
    string password;
    // variables for the login
    string enteredUsername;
    string enteredPassword;
    
    string userData[100];
    
    cout << "Do you want to Register [R] or Login [L]?\n";
    cin >> choice;
    if (choice == "R") {
        cout << "Please enter your firstname:\n>";
        cin >> firstname;
        cout << "Please enter your surname:\n>";
        cin >> surname;
        cout << "Please enter your date of birth:\n>";
        cin >> dob;
        // I use a function to create the abbreviated username
        username = createUsername(firstname, surname, dob); // where is the username function - check the other fragments
    
        cout << "Please enter a password for username: " << username << "\n";
        cin >> password;

        ofstream outputfile("personaldetails.txt", ios::app); // step 1
        outputfile << firstname << "\n"; // step 2
        outputfile << surname << "\n"; // step 3
        outputfile << dob << "\n"; // step 4
        outputfile << username << "\n"; // step 5
        outputfile << password << "\n"; // step 6
        outputfile.close(); // step 7
        cout << "User created. File saved" << endl; // confirmation message
    } // end of register user
    

        return 0;
}




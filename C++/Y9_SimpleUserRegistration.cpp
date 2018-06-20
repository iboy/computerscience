//
//  SimpleUserRegistration Extension Task
//  SimpleUserRegistration.cpp
//
//  Created by Ian Grant on 12/03/2018.
//  Creative Commons ©© 2018 Ian Grant. No rights reserved.
//

#include <iostream> // this handles standard in and output
#include <fstream> // this handles opening and saving to the filesystem.
#include <sstream> // this really helps with concatenating strings and items of different datatypes
#include <string> // strings

using namespace std;

string createUsername(string firstname, string surname, string dob ) {
    string username;
    
    
    for (string::size_type i = 0; i < 3; i++)
    {
        username = username + firstname[i];
    }
    username = username + surname[0] + dob;
    
    cout << "Username created: " << username << "\n";
    return username;
}

int main() {
    // init strings
    
    
    string firstname;
    string username;
    string surname;
    string dob;
    string password;
    
    ofstream outputfile;
    int run = 0;
    while (run < 5) {
	
    	// user input to Add New User
   		cout << "Please enter your firstname:\n>";
    	cin >> firstname;
    	cout << "Please enter your surname:\n>";
    	cin >> surname;
    	cout << "Please enter your date of birth:\n>";
    	cin >> dob;
    
    	// Call a function to create a username - assign it to a variable
    	username = createUsername(firstname, surname, dob);

    	// prompt to enter password
    	cout << "Please enter a password for username: " << username << "\n";
    	cin >> password;
    
    	// save the file - not the ios::app = append mode - this adds to a file and doesn't replace it's contents
    	outputfile.open ("Users.txt", ios::app); // step 1
    	outputfile << "Firstname," << firstname << "\n"; // step 2
    	outputfile << "Surname," << surname << "\n"; // step 3
    	outputfile << "DOB," << dob << "\n"; // step 4
    	outputfile << "Username," << username << "\n"; // step 5
    	outputfile << "Password," << password << "\n"; // step 6
    	outputfile.close(); // step 7
    	cout << "User created. File saved" << endl; // confirmation message
    	run = run + 1; // this adds to the loop control counter
	}
	return 0;
}


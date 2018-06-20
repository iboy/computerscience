//
//  SavingToAFile Extension Task
//  SavingToAFileC++
//
//  Created by Ian Grant on 06/03/2018.
//  Creative Commons ©© 2018 Ian Grant. No rights reserved.
//

#include <iostream>
#include <fstream> // this handles opening and saving to the filesystem.

using namespace std;
int main() {
    
    string firstname;
    string surname;
    string gender;
    int age;
    string favouriteFootballTeam;
    
    ofstream outputfile;
    
    cout << "Please enter your firstname:\n>";
    cin >> firstname;
    
    cout << "Please enter your surname:\n>";
    cin >> surname;
    
    cout << "Please enter your gender:\n>";
    cin >> gender;
    
    cout << "Please enter your age (in whole years):\n>";
    cin >> age;
    
    cout << "Please enter your favourite football team:\n>";
    cin >> favouriteFootballTeam;
    
    //getline(cin, input);
    //cout << "You entered: " << input << endl << endl;
    
    outputfile.open ("personaldetails.txt"); // step 1
    outputfile << "Firstname:" << firstname << "\n"; // step 2
    outputfile << "Surname:" << surname << "\n"; // step 3
    outputfile << "Gender:" << gender << "\n"; // step 4
    outputfile << "Age:" << age << "\n"; // step 5
    outputfile << "Favourite football team: " << favouriteFootballTeam << "\n"; // step 6
    outputfile.close(); // step 7
    cout << "File saved" << endl; // confirmation message
    return 0;
}


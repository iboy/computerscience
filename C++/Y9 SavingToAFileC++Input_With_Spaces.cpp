//
//  SavingToAFile Extension Task
//  SavingToAFileC++
//
//  Created by Ian Grant on 06/03/2018.
//  Creative Commons ©© 2018 Ian Grant. No rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;
int main() {
    ofstream outputfile;
    string input;
    
    // How to get a string/sentence with spaces
    cout << "Please enter a valid sentence (with spaces):\n>";
    
    getline(cin, input);
    cout << "You entered: " << input << endl << endl;
    
    outputfile.open ("example1.txt"); // step 1
    outputfile << input; // step 2
    outputfile.close(); // step 3
    cout << "File saved" << endl; // message
    return 0;
}

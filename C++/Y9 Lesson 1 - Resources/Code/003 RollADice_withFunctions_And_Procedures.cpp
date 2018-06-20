//  RollADice_With_Procedures.cpp
//  RollADice (no procedures or functions)
//
//  Problem
//  Roll two dice and print the values with the highest first.
//  And output what dice roll won.
//  Created by Ian Grant on 26/02/2018.

#include <iostream>       // std::iostream
#include <time.h>
#include <ctime>
#include <stdlib.h>
#include <sstream>

using namespace std;

// initialise variables
int roll1;
int roll2;
stringstream sstm;





int rollADice () {
	int roll = rand()% 6 +1;
    return roll;
}

string orderDice (int roll1, int roll2) {
    string result ="";

    if (roll1 > roll2) {
        sstm <<"Dice Result (highest first): " << roll1 << " then " << roll2 << "\nDice roll 1 wins\n";
        result = sstm.str();
    } else if (roll1 < roll2) {
        sstm << "Dice Result (highest first): " <<  roll2 << " then " <<  roll1 << "\nDice roll 2 wins\n";
        result = sstm.str();
    } else {
        sstm << "The dice rolls were equal: " <<  roll1 << " then " << roll2 << ".\n" ;
        result = sstm.str();
    }
    return result;
}


string outputThrow () {
    string result = "";
    
    roll1  = rollADice();
    roll2  = rollADice();
    result = orderDice(roll1, roll2);
    return result;
}

int main() {
	srand(time(0)); // this only needs to be called once and once only!
    string result = "";
    result = outputThrow();
    cout << result << endl;
    
    return 0;
}

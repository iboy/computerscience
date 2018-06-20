//  main.cpp
//  RollADice (no procedures or functions)
//
//  Problem
//  Roll two dice and print the values with the highest first.
//  And output what dice roll won.
//  Created by Ian Grant on 26/02/2018.

#include <iostream>       // std::iostream
#include <string>
#include <ctime>
#include <time.h>
#include <stdlib.h>

using namespace std;

int roll1;
int roll2;
int randomNumber;







int main() {
    
    srand(time(0));
    randomNumber = rand()% 6 +1;

    // Randomise the dice numbers for roll 1 and 2
    roll1 = randomNumber = rand()% 6 +1;
    roll2 = randomNumber = rand()% 6 +1;
    
    if (roll1 > roll2) {
        cout << "Dice Result (highest first): " << roll1 << " then " << roll2 << endl;
        cout << "Dice roll 1 wins" << endl;
    } else if (roll1 < roll2) {
        cout << "Dice Result (highest first): " << roll2 << " then " << roll1 << endl;
        cout << "Dice roll 2 wins" << endl;
    } else {
        cout << "The dice rolls were equal: " << roll1 << " then " << roll2 << endl;
    }
    return 0;
}

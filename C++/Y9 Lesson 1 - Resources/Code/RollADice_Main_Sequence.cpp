//  main.cpp
//  RollADice (no procedures or functions)
//
//  Problem
//  Roll two dice and print the values with the highest first.
//  And output what dice roll won.
//  Roll two dice and print the values with the highest first.
//  Created by Ian Grant on 26/02/2018.

#include <iostream>       // std::iostream
#include <string>
#include <iterator>
#include <vector>
#include <random>         // std::default_random_engine, std:: random_device, std::mt19937

using namespace std;

int dice1[5];
int roll1;
int roll2;
int randomIndice;



vector<int> rollADice (vector<int> indices) {
    //Adapted from https://stackoverflow.com/questions/14221763/stdrandom-shuffle-produces-same-result-each-time
    random_device r;
    seed_seq seed{r(), r(), r(), r(), r(), r(), r(), r()};
    mt19937 eng(seed);
    
    shuffle ( indices.begin(), indices.end(), eng);
    return indices;
}

int main(int argc, const char * argv[]) {
    
    vector<int> diceNumbers1({ 1, 2, 3, 4, 5, 6 });
   
    // random shuffle dice 1
    random_device r1;
    seed_seq seed1{r1(), r1(), r1(), r1(), r1(), r1(), r1(), r1()};
    mt19937 eng1(seed1);
    
    shuffle ( diceNumbers1.begin(), diceNumbers1.end(), eng1);
    
    // random shuffle dice 2
    vector<int> diceNumbers2({ 1, 2, 3, 4, 5, 6 });
    
    // random shuffle dice 2
    random_device r2;
    seed_seq seed2{r2(), r2(), r2(), r2(), r2(), r2(), r2(), r2()};
    mt19937 eng2(seed2);
    
    shuffle ( diceNumbers2.begin(), diceNumbers2.end(), eng2);

    // Randomise the dice numbers for roll 1 and 2
    roll1 = diceNumbers1[0];
    roll2 = diceNumbers2[0];
    
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

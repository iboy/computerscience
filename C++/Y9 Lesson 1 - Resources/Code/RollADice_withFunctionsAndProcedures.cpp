//  RollADice_With_Procedures.cpp
//  RollADice (no procedures or functions)
//
//  Problem
//  Roll two dice and print the values with the highest first.
//  And output what dice roll won.
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

string orderDice (int roll1, int roll2) {
    string result ="";
    if (roll1 > roll2) {
        result = "Dice Result (highest first): " + to_string(roll1) + " then " + to_string(roll2) + "\nDice roll 1 wins\n";
    } else if (roll1 < roll2) {
        result = "Dice Result (highest first): " + to_string(roll2) + " then " + to_string(roll1) + "\nDice roll 2 wins\n";
    } else {
        result = "The dice rolls were equal: " + to_string(roll1) + " then " + to_string(roll2) + ".\n" ;
    }
    return result;
}

string outputThrow () {
    string result = "";
    vector<int> diceNumbers({ 1, 2, 3, 4, 5, 6 });
    vector<int> randomDiceNumber1 = rollADice(diceNumbers);
    vector<int> randomDiceNumber2 = rollADice(diceNumbers);
    
    // Randomise the dice numbers for roll 1 and 2
    roll1 = randomDiceNumber1[0];
    roll2 = randomDiceNumber2[0];
    
    result = orderDice(roll1, roll2);
    return result;
}

int main(int argc, const char * argv[]) {
    string result = "";
    result = outputThrow();
    cout << result << endl;
    
    return 0;
}

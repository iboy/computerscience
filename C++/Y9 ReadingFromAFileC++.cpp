// This is a code fragment and will not run. Combine it with the other parts.
    if (choice == "L") {
    	
        cout << "You have chosen to login.\n";
        cout << "Please enter your username -->";
        cin >> enteredUsername;
        cout << "Please enter your password -->";
        cin >> enteredPassword;
        
        ifstream inputFile("personaldetails.txt");
        if (inputFile.is_open())
        {
            for (int i = 0; i < 100; ++i) // for now we have a fixed size for our data file
            {
                inputFile >> userData[i]; // puts the data from the file into an array
            }
            
            // now check for a valid username with a matching password
            bool found = false;
            int location = -1;
            for  (int j=3; j<100; j=j+5) // we start from 3: that is the line the username is stored
            {
                if (enteredUsername == userData[j])
                {
                    found = true;
                    location = j;
                    // check password matches
                    if (enteredPassword == userData[j+1]) // j+1 is the line the password is stored in
                    {
                        cout << "You have successfully logged in. \n";
                        cout << "Welcome " << userData[location-3] << "!\n";
                    } else {
                        cout << "Your username or password is incorrect.";
                        cout << "Please try again\n";
                    }
                    
                }
            }
            if (found == false)
            {
                    cout << "Your username or password is incorrect. \n";
                    cout << "Please try again. \n";
            }
        }
    }





class customer():
    ''' The custom class, storing the information for each customer:
    firstname, surname, town, address
    '''

    def __init__(self, firstname="First name", surname = "Surname", town="Town", telephone="020 000 0000"):
        self.firstname=firstname
        self.surname=surname
        self.town=town
        self.telephone = telephone
    
    # Next, getters and setters for the class variables
    def get_firstname(self):
        return self.firstname
    def get_surname(self):
        return self.surname
    def get_town(self):
        return self.town
    def get_telephone(self):
        return self.telephone
    
    def set_firstname(self, new_firstname):
        self.firstname=new_firstname
        
    def set_surname(self,new_surname):
        self.surname=new_surname
        
    def set_town(self,new_town):
        self.town=new_town
        
    def set_telephone(self,new_telephone):
        self.telephone = new_telephone

    # class method to print the customer details
    def print_customer(self):
        print("-------------------------")
        print("Name: ", self.firstname, " ",self.surname)
        print("Town: ", self.town)
        print("Telephone: ", self.telephone)
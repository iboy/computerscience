from customer import customer
from quote import quotation
from datetime import datetime
import pickle
import sys

customer_list = []
quotation_list = []

#main menu
def main_menu():
    print("---------------------------------------------------")
    print("Welcome to the Decoration CMS and Quotation Manager")
    print("---------------------------------------------------")
    print("[1] Add a new customer")
    print("[2] List all customers")
    print("[3] Add a new quote")
    print("[4] List all quotations")
    print("[5] Save customer details")
    print("[6] Save quotation to file")
    print("[0] Exit")
    
    choice = int(input("Select an action -->"))
    
    if choice == 1: 
        add_customer()
    if choice == 2: 
        list_all_customers()
    if choice == 3: 
        add_a_quote()
    if choice == 4: 
        list_all_quotations()
    if choice == 5: 
        save_customer_details()
    if choice == 6: 
        save_quotation()
    if choice == 0: 
        print("Session over.")
        sys.exit()
    
def add_customer():
    print("------------")
    print("Add Customer")
    print("------------")
    firstname = input("Firstname: ")
    surname = input("Surname: ")
    town = input("Town: ")
    telephone = input("Telephone number: ")
    # Aha! What is this next line?
    customer1 = customer(firstname,surname,town,telephone)
    customer1.print_customer()
    customer_list.append(customer1)
    print("Customer successfully added.")
    another = input("Would you like to add another? [y]es or [n]o?: ")
    if another == "y":
        add_customer()
    else:
        main_menu()




def list_all_customers():
    number = 1
    for cust in customer_list:
        print("------------")
        print("Customer", str(number))
        print("------------")
        cust.print_customer()
        number = number + 1
        print("\n")
        print("--------------------------------------------------------------------------")
        print("[A]dd new    [D]elete    [V]iew Quote for Customer     [B]ack to main menu")
        print("--------------------------------------------------------------------------")
    choice = input("-->")
    if choice == "a" or choice == "A":
        add_customer()
    else:
        if choice == "d" or choice == "D":
            delete_customer()
        else:
            if choice == "v" or choice == "V":
                view_quote()
            else:
                main_menu()

def add_a_quote():
    print("------------")
    print("Add a new quote")
    print("---------------")
    print("[N]ew customer    [E]xisting customer")
    choice = input("-->")
    if choice == "n" or choice == "N":
        customer1 = add_customer_for_quote()
    else:
        customer1 = search_for_existing_customer()
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    print("Underlay choice?")
    print("[F]irst Step (£5.99)    [M]onarch (£7.99)    [R]oyale (£60.00)")
    choice =input("-->")
    if choice == "f" or choice == "F":
        uname = "First Step"
    else:
        if choice == "m" or choice == "M":
            uname = "Monarch"
        else:
            if choice == "r" or choice == "R":
                uname = "Royale"
    gripper = 2*length + 2*width
    quotation1 = quotation(customer1, datetime.now(),length,width,uname,gripper)
    quotation1.print_quotation()
    print("[A]dd    [D]elete")
    choice = input("-->")
    if choice == "a" or choice == "A":
        quotation_list.append(quotation1)
        print("Quotation added successfully.")
        main_menu()
    else:
        print("Quotation deleted.")
        main_menu()


def list_all_quotations():
    number = 1
    for quote in quotation_list:
        print ("Quotation ", str(number))
        quote.print_quotation()
        number = number + 1
        print ("\n")
    print("[A]dd new    [D]elete    [B]ack to main menu")
    choice = input("-->")
    if choice == "a" or choice == "A":
        add_a_quote()
    else:
        if choice =="d" or choice == "D":
            print ("Enter a quotation number to delete")
            quote_num = int(input("-->"))
            quote = quotation_list[quote_num-1]
            print("Are you sure you wish to delete ")
            quote.print_quotation()
            choice = input("[Y]es    [N]o")
            if choice == "y" or choice == "Y":
                quotation_list.remove(quote)
                print("Quotation ", quote_num, " removed.")
                main_menu()
            else: list_all_quotations()
        else:
            main_menu()

def add_customer_for_quote():
    print("Add a new customer for quote")
    print("----------------------------")
    firstname = input("Firstname: ")
    surname = input("Surname: ")
    town = input("Town: ")
    telephone = input("Telephone number: ")
    # Aha! What is this next line?
    customer1 = customer(firstname,surname,town,telephone)
    customer_list.append(customer1)
    #print("Customer successfully added.")
    return customer1

def search_for_existing_customer():
    number = 1
    print("All customers")
    print("-------------")

    for cust in customer_list:
        print ("Customer ", str(number))
        cust.print_customer()
        number = number + 1
        print ("\n")
    print("Enter the customer number to add a quote for: ")
    cust_number = int(input("-->"))
    customer1 = customer_list[cust_number-1]
    return customer1

def delete_customer():
    print("Delete Customer")
    print("---------------")
    cust_number = int(input("Customer number to delete -->"))
    customer1 = customer_list[cust_number-1]
    print("Customer")
    customer1.print_customer()
    print("Are you sure you wish to delete?\n")
    choice = input("[Y]es    [N]o")
    if choice == "y" or choice == "Y":
        customer_list.remove(customer1)
        print("Customer deleted ...")
    main_menu()
        

def view_quote():
    print("View quote")
    print("----------")
    print("Enter the customer number to view quote")
    choice = int(input("-->"))
    customer1 = customer_list[choice-1]

    # create a dummy quote - in case the customer doesn't have one saved (?)
    target_quote = quotation(customer1, datetime.now(),0,0,"dummy",0)
    # now search for the quotation with the customer
    for quote in quotation_list:
        if quote.customer == customer1:
            target_quote = quote
    if target_quote.get_underlay_name() == "dummy":
        print("Sorry: ", customer1.get_firstname(), " does not have a quote.\n")
        print("Here is a list of all your customers.\n")
        list_all_customers()
    else:
        target_quote.print_quotation()
        choice =input("-->")
        main_menu()

def save_customer_details():
    # While we are using objects, why don't we try to save (serialise) objects directly
    # rather than writing data out to a text file?
    # Look at pickles
    pass

def save_quotation():
    # While we are using objects, why don't we try to save (serialise) objects directly
    # rather than writing data out to a text file?
    # Look at pickles
    print("Saving quotation")
    print("----------------")
    
    save_object(quotation_list,"quotations.pkl")

def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

    with open(filename, 'rb') as input:
        quotation1 = pickle.load(input)
        print(quotation1[0].customer.firstname)
        print(quotation1[0].total_price)

main_menu()
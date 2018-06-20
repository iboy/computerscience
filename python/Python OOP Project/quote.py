from customer import customer

class quotation():
    '''Quotation is a class that stores info for a quote.
    Each quotation has a customer and a quotation timestamp.
    Dimensions (length x width), underlay_name, length of gripper,
    underlay_price, which is calculated based on the underlay selected, 
    and finally the total price.'''

    def __init__(self, customer, date, length, width, uname, gripper):
        '''
        Constructor for quote
        '''
        self.customer = customer
        self.quotation_date = date
        self.length = length
        self.width = width
        self.uname = uname
        self.gripper = gripper
        self.underlay_price = self.set_underlay_price()
        self.total_price = self.set_total_price()

    # Setters and Getters
    def get_customer(self):
        return self.customer
    def get_quotation_date(self):
        return self.quotation_date
    def get_length(self):
        return self.length
    def get_width(self):
       return self.width
    def get_underlay_name(self):
        return self.uname
    def get_underlay_price(self):
        return self.underlay_price
    def get_total_price(self):
        return self.total_price
    def get_gripper(self):
        return self.gripper

    def set_customer(self, new_customer):
        self.customer = new_customer
    def set_quotation_date(self, new_quotation_date):
        self.quotation_date  = new_quotation_date
    def set_length(self, new_length):
        self.length = new_length
    def set_width(self, new_width):
        self.width = new_width
    def set_underlay_name(self,new_underlay_name):
        self.uname = new_underlay_name

    # class method to print the customer details
    def print_quotation(self):
        print("------------------")
        print("Quotation Details")
        print("------------------")
        self.customer.print_customer()
        print("Date: ", self.quotation_date.day, "-",self.quotation_date.month, "-",self.quotation_date.year)
        print("Room measurement--> length ", self.get_length(), ". Width ", self.get_width(),". Area: ",self.get_length()*self.get_width(), "meters squared" )
        print("Underlay type: ", self.get_underlay_name())
        print("Underlay price: ", self.get_underlay_price())
        print("--------------------------------------")
        print("Total Price (including labour) = ", self.get_total_price())
        print("--------------------------------------")


    # Total price calculated to include cost for material and labour costs
    def set_total_price(self):
        area = self.length*self.width
        if area >=16:
            labour_cost = (area/16) *65
        else:
            labour_cost = 65
        return (area*22.5)+(area*self.get_underlay_price())+labour_cost

    def set_underlay_price(self):
        if self.get_underlay_name() == "First Step":
            return 5.99
        else:
            if self.get_underlay_name() == "Monarch":
                return 7.99
            else: 
                if self.get_underlay_name() == "Royale":
                    return 60.00
                else:
                    return 0

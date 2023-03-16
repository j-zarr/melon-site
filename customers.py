"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self,first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def __repr__(self):
         return (
             f"<Customer: {self.first_name}, {self.last_name}, {self.email}>"
             )
    

        
def read_customer_from_file(filepath):

    customer_dict = {}

    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                email,
                password
            ) = line.rstrip().split("|")
        
            customer_dict[email] = Customer(first_name, last_name, email, password)
    
    return customer_dict

    
def get_by_email(email):
    """returns Customer instance by looking up email as key from gllobal dict"""

    return customers.get(email)

customers = read_customer_from_file("customers.txt")

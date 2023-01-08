from faker import Faker

f = Faker()

class BaseContact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def contact(self):
        print("I am choosing a " + self.phone + " and I am calling " + self.name)

    @property
    def label_length(self):
        return len(self.name)

class BusinessContact(BaseContact):
    def __init__(self, name, email, phone, position, company, business_phone):
        super().__init__(name, email, phone)
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        print("I am choosing a " + self.business_phone + " and I am calling " + self.name + " at " + self.company)

    @property
    def label_length(self):
        return len(self.name)

def create_contacts(type_of_contact, quantity):
    contacts = []
    for i in range(quantity):
        if type_of_contact == "Base":
            contact = BaseContact(name=f.name(), email=f.email(), phone=f.phone_number())
        elif type_of_contact == "Business":
            contact = BusinessContact(name=f.name(), email=f.email(), phone=f.phone_number(), position=f.job(), company=f.company(), business_phone=f.phone_number())
        contacts.append

contacts = create_contacts("Base", 5)

for contact in contacts:
    print(f"Name: {contact.name}")
    print(f"Email: {contact.email}")
    print(f"Phone: {contact.phone}")

contacts = create_contacts("Business", 3)

for contact in contacts:
    print(f"Name: {contact.name}")
    print(f"Email: {contact.email}")
    print(f"Phone: {contact.phone}")
    print(f"Position: {contact.position}")
    print(f"Company: {contact.company}")
    print(f"Business Phone: {contact.business_phone}")
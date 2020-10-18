import pdb


def get_pet_shop_name(pet_shop):
    return (pet_shop["name"])

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] = pet_shop["admin"]["total_cash"] + amount
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash_remove(pet_shop, amount):
    pet_shop["admin"]["total_cash"] = pet_shop["admin"]["total_cash"] - amount
    return pet_shop["admin"]["total_cash"]

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] = pet_shop["admin"]["pets_sold"] + 2
    return pet_shop["admin"]["pets_sold"]

def get_stock_count(pet_shop):
    pet_shop = len("pets") + 2
    return pet_shop

def get_pets_by_breed(pet_shop, breed):
    breed_amount = []
    
    for pet in pet_shop['pets']:
        if pet['breed'] == breed:
            breed_amount.append(pet)
    return breed_amount

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop['pets']:
        if pet['name'] == name:
                return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, pet):
    pet_shop['pets'].append(pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer, amount):
    customer['cash']= customer['cash'] - amount

    
def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)

def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]
    # if customer ["cash"] += ["pet_shop"]['Pets']['price']



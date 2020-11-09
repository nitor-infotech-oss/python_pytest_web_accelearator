"""
This is the common util file to perform various functions.
"""
from faker import Faker
fake = Faker()


def generate_random_email_and_password():
    """
    This function is used to generate random email and password.
    :return:
    """
    email = fake.email()

    password_string = fake.password()

    random_info = {
        'email': email,
        'password': password_string
    }
    return random_info


def generate_random_first_and_last_name():
    """
    This function is used to generate random first and last name.
    :return:
    """
    random_f_name = fake.first_name()
    random_l_name = fake.last_name()

    return {
        'f_name': random_f_name,
        'l_name': random_l_name
    }


def generate_random_details():
    """
    This function is used to generate random user details using faker package.
    :return:
    """
    full_addr = fake.address()
    addr_1 = full_addr.split("\n")[0]
    company_name = fake.company()
    city_name = fake.city()
    zip_code = fake.zipcode()
    phone_number = fake.random_int(9000000000, 9999999999)

    return {
        'company': company_name,
        'city': city_name,
        'addr_1': addr_1,
        'zip': zip_code,
        'phone': str(phone_number)

    }
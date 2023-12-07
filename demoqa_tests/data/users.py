import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    user_gender: str
    user_phone_number: str
    month: str
    year: str
    day: str
    user_subject: str
    user_hobby: str
    user_picture: str
    user_current_address: str
    user_state: str
    user_city: str


test_user = User(
    first_name='Alexander',
    last_name='Osipkin',
    user_email='alex-test.qaguru@test.com',
    user_gender='Male',  # male, famele, other (можно использовать только одно)
    user_phone_number='1234567890',
    month='June',
    year='1996',
    day='11',
    user_subject='English',
    user_hobby='Sports',  # sports, reading, music (можно использовать несколько)
    user_picture='kot-kartinka.jpg',
    user_current_address='Saint-Petersburg, Pushkin street 42',
    user_state='Uttar Pradesh',
    user_city='Agra',
)

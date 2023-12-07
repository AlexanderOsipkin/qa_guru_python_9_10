from demoqa_tests.pages.registration_page import RegistrationPage


def test_registration():
    registration_page = RegistrationPage()
    registration_page.open_registration_page()

    # WHEN
    registration_page.fill_first_name('Alexander')
    registration_page.fill_last_name('Osipkin')
    registration_page.fill_user_email('alex-test.qaguru@test.com')
    registration_page.gender_selection('Male')
    registration_page.fill_user_phone_number('1234567890')
    registration_page.fill_date_of_birth('1996', 'June', '11')
    registration_page.select_user_subject('English')
    registration_page.user_hobby_checkbox('Sports')
    registration_page.user_picture('kot-kartinka.jpg')
    registration_page.user_current_adress('Saint-Petersburg, Pushkin street 42')
    registration_page.user_state('Uttar Pradesh')
    registration_page.user_city('Agra')
    registration_page.submit_the_form()

    # THEN
    registration_page.should_registered_user_with(
        'Alexander Osipkin',
        'alex-test.qaguru@test.com',
        'Male',
        '1234567890',
        '11 June,1996',
        'English',
        'Sports',
        'kot-kartinka.jpg',
        'Saint-Petersburg, Pushkin street 42',
        'Uttar Pradesh Agra',
    )

    registration_page.close_the_form()

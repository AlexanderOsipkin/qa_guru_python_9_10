from selene import browser, have, be, by
from demoqa_tests import resource


class RegistrationPage:
    def open_registration_page(self):
        browser.open('/automation-practice-form')
        browser.element('.main-header').should(have.text('Practice Form'))
        return self

    def register(self, user):
        browser.element('#firstName').should(be.blank).type(user.first_name)
        browser.element('#lastName').should(be.blank).type(user.last_name)
        browser.element('#userEmail').should(be.blank).type(user.user_email)
        browser.element('#gender-radio-1').double_click()
        browser.element('#userNumber').should(be.blank).type(user.user_phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(
            by.text(user.month)
        ).click()
        browser.element('.react-datepicker__year-select').click().element(
            by.text(user.year)
        ).click()
        browser.element(f'.react-datepicker__day--0{user.day}').click()
        browser.element('#subjectsInput').should(be.blank).type(
            user.user_subject
        ).press_enter()
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('#uploadPicture').send_keys(resource.path(user.user_picture))
        browser.element('#currentAddress').should(be.blank).type(
            user.user_current_address
        )
        browser.element('#react-select-3-input').type(user.user_state).press_enter()
        browser.element('#react-select-4-input').type(user.user_city).press_enter()
        browser.element('#submit').press_enter()

    def should_registered_user_with(self, user):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.user_email,
                user.user_gender,
                user.user_phone_number,
                f'{user.day} {user.month},{user.year}',
                user.user_subject,
                user.user_hobby,
                user.user_picture,
                user.user_current_address,
                f'{user.user_state} {user.user_city}',
            )
        )
        return self

    def close_the_form(self):
        browser.element('#closeLargeModal').press_enter()
        return self

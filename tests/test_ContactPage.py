import pytest
from basePage import basePage
from contactPage import contactPage
from injectData import injectData

class Test_contactPage(): 
    test_data = injectData.inject_test_data("testData/testData.json")

    @pytest.mark.parametrize("input", test_data.HappyPath)    
    def test_contactPage_errors(self, browser, input):

        # Test Case: 1 ##
            # 1. From home page go to contact page 
            # 2. Click the submit button 
            # 3. Verify errror messages 
            # 4. Populate mandatory fields 
            # 5. Validate errors are gone

        page = basePage(browser)
        page.load()
        page.click_ContactPage()

        contactpage = contactPage(browser)
        contactpage.click_Submit()

        assert "Forename is required" == contactpage.get_forename_error()
        assert "Email is required" == contactpage.get_email_error()
        assert "Message is required" == contactpage.get_message_error()

        contactpage.set_forename(input.forename)
        contactpage.set_surname(input.surname)
        contactpage.set_email(input.email)
        contactpage.set_telephone(input.phone)
        contactpage.set_message(input.message)

        assert "" == contactpage.get_forename_error()
        assert "" == contactpage.get_email_error()
        assert "" == contactpage.get_message_error()
    
    @pytest.mark.repeat(5)
    @pytest.mark.parametrize("input", test_data.HappyPath)    
    def test_contactPage_submit_success(self, browser, input): 
       
        ## Test Case: 2 ##
            # 1. From home page go to contact page 
            # 2. Populate Mandatory Fields
            # 3. Click submit button 
            # 4. Validate Successful Submission message 
            # Note: Run this 5 times to ensure 100% pass rate 

        page = basePage(browser)
        page.load()
        page.click_ContactPage()

        contactpage = contactPage(browser)
        contactpage.click_Submit()

        contactpage.set_forename(input.forename)
        contactpage.set_surname(input.surname)
        contactpage.set_email(input.email)
        contactpage.set_telephone(input.phone)
        contactpage.set_message(input.message)


        contactpage.click_Submit()
        forename = input.forename     
        assert 'thanks', forename == contactPage.submit_success()

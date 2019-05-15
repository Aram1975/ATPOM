from selenium.webdriver.support.ui import Select

class Register():
    def __init__(self, driver):

        self.driver = driver

        # These are the three locators on this page
        self.input_email_xpath = "//input[@id='email']"
        self.press_button_xpath = "//img[@id='enterimg']"
        self.firstname_xpath = "//input[@placeholder='First Name']"
        self.lastname_xpath = "//input[@placeholder='Last Name']"
        self.address = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]"
        self.email_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]"
        self.phone_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]"
        self.gender_xpath = "//label[2]//input[1]"
        self.hobbies_xpath = "//input[@id='checkbox2']"

        self.language_click_xpath = "//div[@id='msdd']"
        self.language_xpath = "//a[contains(text(),'English')]"

        self.skills_xpath = "//select[@id='Skills']"
        drp = Select(self.skills_xpath)
        drp.select_by_visible_text("Python")

        self.country_xpath = "//select[@id='countries']"
        drp1 = Select(self.country_xpath)
        drp1.select_by_visible_text("Canada")

        self.year_xpath = "//select[@id='yearbox']"
        drp2 = Select(self.year_xpath)
        drp2.select_by_visible_text("1976")


        self.month_xpath = "//select[@placeholder='Month']"
        drp3 = Select(self.month_xpath)
        drp3.select_by_visible_text("May")

        self.day_xpath = "//select[@id='daybox']"
        drp4 = Select(self.day_xpath)
        drp4.select_by_visible_text("28")

        self.password_xpath = "//input[@id='firstpassword']"

        self.confirm_xpath = "//input[@id='secondpassword']"

        self.submit_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[14]/div[1]/button[1]""



    def enter_email(self):
        self.driver.find_element_by_xpath(self.input_email_xpath).click()

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def enter_Login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
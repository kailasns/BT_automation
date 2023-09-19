from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BtTest:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

    def bt_test_flow(self):
        # Test Case Steps

        # Step 1: Open the BT Mobile website
        self.driver.get("https://www.bt.com/")
        try:
            # Step 2: Close the Cookie pop-up if it appears
            cookie_popup = self.driver.find_element(By.ID, "enter popup id if any")
            if cookie_popup.is_displayed():
                cookie_popup.click()
        except:
            print("Popup was not invoked")

        # Step 4: Hover over the "Mobile" menu
        mobile_menu = self.driver.find_element(By.XPATH,
                                          "//body/div[@id='body-wrapper']/div[@id='bt-header']/nav[@id='bt-navbar']/div[2]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[4]/a[1]/span[1]")
        ActionChains(self.driver).move_to_element(mobile_menu).perform()

        # Step 5: Click on "Mobile phones" from the mobile menu
        mobile_phones_option = self.driver.find_element(By.XPATH, "//a[text()='Mobile phones']")
        mobile_phones_option.click()

        # Step 6: Wait for the page to load (you can use Webself.driverWait for better waiting)
        self.driver.implicitly_wait(10)  # Implicit wait for demonstration purposes; use Webself.driverWait for production

        # Step 7: Verify the numbers of banners present below “See Handset details” should not be less than 3
        banners = self.driver.find_elements(By.XPATH, "(//div[@class='flexpay-card_text_container__KQznu'])")
        assert len(banners) == 3, "Number of banners is  3"

        # Step 9: Click on "View SIM only deals"
        view_sim_deals = self.driver.find_element(By.XPATH, "//a[contains(text(),'View SIM only deals')]")
        view_sim_deals.click()

        # Step 11: Validate the title of the new page
        text_to_check = "Enjoy 30% off &double data"

        # Check if the text is present on the page
        if text_to_check in self.driver.page_source:
            print(f"'{text_to_check}' is present on the page.")
        else:
            print(f"'{text_to_check}' is not present on the page.")

        # Step 12: Validate the text "30% off and double data" for the 125GB 250GB Essential Plan
        plan_text = self.driver.find_element(By.XPATH, "//div[@class='sim-only-deals_gradient_bg__2BG-x']//div[10]").text
        expected_plan_text = "was 125GB 250GB Essential Plan, was £27 £18.90 per month"
        assert plan_text == expected_plan_text, f"Expected text '{expected_plan_text}' not found in '{plan_text}'"
        self.driver.quit()

from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

        """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
        """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://letskodeit.teachable.com/"
        if self.browser == "iexplore":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome(executable_path="C:\\Users\\Abinash\\Desktop\\DRIVER\\chrome"
                                                      "\\chromedriver.exe")
        else:
            driver = webdriver.Chrome(executable_path="C:\\Users\\Abinash\\Desktop\\DRIVER\\chrome"
                                                      "\\chromedriver.exe")

        driver.implicitly_wait(3)

        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver

"""
locator.py
"""

class WebLocators:


   def __init__(self):
       self.usernameLocator = "username"
       self.passwordLocator = "password"
       self.buttonLocator = "//button[@type='submit']"
       self.forgotpasswordLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p'
       self.resetpasswordLocator = '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]'
       self.resetconformationlocator = '//*[@id="app"]/div[1]/div[1]/div/h6'
       self.adminpageLocator = "//a[contains(@href,'viewAdminModule')]"

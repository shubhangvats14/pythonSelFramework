Writing Selenium Framework with Standards

- The Browser Invocation code should always be generic

- All page objects should be defined in separate classes, operations can be performed within the class e.g.,
in self.driver.find_element(By.LINK_TEXT, "Shop").click() --- self.driver.find_element(By.LINK_TEXT, "Shop") should be defined inside a different class
and click() can be performed in the actual test

- By using Page Objects concept, we need to define an object for each class from where we are returning page elements --
To overcome this, we can use the connections between objects and can just define child objects inside the parent one
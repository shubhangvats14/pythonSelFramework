Writing Selenium Framework with Standards

- The Browser Invocation code should always be generic

- All page objects should be defined in separate classes, operations can be performed within the class e.g.,
in self.driver.find_element(By.LINK_TEXT, "Shop").click() --- self.driver.find_element(By.LINK_TEXT, "Shop") should be defined inside a different class
and click() can be performed in the actual test

- By using Page Objects concept, we need to define an object for each class from where we are returning page elements --
To overcome this, we can use the connections between objects and can just define child objects inside the parent one

- If there are any common utilities, which can be used at more than one place in our code, we should try to generalize it
e.g., the explicit wait code can be generalized and can be added to the Utilities > BaseClass, as our every Test Class
will inherit BaseClass

- @staticmethod -- This needs to be added before method definition
  static methods can be called without creating class object,it can directly be called
  with ClassName., so for a class method which is static, we won't require to create an object for this Class to call.
  self is also not needed for static methods as on of the parameters
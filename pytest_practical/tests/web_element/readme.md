# Table of Contents
- [Description](#description)
- [BaseElement](#baseelement)
    * [Constructor usage](#constructor-usage)
    * [Lazy Loading](#lazy-loading)
    * [Button](#button)
    * [CheckBox](#checkbox)
    * [Dropdown](#dropdown)
    * [Label](#label)
    * [Link](#link)
    * [RadioButton](#radiobutton)
    * [Table](#table)
    * [TextBox](#textbox)
    * [Examples](#examples)
- [WebElementList](#webelementlist)
    * [Constructor Usage](#constructor-usage)
    * [Examples](#examples)

# Description
This file contains description and usage of various element casses defined under this package. First thing to note is that there are two groups of classes:
1. [BaseElement](base_element.py): Represents actions and properties for single unique element
2. [WebElementList](web_element_list.py): Represents actions and properties for list of elements usually found through find_elements_by_*

# BaseElement
This is [base class](base_element.py) containing generic properties and methods to be overridden or re-used by specific element classes. 

## Constructor usage
To have any of derived element classes initialized, there are two groups of parameters:
1. Passing driver and selector - This will be used in most cases while creating objects of specific element classes. 
Selector could be tuple, like **(By.Id, "some_id")**, or string representing name or text of web element. 
2. Passing element - This will only be used when element class needs to be initialized through element objects retrieved via [WebElementList](web_element_list.py) class

There is fourth parameter (wait_time) which can be overriden while initializing any element class. Default value is 10.

## Lazy Loading
To ensure that element is only instantiated when it is interacted with, element is found using [property](base_element.py#L36) and is not instantiated via constructor. 

Various element classes are defined below along with their usage

## Button
There are no intuitive methods that come to my mind except click, which can be directly reused from BaseElement class. So nothing defined here really.

## CheckBox
Methods specific to CheckBoxes are defined: `check(), uncheck(), is_checked() and toggle()`. 

## Dropdown
This class represents traditional selenium.webdriver.support.select.Select functionalities. So I have chosen a different name (DropDown) to ensure there is no conflict while using same. To ensure that traditional Select functionalities are used, web_element property of BaseElement is overridden to initialize Select class. 
Methods specific to Select/Dropdown are defined: `select_by_value(), select_by_index()` etc. Everything is defined as wrapper over traditional Select methods and properties. 

## Label
This class represents any static text on HTML. It could be page headers, paragraph headers, section headers or labels to text boxes or any other web elements. There is nothing specific intuitive action for Label class yet. Usually used to get @text property.

## Link
This class represents `<a>` tag

## RadioButton
This class represents radio buttons. Added one method `select()` which internally calls `click()` method. The naming makes it intuitive.

## Table
This class represents `<table>` tag. Very useful methods defined here from tester perspective: `get_rows(), get_column_headers(), get_row_count(), get_header_rows_text(), get_data_rows_text(), get_all_rows_text(), get_data_as_row_col_array()`

## TextBox
This class represents any textbox type element. As of now, there is only one method - `enter_text()` that appears to be intuitive here. 

## Examples
1. `self.client_table = Table(self.driver, (By.ID, 'DataTables_Table_0'))`
2. `self.app_login_button = Button(self.driver, (By.CSS_SELECTOR, '.sbmtLrg.sbmtOrng'))`
3. `self.email_field = TextBox(self.driver, (By.ID, "id_username"))`
4. `self.password_field = TextBox(self.driver, (By.ID, "id_password"))`
5. `self.clockins_clockouts_alerts_link = Link(self.driver, (By.LINK_TEXT, 'Clock-ins, Clock-outs, and Alerts'))`

# WebElementList
This class is created specifically to interact with list of elements that are usually found through find_elements_by_* via single selector. Since it represents list of elements it is not inheriting BaseElement class and is standalone class. It exposes [web_elements](web_element.py#L36) property to return multiple elements.

There is only one other property defined as of now which is likely to be used - text_list. This property returns the text of all elements in list.

## Constructor Usage
It does not accept string as selector. There is only tuple format, like **(By.Id, "some_id")**, of selector accepted.

## Examples
In page object, this could be used as
* `self.all_sections = WebElementList(self.driver, (By.CSS_SELECTOR, "h3.title"))`

In step implementation, text on all those sections could be retrieved as
* `labels = pages.agency_settings_page.all_sections.text_list`
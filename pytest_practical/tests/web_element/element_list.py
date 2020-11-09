from pytest_practical.tests.web_element.label import Label
from pytest_practical.tests.web_element.button import Button
from pytest_practical.tests.web_element.checkbox import CheckBox
from pytest_practical.tests.web_element.dropdown import DropDown
from pytest_practical.tests.web_element.link import Link
from pytest_practical.tests.web_element.radio_button import RadioButton
from pytest_practical.tests.web_element.textbox import TextBox


class ElementList(object):
    LABEL = Label
    BUTTON = Button
    CHECKBOX = CheckBox
    DROPDOWN = DropDown
    LINK = Link
    RADIOBUTTON = RadioButton
    TEXTBOX = TextBox

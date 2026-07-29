import time

from playwright.sync_api import Page, expect
def test_inputFieldPractice(page: Page):
    page.goto("https://letcode.in/test")
#1.Input fields
    expect(page.get_by_role("heading",name="Edit Fields")).to_be_visible()
    page.locator("div.group").filter(
        has=page.get_by_role("heading",name="Edit Fields")
    ).get_by_role("link",name="Play Sandbox").click()

    expect(page).to_have_url("https://letcode.in/edit")
    page.get_by_placeholder("Enter first & last name").fill("Nilavarasi Raj")
    #Append a text and press keyboard tab
    page.locator("#join").press_sequentially("I am happy & ")
    page.locator("#join").press("Tab")

    #----What is inside the text box?    ---loca.input_value()
    # textvalue = page.locator("#getMe").input_value()
      #Option 2 --- #use "get"
    textvalue = page.get_by_label("What is inside the text box").input_value()
    print(textvalue)

    #----Clear the text
    page.locator("#clearMe").clear()
    time.sleep(10)

    #----Confirm edit field is disabled
        #method 1
    expect(page.locator("#noEdit")).to_be_disabled()

    #-----Confirm text is readonly
    expect(page.locator("#dontwrite")).to_have_attribute("readonly","")

    expect(page.locator("#dontwrite")).to_have_value("This text is readonly")

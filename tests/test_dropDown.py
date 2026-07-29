import time

from playwright.sync_api import Page, expect


def test_dropDownPractice(page: Page):
    page.goto("https://letcode.in/test", wait_until="domcontentloaded", timeout=60000)

    page.locator("div.group").filter(
        has=page.get_by_role("heading", name="Drop-Down")
    ).get_by_role("link", name="Play Sandbox").click()

    #3. DROP DOWN
    expect(page).to_have_url("https://letcode.in/dropdowns")

    #---------Select the apple using visible text
    page.locator("#fruits").select_option(label="Apple")
    expect(page.locator("#fruits")).to_have_value("0")

    print('----------------------------------------------------')

    # Select superheroes
    page.locator("#superheros").select_option(
        label=["Aquaman", "Doc Savage", "Thor"]
    )
    page.locator("//p[contains(text(),'You have selected')]").to_be_visible(timeout=10000) ## Wait until the confirmation message appears.
    hero_message = page.locator("p.text-sm.font-medium").filter(                   # Reason: There are TWO <p class="text-sm font-medium"> elements on the page
        has_text="Aquaman"                                                         # (one for Apple selection and one for Superheroes).
    )                                                                              # Using has_text="Aquaman" uniquely identifies the superheroes message.
    expect(hero_message).to_be_visible(timeout=7000)                               # Ensure the specific hero message is visible before reading it.
    print(hero_message.text_content())                                             # Read and print the confirmation message.

    #-------------------Select the last programming language and print all the options
    page.locator("#lang").select_option(value="sharp") ## Select last programming languag
    options = page.locator("#lang option").all_text_contents() # Print all options
    print("Available languages : ")
    for option in options:
        print(option)

    #-------------------Select India using value & print the selected value
    page.locator("#country").select_option(value="India")
    selected_country = page.locator("p.text-sm.font-medium").filter(
        has_text="India"
    )
    expect(selected_country).to_be_visible(timeout=8000)
    print(selected_country.text_content())

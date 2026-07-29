from playwright.sync_api import Page, expect

def test_inputFieldPractice(page: Page):
    page.goto("https://letcode.in/test")

    expect(page.get_by_role("heading", name="Click Actions")).to_be_visible()
    page.locator("div.group").filter(
        has = page.get_by_role("heading", name="Click Actions")
    ).get_by_role("link", name="Play Sandbox").click()


    #2. CLICK ACTIONS PAGE
    expect(page).to_have_url("https://letcode.in/button")
    #----------------Goto Home and come back here using driver commands
    page.get_by_role("link", name="Goto Home").click()  # Click Goto Home
    expect(page).to_have_url("https://letcode.in/")         # Verify home page
    page.go_back()          # Come back to button page
    expect(page).to_have_url("https://letcode.in/button")   # Verify Button page
                        #Browser navigation equivalents:
                            # page.go_back()  # Browser Back
                            # page.go_forward()  # Browser Forward
                            # page.reload()  # Refresh

    #---------------Get the X & Y co-ordinates---------Using BOUNDING BOX
    location = page.get_by_role("button", name="Find Location").bounding_box()
    print("X : ", location["x"])
    print("Y : ", location["y"])

    #----------------Find the color of the button
    color = page.locator("#color").evaluate(
        "el => getComputedStyle(el).backgroundColor"
    )
    print("Background Color : ",color)

    #----------------How tall & fat I am?
    box = page.locator("#property").bounding_box()
    print("Width : ", box["width"])
    print("Height : ", box["height"])

    #----------------Confirm button is disabled
    expect(page.get_by_role("button", name="Disabled")).to_be_disabled()


    #-----------------Click and Hold Button
    hold_button = page.locator("#isDisabled").nth(1)  #✅ Use a stable id/class/unique locator
    print("Before:", hold_button.text_content())
    hold_button.hover()
    page.wait_for_timeout(3000)
    print("After:", hold_button.text_content())

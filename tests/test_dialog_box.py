import time

from playwright.sync_api import Page, expect, sync_playwright

def test_dialogBoxPractice(page: Page):
    page.goto("https://letcode.in/test", wait_until="domcontentloaded", timeout=60000)

    page.locator("div.group").filter(
        has=page.get_by_role("heading", name="Dialog Box")
    ).get_by_role("link", name="Play Sandbox").click()

    #4. DIALOG BOX
    expect(page).to_have_url("https://letcode.in/alert")
    #-------------Accept the Alert
    # page.on('dialog', lambda alert:alert.accept())
    # page.get_by_role("button", name="Simple Alert").click()
    # # time.sleep(5)


    #-------------Dismiss the Alert & print the alert text
    # def handle_dialog(dialog):
    #     print("Alert Text: ", dialog.message)
    #     dialog.dismiss()
    # page.on('dialog', handle_dialog)
    # page.get_by_role("button", name="Confirm Alert").click()
    # time.sleep(5)

    # -------------Type your name & accept
    # page.on('dialog', lambda alert:alert.accept("Nila yes"))
    # page.get_by_role("button", name="Prompt Alert").click()
    # time.sleep(5)

    #--------------Sweet alert   -------------Sweet Alert (Modern Alert), this is not a browser JavaScript dialog, so page.on("dialog") will not work.
                                             # The alert is part of the webpage DOM and should be handled like a normal element.
    page.get_by_role("button", name="Modern Alert").click()   # Click Sweet Alert button
    sweet_alert_text = page.locator("div.card-content").text_content()   # Get alert text
    print("Sweet alert Text : ", sweet_alert_text)
    page.get_by_role("button", name="close").click()

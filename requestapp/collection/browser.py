from ..models import Browsers

def check_browser_type(browser):
    if Browsers.check_if_browser_exists(browser):
        Browsers.increment_existing(browser)
    else:
        Browsers.create_new_entry(browser)


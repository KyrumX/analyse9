from django import template

from requestapp.models import Browsers

register = template.Library()

@register.simple_tag()
def display_browsers_in_table():
    html = "<table border='1'>" \
            "<tr>" \
                "<th>" \
                    "Browser type" \
                "</th>" \
                "<th>" \
                    "Amount" \
                "</th>" \
            "<tr/>"


    objects = Browsers.get_all_objects()

    for e in objects:
        html += "<tr>" \
                    "<td>" + e.browser_type + "</td>" \
                    "<td>" + str(e.amount) + "</td>" \
                "</tr>"

    html += "</table>"
    return html

from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


def nice_number(f):
    try:
        f = float(f)
    except (TypeError, ValueError) as e:
        return f, ""  # Not a float, integer or string which can be inteperted as a flaot / integer

    if f < 0:  # pull the sign out now so I know where to stop
        sign = "-"  # when going backwards
        f = -f
    else:
        sign = ""

    s = "%.2f" % f
    s = s.replace(".", ",")
    # -6 is the thousand's place  --  987654.21
    # -3 goes back 1000 at a time
    # stop at 0 instead of -1 so "999.99" doesn't lead with a ",".
    for i in range(len(s) - 6, 0, -3):  # -6 is the first thousands place
        s = s[:i] + "." + s[i:]  # Go back 1000 at a time

    return sign, s


@register.filter
def euro(f, autoescape=None) -> str:
    sign, s = nice_number(f)

    if autoescape:
        esc = conditional_escape
    else:
        def esc(x):
            return x

    result = "&euro;&nbsp;%s&nbsp;%s" % (esc(sign), esc(s))
    return mark_safe(result)


@register.filter
def euro_plain(f, autoescape=None) -> str:
    sign, s = nice_number(f)

    if autoescape:
        esc = conditional_escape
    else:
        def esc(x):
            return x

    result = "EUR %s %s" % (esc(sign), esc(s))
    return mark_safe(result)


euro.needs_autoescape = True

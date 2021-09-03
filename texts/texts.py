from django.utils.translation import gettext_lazy as _

PLAIN_CONST = _("hello")

def print_things():
    print(PLAIN_CONST)

    print(_("Without a const"))

    print(_("This time with plain %s.") % 'percent outside!')

    print(_("This time with plain %s" % 'percent inside!'))

    test_value = 'test value'

    print(_(f"This time with a formatstring: {test_value}"))

    print(_("This time with a external format: {test_value}").format(test_value=test_value))

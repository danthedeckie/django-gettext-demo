# Tests for django / gettext translations

These are for educational purposes, to see / show what actually happens,
the effect of putting `_(` in the wrong places, etc.


# To use

```sh
make
make test
```


# Explanation

This is the expected output:
```
in English
hello
Without a const
This time with plain percent outside!.
This time with plain percent inside!
This time with a formatstring: test value
This time with a external format: test value
---
now in spanish
hola
Sin una constante
Esta vez con una percent outside! sencillo.
This time with plain percent inside!
This time with a formatstring: test value
Esta vez con un formato externo: test value
```

Which shows that (from `texts/texts.py`):

```python

# A plain translated value works:
>>> print(PLAIN_CONST)
'hola'

# A plain string inside a _() works:
>>> print(_("Without a const"))
'Sin una constante'

# Using `%s` inside the _(), but acutally doing the % interpolation
# outside of the _() works:
>>> print(_("This time with plain %s.") % 'percent outside!')
'Esta vez con una percent outside! sencillo.'

# Using % *inside* the _() doesn't work:
>>> print(_("This time with plain %s" % 'percent inside!'))
'This time with plain percent inside!'

# Using a f"" inside a _() doesn't work:
>>> print(_(f"This time with a formatstring: {test_value}"))
'This time with a formatstring: test value'

# Using a {} type string, and formatting it *outside* of the _() works:
>>> print(_("This time with a external format: {test_value}").format(test_value=test_value))
'Esta vez con un formato externo: test value'
```

Apologies for incorrect Spanish

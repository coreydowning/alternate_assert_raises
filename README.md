# Alternate assertRaises

It's weird to me that assertRaises() in Python's unittest only catches the exception you specify, and otherwise lets the exception raise. I think it should provide you with a nice error message about what exception was actually raised.

To make this work:

1. `pip install pytest`
1. `py.test`

You should see two passing tests and two failing tests.
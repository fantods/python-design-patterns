# Dynamically adds new features to an object without changing implemenetation

# Pros:
# flexible alternative to subclassing
# allow for behavior modification at runtime
# can wrap component with multiple decorators
# classes should be open for extension but closed for modification

# Cons:
# results in many small objects, overuse is complex
# can complicate process of object instantiation
# complicated to have decorators track other decorators

# create decorators for HTML tags

from __future__ import print_function


class TextTag(object):
    """Represents a base text tag"""

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


simple_hello = TextTag("hello, world!")
special_hello = ItalicWrapper(BoldWrapper(simple_hello))
print("before:", simple_hello.render())
print("after:", special_hello.render())

# output:
# before: hello, world!
# after: <i><b>hello, world!</b></i>
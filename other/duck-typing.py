# allows for functions to be created that do not depend on a certain type
# especially powerful for built-in datatypes

def duck(iterable):
    for index, item in enumerate(iterable):
        print(f"Index: {index}, Item: {item}")


# can operator on arrays, dicts and strings easily
ary = [1, 2, 3, 4]
dic = {"first": 1, "second": 2, "third": 3}
st = "duck"

duck(ary)
# Index: 0, Item: 1
# Index: 1, Item: 2
# Index: 2, Item: 3
# Index: 3, Item: 4

duck(dic)
# Index: 0, Item: first
# Index: 1, Item: second
# Index: 2, Item: third

duck(st)
# Index: 0, Item: d
# Index: 1, Item: u
# Index: 2, Item: c
# Index: 3, Item: k
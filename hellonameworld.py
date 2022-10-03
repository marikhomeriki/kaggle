def hello(name=None):
    if not name:
        return "Hello, World!"
    else:
        name = name.lower().capitalize()
        return f"Hello, {name}!"


name = "mAri"

print(hello(name))

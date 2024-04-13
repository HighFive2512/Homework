def kwargs_length(**kwargs) -> int:
    return len(kwargs)


dict = {"name": "Peter", "age": 25}
print(kwargs_length(**dict))
print(kwargs_length(name="Peter", age=25))

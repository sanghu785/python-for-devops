#| 6 | 🟡 | Write a function that checks if a variable is mutable or immutable by testing its behavior |
def check_mutability(obj):
    original_id = id(obj)

    try:
        # Try common mutation patterns
        if isinstance(obj, list):
            obj.append("test")
        elif isinstance(obj, dict):
            obj["__test__"] = "test"
        elif isinstance(obj, set):
            obj.add("test")
        else:
            # For immutable types, attempt "fake mutation"
            obj = obj
    except Exception:
        return "Immutable (cannot be modified)"

    if id(obj) == original_id:
        return "Mutable (modified in place)"
    else:
        return "Immutable (new object created)"
    

if __name__ == "__main__":
    obj = input()
    check_mutability(obj)

#two
import one
print("top level in TWO.PY")
one.func()

if __name__ == "__main__":
    print("TWI directly")
else:
    print("TWO is imported")
from mypackage.age_logic import age_check
from mypackage.strings import upp_case

# Test 1: Underage
print(f"Package Age Test (10): {age_check(10)}") 

# Test 2: Adult
print(f"Package Age Test (20): {age_check(20)}")

# Test 3: String Conversion
print(f"Package String Test: {upp_case('my name is ayesha')}")
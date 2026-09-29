import random
import string
from datetime import datetime
import re 

import IronVaultArchive
from IronVaultArchive import validate_string
from IronVaultArchive import validate_date as valdate

# Generates random string to test our validation
# I think it's similar to unit tests
def gen_random_string():
    strLen = random.randint(0,50)
    return ''.join(random.choices(string.ascii_letters + string.digits + "!@#%^&&", k=strLen))


def fuzz_validate_string(iterations=100):
    for i in range(iterations):
        minN = random.randint(0,50)
        maxN = random.randint(minN, 100)
        
        test_string = gen_random_string()
        print(f"{i} Min: " + str(min) + "\tMax: " + str(maxN) + "\tString: " + test_string, end="\t")
        expected = minN <= len(test_string) <= maxN
        actual = validate_string(minN, maxN, test_string)
        print(actual)
        if expected != actual:
            print("Bug found!: minN={minN}\tmaxN={maxN} \t length={len(test_string)}")
            print(f"Expected={expected} \t actual={actual}")
    
    print(f"No failures found {iterations} tests")
    
def fuzz_validate_date(iterations = 100):
    for i in range(iterations):
        month = random.randint(-5,12)
        day = random.randint(-5, 31)
        year = random.randint(-2000, 2055)
        dateString = f"{month}/{day}/{year}"
        #dateString = gen_random_string()
        print(f"{i} Date used: { dateString}", end="\t")
        
        try:
            datetime.strptime(dateString, "%m/%d/%Y")
            expected = True
        except ValueError:
            expected = False
        
        actual = valdate(dateString)
        print(f"Expected: {expected}\tActual: {actual}")
        if expected != actual:
            print("Bug found!: { dateString}")
            print(f"Expected={expected}\t actual={actual}")
            return
    print(f"No failures found after {iterations} tests")
    
def get_rand_chars(strLen = 3, chars = "123456790()-. "):
    result = ''.join(
        random.choice(chars)
        for _ in range(random.randint(3, strLen))
    )
    return result

# AI defenition of validating a phone number
def validate_phone_number(phoneStr):
    pattern = re.compile(
        r'^'
        r'(\+?1[\s.-]?)?'    # Optinal country code
        r'(\(\d{3}\)|\d{3})' # Area code
        r'[\s.-]?'           # Optional seprator
        r'\d{3}'             # Prefix
        r'[\s.-]?'           # Optional seprator
        r'\d{4}'
        r'$'
    )
    
def fuzz_validate_phone(iterations=1000):
    for i in range(iterations):
        aCode= get_rand_chars(5)
        prefix = get_rand_chars(4)
        lineNu = get_rand_chars(4)
        
        phone_str = aCode + prefix + lineNu
        expected = IronVaultArchive.validate_phone(phone_str)
        actual = validate_phone_number(phone_str)
        print(f"Phone String: { phone_str}\t Expected: { expected }\t Actual: { actual }")
        if expected != actual:
            print (f"{i}: Bug Found: {phone_str}\tExpected={expected}\tactual={actual}")
            return
        

        
def main():
   #fuzz_validate_string()
    #fuzz_validate_date()
    fuzz_validate_phone()
    #validate_phone_number()
if __name__ =="__main__":
    main()
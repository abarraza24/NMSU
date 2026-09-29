########################################################
# Software Req Doc: SB5 Fuzz Testing Suite            #
# Release Date: September 28, 2026                    #
# Coder: Alexis Barraza                               #
# Description: This program genereates                #
# malformed input to test the phone and date           #
# validation without crashing the program              #
########################################################

import random
import string
from datetime import datetime

from IronVaultArchive import validate_phone

# Generate a random malformed string for fuzz testing
def generate_fuzzy_payload(length=15):
    """
    Generate a random string containing letters, numbers,
    punctuation, spaces, tabs, and new lines
    

    Args:
        length: The number of random characters to generate
        
    Returns:
        A randomly generated String used for fuzz testing
    """
    chars = ( string.ascii_letters + string.digits + string.punctuation + "\t\n")
    return "".join(
        random.choice(chars)
        for _ in range(length)
    )

def main():
    print("--- Ironclad Logistics: Running Fuzz Suite ---")
    
    #Generates random payloads and add specific invalid test values
    fuzz_samples = [
        generate_fuzzy_payload(12)
        for _ in range(5)
    ] + [
        "02/30/2026",
        "99/99/9999",
        "'; DROP TABLE drivers;--",
        "X" * 1000,
        "575-555-ABCD"
    ]
    
    # Loop through each payload and test it
    for i, payload in enumerate(fuzz_samples, 1):

        print(f"Test #{i} Payload: {payload}")

        # The expected phone result for malformed payloads is False
        expected_phone = False

        # Send the payload directly to validate_phone()
        actual_phone = validate_phone(payload)

        print(
            f"  -> Phone Regex Check: {actual_phone}"
        )

        # Compare the expected phone result to the actual result
        if expected_phone != actual_phone:
            print(
                f"{i}: Bug Found: {payload}\t"
                f"Expected={expected_phone}\tActual={actual_phone}"
            )

        # The expected date result starts as False
        expected_date = False

        # Try to convert the payload into a date
        try:
            datetime.strptime(payload, "%m/%d/%Y")

            # If no error occurs, the payload is a valid date
            actual_date = True

        except ValueError:

            # If ValueError occurs, the payload is not a valid date
            actual_date = False

        print(
            f"  -> Date Parser: Expected={expected_date}\t"
            f"Actual={actual_date}"
        )

        # Compare the expected date result to the actual result
        if expected_date != actual_date:
            print(
                f"{i}: Bug Found: {payload}\t"
                f"Expected={expected_date}\tActual={actual_date}"
            )

        print("-" * 45)
        
        print(f"Test #{i} Payload: {payload}")
        
        # Send the payload directly to the phone validator
        is_valid_phone = validate_phone(payload)
        
        print(f"  -> Phone Regex Check: {is_valid_phone} " 
             f"(Gracefully Evaluated)"
        )
        
        # try to process the same payload as a date
        try:
            datetime.strptime(payload, "%m/%d/%Y")

            print("  -> Date Parser: Accepted")
            
        # Catch an invalid date without crashing the program
        except ValueError:
            print(
                "  -> Date Parser: Gracefully Caught ValueError"
            )
            
        # Catch any unexpected errors during fuzz testing
        except Exception as e:
            print(f"  -> UNCAUGHT CRASH: {e}")
            
        print("-" * 45)
    
if __name__ =="__main__":
    main()
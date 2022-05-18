#!/usr/bin/env python3

"""
DNSControl presubmit script

Run before submitting, hence the pre prefix...
"""

class TestFailureError(Exception):
    """Raised when Presubmit test case failed"""
    pass

import json
import sys

def check_credentials_for_secrets():
    """check_credentials_for_secrets ensures only environment variables are present
    in creds.json

    :rasies:
        TestFailureError: If any key within a credential provider does not start with a $ indicating it is not an environment variable
    """
    creds_file="creds.json"
    with open(creds_file, "r") as creds:
        creds_data = json.load(creds)
        for provider in creds_data:
            if not all(i == '$' for i in [n[:1] for n in creds_data[provider].values()]):
                raise TestFailureError(
                    """check_credentials_for_secrets failed. 
                    Ensure credential values are all environtment 
                    variables beginning with '$'""")
    
def main():
    print("Running Presubmit Checks...")

    # List of check functions to run, easily amended, just add function name
    presubmit_checks = [
        check_credentials_for_secrets,
    ]
    # Run each check in the list
    [check() for check in presubmit_checks]

    # If a check failed then it should raise an exception, else pass.
    print("No Errors Raise, must have passed")
    sys.exit()

if __name__ == "__main__":
    main()

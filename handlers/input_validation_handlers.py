# This file holds any type of function that should validate or santize information
# All functions should get an ninput. if the input is valid, it's returning.
# If not, a print will pop to start a fresh round
# TODO: add IPv6 and Proxy validation
import re


# Make sure that the string is valid IP.
def validate_ipv4(ip_as_string: str) -> bool:
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip_as_string):
        return True
    return False


def validate_ipv6():
    pass


# Make sure that the string is valid domain.
def validate_domain(domain_as_string: str) -> bool:
    if re.match(r"^(?=.{1,253}\.?$)(?:(?!-|[^.]+_)[A-Za-z0-9-_]{1,63}(?<!-)(?:\.|$)){2,}$", domain_as_string):
        return True
    return False


# The following function have to get only the part which acts as domain or IP
# It will use the 2 functions above to return the same string if it's valid
def validate_ip_or_domain(input_string: str) -> bool:
    if sanitize_strings(input_string) and (validate_ipv4(input_string) or validate_domain(input_string)):
        return True
    return False


# TODO: Yeah. this is not really sanityzing
def sanitize_strings(income_string: str) -> bool:
    if not any(char in income_string for char in "|&`"):
        return True
    else:
        return False

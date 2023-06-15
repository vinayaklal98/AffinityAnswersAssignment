import requests, re

ADDRESSES = [
    "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050",
    "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095",
    "2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050",
    "Colony, Bengaluru, Karnataka 560050",
    "Colony, Bengaluru, Karnataka 56098",
    "374/B, 80 Feet Rd, State Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore. 560050"]

def runner():
    for address in ADDRESSES:

        # Step 1: To get the correct pincode from the given address
        pincode = get_correct_pincode(address)
        if pincode:

            # Step 2: To verify whether the postoffices retrieved from the given pincode actually lie in the address
            # Step 3: Return True if the pincode is correct else return False
            correct_address_flag = check_for_correct_address(address, pincode)
            print(correct_address_flag)
        else:
            print(False)

def get_correct_pincode(address):

    # According to Indian Postal Services, The Indian Pincodes contists of 6 digits
    # The First Step is to retrive the correct pincode to Check for the correct address

    pattern = r"\b\d{6}\b"
    # \b: Word boundary to ensure that the number is not part of a larger number.
    # \d: Matches any digit.
    # {6}: Matches exactly six occurrences of the preceding pattern (in this case, \d).
    # \b: Word boundary to ensure that the number is not part of a larger number.
    pincodes = re.findall(pattern, address)

    # If the pincodes are presnt we get them in the pincodes list and fetch the first object
    if pincodes: return pincodes[0]
    else: return None

def check_for_correct_address(address, pincode):

    # The documents for api to check for all the postoffices corresponding to the given pincode can be found at http://www.postalpincode.in/Api-Details
    postal_api = f"https://api.postalpincode.in/pincode/{pincode}"

    # The response is a json object and the status tells us if the pincode is correct or not
    data = requests.get(postal_api).json()[0]
    if data["Status"].lower() == "success":
        postoffices = [po["Name"].replace("("," ").replace(")"," ").split(" ")[0] if "(" in po["Name"] and ")" in po["Name"] else po["Name"] for po in data["PostOffice"]]
        
        # If there are more than 1 postoffices, all of them are checked.
        for postoffice in postoffices:
            if postoffice in address: return True
        else:
            return False
        
if __name__ == "__main__":
    runner()
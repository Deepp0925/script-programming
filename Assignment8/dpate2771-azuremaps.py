import requests

# 1. Insert API Key as a string that is provided by Instructor in D2L
# YOUR CODE HERE (1 line)
key = "Cw3IsowP04aitvHHLLFkPc1ZvezvKh9LKjX_FwzTT0M"

# 2. getCountry function is used to lookup the appropriate country code
# assigned to the IP Address. This function requires one argument (ip)
# You will need to insert the key and ip variables to complete the apiURL string
# Example API URL: 'https://atlas.microsoft.com/geolocation/ip/json?subscription-key=<key inside D2L>&api-version=1.0&ip=###.###.###.###


def getCountry(ip):
    apiURL = 'https://atlas.microsoft.com/geolocation/ip/json?subscription-key=' + \
        key+'&api-version=1.0&ip='+ip
    r = requests.get(apiURL)

    # Print statements are extremely helpful!
    # OPTIONAL Print statements can be used here
    # print(r.json())

    # 3. Some requests requests returned may be blank. We must write an exception handling
    # statement to avoid errors that may prevent all of the IPs from being processed.
    # You need to extract the country code from the JSON returned.
    # YOUR CODE HERE (Less than 10 lines)
    try:
        country = r.json()['countryRegion']['isoCode']
        return country
    except:
        return "Error Parsing Country Code"


def main():
    print("Good Luck")
    # Print statements are extremely helpful!
    # OPTIONAL the print statement below to test if your function is working.
    # HINT it should only print "US", and this script is done!

    print(getCountry('8.8.8.8'))


if __name__ == "__main__":
    main()

import requests

# insert your api key here for prowl -> https://aws.amazon.com/marketplace/pp/prodview-cr64x4lse5uui
headers = {"x-api-key" : "INSERT_API_KEY"}


filename = 'addresses.txt'

# open the file
file_handle = open(filename, 'r')

# read the contents of the file
file_content = file_handle.read()

# split the text of the file at each line, which
# should correspond to an IP address.
file_lines = file_content.split('\n')


for ip in file_lines:
    api_url = 'https://84h9dq7p3c.execute-api.eu-west-1.amazonaws.com/live/GetIPReputation?ip='+ip+''
    print(api_url)
    response = requests.get(api_url,headers=headers )

    if response.ok:
        print(response.content)

# Make sure to close the file!
file_handle.close()

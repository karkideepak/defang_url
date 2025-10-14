# Ask for user input
user_url = input("Enter the URL: ")

# Define the function for this process
def defang_url(url):
    # Replace '.' with '[.]', ':' with '[:]' , 'http' with 'hxxp'
    defanged = url.replace('.','[.]').replace('http','hxxp').replace(':','[:]')
    return defanged

# Display the result
final_url = defang_url(user_url)
print("Defanged URL: ", final_url)

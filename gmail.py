from simplegmail import Gmail

# Specify the path to the client secret file
client_secret_path = 'secrets/client_secret.json'

# Initialize Gmail with the specified client secret file path
gmail = Gmail(client_secret_file=client_secret_path)

# Rest of your code to read emails
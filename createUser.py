import csv
import requests

def read_csv_file(file_path):
    users = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['firstName', 'lastName', 'email', 'invite'], delimiter=';')
        next(reader)  # Skip the header row
        for row in reader:
            users.append(row)
    return users

def post_user_data(user, api_token):
    url = 'https://rss.wedo.swiss/api/admin/users/user'
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json',
    }
    data = {
        'firstName': user['firstName'],
        'lastName': user['lastName'],
        'email': user['email'],
        'userType': 'USER',
        'language': 'fr-fr',
        'invite': user['invite'].lower() == 'true'
    }
    response = requests.post(url, json=data, headers=headers)
    return response.status_code, response.json()

def main():
    csv_file_path = 'users.csv'
    api_token = 'API_TOKEN'

    users = read_csv_file(csv_file_path)
    for user in users:
        status_code, response_json = post_user_data(user, api_token)
        print(f"Status Code: {status_code}, Response: {response_json}")

if __name__ == '__main__':
    main()

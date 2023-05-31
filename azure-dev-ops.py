import requests
import os
import base64

#Enter your personal access token here or get it from your environment variables
personal_access_token = os.getenv('AZURE_DEV_OPS_KIA')

# Define your organization name and project name
organization = 'ORGANIZATION_NAME_HERE'
project = 'PROJECT_NAME_HERE'
repositoryId = 'REPOSITORY_NAME_HERE'
your_email = 'emails@email.com'

# Define your date range in the format 'YYYY-MM-DD'
from_date = '2023-05-01'
to_date = '2023-05-12'

# Get your PAT from an environment variable
pat = personal_access_token

# Encode your PAT for Basic Auth
encoded_pat = base64.b64encode(b':' + pat.encode()).decode()

url = f'https://dev.azure.com/{organization}/{project}/_apis/git/repositories/{repositoryId}/commits?searchCriteria.fromDate={from_date}&searchCriteria.toDate={to_date}&api-version=6.0'

headers = {
    'Accept': 'application/json',
    'Authorization': f'Basic {encoded_pat}',  
}

response = requests.get(url, headers=headers)


# Ensure 'value' key exists in the response before proceeding
if 'value' in response.json():
    commits = response.json()['value']  # The 'value' field contains the commits

    # List of emails to filter
    emails_to_filter = ['your_email@email.com']

    # Filter commits by email
    filtered_commits = [commit for commit in commits if commit['committer']['email'] in emails_to_filter]

    for commit in filtered_commits:
        print(commit['comment'] + "\n")
else:
    print("No commits found")

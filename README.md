# Azure DevOps Commit Log

This script fetches a list of commits from a specified Azure DevOps repository and filters them based on the committer's email and a date range.

## How It Works

The script makes use of the Azure DevOps REST API to fetch a list of commits from a specific repository within a given date range. 

The list of commits is then filtered based on the committer's email address, and the comment for each commit is printed to the console.

Here's a brief explanation of how the script works:

1. **Define the Parameters**: The script begins by setting the necessary parameters, including your Personal Access Token (PAT), the organization name, project name, repository ID, and the date range for the commits you want to fetch.

2. **Request Commits**: The script sends a GET request to the Azure DevOps API, which returns a list of commits from the specified repository within the given date range. The request uses Basic Authentication with the provided PAT.

3. **Filter Commits**: The script then filters the list of commits based on the committer's email address. This is done using a list comprehension that checks whether the email address associated with each commit is in a predefined list of email addresses.

4. **Print Commit Comments**: Finally, the script prints the comment for each commit in the filtered list to the console.

## Setup

To use this script, you will need to:

1. Set the `AZURE_DEV_OPS_KIA` environment variable with your Azure DevOps Personal Access Token (PAT), or directly replace 'your_PAT_here' in the script with your actual PAT. Remember to keep your PAT secret!

2. Replace 'knowitalls', 'WebSite', 'Mimir.vNext' in the script with your actual Azure DevOps organization, project, and repository ID.

3. (Optional) If you want to filter the commits by a different set of email addresses, modify the `emails_to_filter` list in the script.

Once you have made these changes, you can run the script with Python 3.

## Notes

- This script requires the `requests` and `base64` Python libraries.
- The Azure DevOps REST API version used in this script is 6.0. If you're using this script at a later date, you may want to check if there are newer versions of the API available.

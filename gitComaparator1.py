import requests

def compare_branches(org, repo, branch1, branch2, token):
    url = f"https://api.github.com/repos/{org}/{repo}/compare/{branch1}...{branch2}"
    headers = {'Authorization': f'token {token}'}
    
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()

        # Initialize arrays for file types
        modified_files = []
        added_files = []
        removed_files = []

        # Iterate through the files and categorize them
        for file in data['files']:
            if file['status'] == 'modified':
                modified_files.append(file['filename'])
            elif file['status'] == 'added':
                added_files.append(file['filename'])
            elif file['status'] == 'removed':
                removed_files.append(file['filename'])

        # Output the results
        print(f"Modified files: {modified_files}")
        print(f"Added files: {added_files}")
        print(f"Removed files: {removed_files}")
    else:
        print("Failed to compare branches. Status code:", response.status_code)

# Replace these variables with your organization's details
org = 'MyOrg'  # Your organization's name
repo = 'MyRepo'  # The repository's name
branch1 = 'branch1'  # The first branch to compare
branch2 = 'branch2'  # The second branch to compare
token = 'your_github_token'  # Your personal access token

compare_branches(org, repo, branch1, branch2, token)

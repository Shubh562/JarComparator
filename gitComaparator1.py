import requests

def compare_branches(user, repo, branch1, branch2, token):
    url = f"https://api.github.com/repos/{user}/{repo}/compare/{branch1}...{branch2}"
    headers = {'Authorization': f'token {token}'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"Comparing {branch1} to {branch2} in {user}/{repo}")
        print(f"Total Commits: {data['total_commits']}")
        for commit in data['commits']:
            print(f"- {commit['commit']['author']['name']}: {commit['commit']['message']}")
    else:
        print("Failed to compare branches. Status code:", response.status_code)

# Replace these variables with your own details
user = 'username'
repo = 'repo'
branch1 = 'branch1'
branch2 = 'branch2'
token = 'your_github_token'

compare_branches(user, repo, branch1, branch2, token)


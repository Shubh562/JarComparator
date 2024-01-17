import requests

def compare_branches(org, repo, base, head, token):
    url = f"https://api.github.com/repos/{org}/{repo}/compare/{base}...{head}"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code != 200:
        raise Exception(f"GitHub API Error: {data.get('message')}")

    modified_files = [file['filename'] for file in data['files'] if file['status'] == 'modified']
    new_files = [file['filename'] for file in data['files'] if file['status'] == 'added']
    deleted_files = [file['filename'] for file in data['files'] if file['status'] == 'removed']

    return modified_files, new_files, deleted_files

# Example usage
org = 'your-organization-name'
repo = 'your-repository'
base_branch = 'main'
head_branch = 'feature-branch'
token = 'your-github-token'

modified, new, deleted = compare_branches(org, repo, base_branch, head_branch, token)
print("Modified files:", modified)
print("New files:", new)
print("Deleted files:", deleted)

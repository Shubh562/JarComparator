from github import Github

def compare_branches(token, repo_name, base, head):
    g = Github(token)
    repo = g.get_repo(repo_name)

    comparison = repo.compare(base, head)

    modified_files = [file.filename for file in comparison.files if file.status == 'modified']
    new_files = [file.filename for file in comparison.files if file.status == 'added']
    deleted_files = [file.filename for file in comparison.files if file.status == 'removed']

    return modified_files, new_files, deleted_files

# Example usage
token = 'your-github-token'
repo_name = 'organization-name/repository-name'
base_branch = 'main'
head_branch = 'feature-branch'

modified, new, deleted = compare_branches(token, repo_name, base_branch, head_branch)
print("Modified files:", modified)
print("New files:", new)
print("Deleted files:", deleted)

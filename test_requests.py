import requests
import os

OWNER = "sharma-sandy"
REPO = "test-actions-repo"
PULL_NUMBER = 13


def create_file_comment(
    OWNER, REPO, PULL_NUMBER, commit_id, message, filepath, linenumber
):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{PULL_NUMBER}/comments"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
    }
    data = {
        "body": message,
        "commit_id": commit_id,
        "path": filepath,
        "line": linenumber,
    }
    r = requests.post(url, headers=headers, json=data)
    return r


def create_comment(OWNER, REPO, PULL_NUMBER, message):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{PULL_NUMBER}/comments"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
    }
    data = {
        "body": message,
    }
    r = requests.post(url, headers=headers, json=data)
    return r


res = create_comment(OWNER, REPO, PULL_NUMBER, "test comment")
print(res.status_code)

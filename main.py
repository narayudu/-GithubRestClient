# ++++++++++++++++++++ GitHub REST API Client ++++++++++++++++++++
import requests as req
import json
import datetime as dt
import yaml
import input_params as parms
from secrets import GITHUB_TOKEN

# Global variables
github_base_url = "https://api.github.com"


# ------------------ Functions for GitHub API calls -------------------------
# This function lists all Open PRs younger than given days for the given repo and the given owner
def get_open_prs(owner: str, repo: str, age: int):
    current_time = dt.datetime.utcnow()  # As GitHub returns the dates with 'Z' zeroth timezone - UTC
    aged_date_limit = current_time - dt.timedelta(days=age)
    query_url = f"{github_base_url}/repos/{owner}/{repo}/pulls"
    params_dict = {
        "state": "open"
    }
    headers_dict = {
        "Content-Type": "application/json",
        "Authorization": GITHUB_TOKEN
    }
    print("Requesting Github API to get PRs:")
    resp_json = req.get(url=query_url, params=params_dict, headers=headers_dict)
    print(f"Response code: {resp_json.status_code}")
    resp_json_list = json.loads(resp_json.content)

    filtered_pr_list = []
    for pr_dict in resp_json_list:
        pr_created_date = dt.datetime.strptime(pr_dict.get("created_at"), "%Y-%m-%dT%H:%M:%S%z").replace(tzinfo=None)
        if pr_created_date > aged_date_limit:
            filtered_pr_dict = {
                "number": "",
                "url": "",
                "title": "",
                "state": "",
                "created_at": "",
                "head": ""
            }
            for key in filtered_pr_dict.keys():
                if key == "head":
                    filtered_pr_dict.update({key: pr_dict.get(key).get("sha")})
                else:
                    filtered_pr_dict.update({key: pr_dict.get(key)})
            # print("-------------------------------------------------------------------")
            # print(filtered_pr_dict)
            # print("-------------------------------------------------------------------")
            filtered_pr_list.append(filtered_pr_dict)
    print(yaml.dump(filtered_pr_list))
    return filtered_pr_list


# This function returns all commit statuses of the given reference of  given repo and the given owner
def get_commit_status(owner: str, repo: str, ref: str):
    ref_commit_status_dict = {}
    query_url = f"{github_base_url}/repos/{owner}/{repo}/commits/{ref}/status"
    headers_dict = {
        "Content-Type": "application/json",
        "Authorization": GITHUB_TOKEN
    }
    print(f"Requesting Github API to get commit status for the reference: {ref}")
    resp_json = req.get(url=query_url, headers=headers_dict)
    print(f"Response code: {resp_json.status_code}")
    resp_json_dict = json.loads(resp_json.content)

    # Update required commit_status_dict keys and values from response json of GitHub API call
    ref_commit_status_dict.update({"state": resp_json_dict.get("state")})
    commit_status_list = []
    for commit_status in resp_json_dict.get("statuses"):
        required_commit_status_dict = {
            "state": "",
            "context": "",
            "updated_at": ""
        }
        for key in required_commit_status_dict.keys():
            required_commit_status_dict.update({key: commit_status.get(key)})
        commit_status_list.append(required_commit_status_dict)
    ref_commit_status_dict.update({"statuses": commit_status_list})
    return yaml.dump(ref_commit_status_dict)


# ------------------ Main function ------------------
def main():
    print("--------------------Listing filtered PRs--------------------------")
    pr_list = get_open_prs(parms.REP_OWNER, parms.REPO_NAME, parms.PR_AGE)
    print("------------------------------------------------------------------")
    for pr in pr_list:
        print(f"-----------------------PR-{pr.get('number')} - Commit Status -------------------------")
        print(get_commit_status(parms.REP_OWNER, parms.REPO_NAME, pr.get("head")))
        print("------------------------------------------------------------------")


if __name__ == '__main__':
    main()

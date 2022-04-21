GitHub REST API Client
This python script list all open PRs younger than a given days of a GitHub repo and their corresponding HEAD commit statuses. Currently, below default input params have been used to run the script: Repo: argo-cd Repo owner: argoproj PRs younger than: 3 days

NOTE
secrects.py should contain the GitHub Personal Access Token in order to connect to GitHub API

Build Container for this script:
Replace the 'latest' tags as per the requirement

 sudo docker build -t githubpyclient:latest .
Running as Container:
Running with default input params:

docker run githubpyclient Running with given input params:

docker run -e REPO_OWNER='flutter'
-e REPO_NAME='flutter'
-e PR_AGE=1
githubpyclient Example Output

docker run -e REPO_OWNER='argoproj'
-e REPO_NAME='argo-cd'
-e PR_AGE=1
githubpyclient

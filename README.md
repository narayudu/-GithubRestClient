GitHub REST API Client
-----------------------

This python script list all open PRs younger than a given days of a GitHub repo and their corresponding HEAD commit statuses. Currently, below default input params have been used to run the script: 

Repo: **argo-cd**

Repo owner: **argoproj** 

PRs younger than: **3 days**

**NOTE**

secrects.py should contain the GitHub Personal Access Token in order to connect to GitHub API

**Build Container for this script:**

Replace the 'latest' tags as per the requirement

             sudo docker build -t githubpyclient:latest .
**Running as Container:** Running with default input params:

              sudo docker run githubpyclient 
              
              
 --------------------Listing filtered PRs--------------------------
 
Requesting Github API to get PRs:

Response code: 200
- created_at: '2022-04-21T18:36:45Z'
- 
  head: 353487cfbd2cd2dc0b062ab16be951b50bc23484
  
  number: 9166
  
  state: open
  
  title: 'docs: 2.4 upgrade notes cmp changes'
  
  url: https://api.github.com/repos/argoproj/argo-cd/pulls/9166


-----------------------PR-9166 - Commit Status -------------------------

Requesting Github API to get commit status for the reference: 353487cfbd2cd2dc0b062ab16be951b50bc23484

Response code: 200

state: success

statuses:

- context: security/snyk (Argoproj)
- 
  state: success
  
  updated_at: '2022-04-21T18:36:51Z'
  
- context: license/snyk (Argoproj)
- 
  state: success
  
  updated_at: '2022-04-21T18:36:51Z'
  
- context: docs/readthedocs.org:argo-cd
- 
  state: success
  updated_at: '2022-04-21T18:38:06Z'
             
              
              
              


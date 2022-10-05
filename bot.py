import requests

url = "https://leetcode.com/graphql"

query = """

query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    id
    title
    titleSlug
    timestamp
  }
}
    
"""

vars = """
{
  "username": "harshitpanwar",
  "limit": 15
}
"""

response = requests.post(url=url, json={"query": query, "variables":vars})
print("response status code: ", response.status_code)
if response.status_code == 200:
    print("response : ", response.content)

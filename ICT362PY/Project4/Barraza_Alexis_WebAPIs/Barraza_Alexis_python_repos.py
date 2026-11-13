"""
Queries the GitHub API for popular Python repositories
and processes the returned JSON data.
"""

import requests
import plotly.express as px


def validate_response(status_code, response_dict):
    """Validate the API response and return the repository list."""

    if status_code != 200:
        raise ValueError("GitHub API request failed.")

    return response_dict['items']


def prepare_repo_data(repo_dicts):
    """Extract repository names, stars, and links."""

    repo_names = []
    stars = []
    repo_links = []

    for repo_dict in repo_dicts:
        repo_names.append(repo_dict['name'])
        stars.append(repo_dict['stargazers_count'])
        repo_links.append(repo_dict['html_url'])

    return repo_names, stars, repo_links


if __name__ == "__main__":
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"

    headers = {"Accept": "application/vnd.github.v3+json"}

    r = requests.get(url, headers=headers, timeout=10)

    print(f"Status code: {r.status_code}")

    response_dict = r.json()

    print(f"Total repositories: {response_dict['total_count']}")

    repo_dicts = validate_response(r.status_code, response_dict)

    print(f"Repositories returned: {len(repo_dicts)}")

    repo_names, stars, repo_links = prepare_repo_data(repo_dicts)

    # Create clickable repository names and hover information.
    repo_links_display = []
    hover_texts = []

    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']

        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links_display.append(repo_link)

        owner = repo_dict['owner']['login']
        description = repo_dict['description'] or "No description available."

        hover_text = f"{owner}<br />{description}"
        hover_texts.append(hover_text)

    title = "Most-Starred Python Projects on GitHub"

    labels = {
        'x': 'Repository',
        'y': 'Stars'
    }

    fig = px.bar(
        x=repo_links_display,
        y=stars,
        title=title,
        labels=labels,
        hover_name=hover_texts
    )

    fig.show()
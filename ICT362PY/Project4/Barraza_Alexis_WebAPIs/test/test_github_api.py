from Barraza_Alexis_python_repos import validate_response, prepare_repo_data


def test_successful_status_code():
    """REQ-API-01: Test that a successful status code is accepted."""

    response_dict = {
        'items': []
    }

    repo_dicts = validate_response(200, response_dict)

    assert repo_dicts == []


def test_repository_data_is_parsed():
    """REQ-API-02: Test that repository data is read from the response dictionary."""

    response_dict = {
        'items': [
            {
                'name': 'test-project',
                'stargazers_count': 100,
                'html_url': 'https://github.com/test/test-project'
            }
        ]
    }

    repo_dicts = validate_response(200, response_dict)

    assert len(repo_dicts) == 1
    assert repo_dicts[0]['name'] == 'test-project'


def test_repository_values_are_prepared():
    """REQ-API-03: Test that repository values are prepared for Plotly."""

    repo_dicts = [
        {
            'name': 'test-project',
            'stargazers_count': 100,
            'html_url': 'https://github.com/test/test-project'
        }
    ]

    repo_names, stars, repo_links = prepare_repo_data(repo_dicts)

    assert repo_names[0] == 'test-project'
    assert stars[0] == 100
    assert repo_links[0] == 'https://github.com/test/test-project'
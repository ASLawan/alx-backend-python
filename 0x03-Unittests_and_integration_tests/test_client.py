#!/usr/bin/env python3
"""
    Module implementing test classes for GithubOrgClient

"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from utils import get_json
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient"""
    @parameterized.expand([
        ("google", {"login": "google", "id": 1, "repos_url":
                             "https://api.github.com/orgs/google/repos"}),
        ("abc", {"login": "abc", "id": 2, "repos_url":
                          "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected_json, mock_get_json):
        """Test GithubOrgClient"""
        mock_get_json.return_value = expected_json

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with
        (GithubOrgClient.ORG_URL.format(org=org_name))
        self.assertEqual(result, expected_json)

    def test_public_repos_url(self):
        """Tests GithubOrgClient._public_repos_url method"""
        expected_payload = {"login": "google", "repos_url":
                            "https://api.github.com/orgs/google/repos"}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = expected_payload
            client = GithubOrgClient("google")
            result = client._public_repos_url

            self.assertEqual(result, expected_payload["repos_url"])


if __name__ == "__main__":
    unittest.main()

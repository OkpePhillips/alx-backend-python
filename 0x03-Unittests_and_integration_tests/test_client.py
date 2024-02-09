#!/usr/bin/env python3
"""
GihubClient test module
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    GithubOrgClient test class
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.utils.get_json", return_value={"repos_url":
           "https://api.github.com/orgs/{}/repos".format("example")})
    #@patch("client.get_json", return_value={"repos_url":
     #      "https://api.github.com/orgs/{}/repos".format("example")})
    def test_org(self, org_name, mock_get_json):
        """Test the GithubOrgClient.org method."""
        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with("https://api.github.com\
                                              /orgs/{}/repos".format(org_name))
        mock_get_json.assert_not_called()

        self.assertEqual(result, {"repos_url": "https://api.github.com\
                                  /orgs/{}/repos".format("example")})


if __name__ == '__main__':
    unittest.main()

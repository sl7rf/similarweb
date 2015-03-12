import json
import httpretty
from similarweb import SourcesClient


def test_sources_client_has_user_key():
    client = SourcesClient("test_key")

    assert client.user_key == "test_key"


def test_sources_client_has_base_url():
    client = SourcesClient("test_key")

    assert client.base_url == "http://api.similarweb.com/Site/%(url)s/%(version)s/"


def test_sources_client_has_empty_full_url():
    client = SourcesClient("test_key")

    assert client.full_url == ""


@httpretty.activate
def test_sources_client_social_referrals_completes_full_url():
    target_url = ("http://api.similarweb.com/Site/"
                  "example.com/v1/SocialReferringSites?"
                  "UserKey=test_key")
    f = "test_fixtures/sources_client_social_referrals_good_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        client.social_referrals("example.com")

        assert client.full_url == target_url


@httpretty.activate
def test_sources_client_social_referrals_response_from_invalid_api_key():
    expected = {"Error": "user_key_invalid"}
    target_url = ("http://api.similarweb.com/Site/"
                  "example.com/v1/SocialReferringSites?"
                  "UserKey=invalid_key")
    f = "test_fixtures/sources_client_social_referrals_invalid_api_key_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("invalid_key")
        result = client.social_referrals("example.com")

        assert result == expected


@httpretty.activate
def test_sources_client_social_referrals_response_from_malformed_url():
    expected = {"Error": "Malformed or Unknown URL"}
    target_url = ("http://api.similarweb.com/Site/"
                  "bad_url/v1/SocialReferringSites?"
                  "UserKey=test_key")
    f = "test_fixtures/sources_client_social_referrals_url_malformed_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        result = client.social_referrals("bad_url")

        assert result == expected


@httpretty.activate
def test_sources_client_social_referrals_response_from_malformed_url_incl_http():
    expected = {"Error": "Malformed or Unknown URL"}
    target_url = ("http://api.similarweb.com/Site/"
                  "http://example.com/v1/SocialReferringSites?"
                  "UserKey=test_key")
    f = "test_fixtures/sources_client_social_referrals_url_with_http_response.json"
    with open(f) as data_file:
        stringified = data_file.read().replace("\n", "")
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        result = client.social_referrals("http://example.com")

        assert result == expected


@httpretty.activate
def test_sources_client_social_referrals_response_from_empty_response():
    expected = {"Error": "Unknown Error"}
    target_url = ("http://api.similarweb.com/Site/"
                  "example.com/v1/SocialReferringSites?"
                  "UserKey=test_key")
    f = "test_fixtures/sources_client_social_referrals_empty_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        result = client.social_referrals("example.com")

        assert result == expected


@httpretty.activate
def test_sources_client_social_referrals_response_from_good_inputs():
    expected = {"SocialSources": {
                  "Facebook": 0.5872484011274256,
                  "Reddit": 0.1955231030114612,
                  "Twitter": 0.13209235484709875,
                  "Youtube": 0.06292737412742913,
                  "Weibo.com": 0.010782551614770926},
                "StartDate": "12/2014",
                "EndDate": "02/2015"}
    target_url = ("http://api.similarweb.com/Site/"
                  "example.com/v1/SocialReferringSites?"
                  "UserKey=test_key")
    f = "test_fixtures/sources_client_social_referrals_good_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        result = client.social_referrals("example.com")

        assert result == expected


@httpretty.activate
def test_sources_client_organic_search_keywords_completes_full_url():
    target_url = ("http://api.similarweb.com/Site/"
                  "example.com/v1/orgsearch?start=11-2014&"
                  "end=12-2014&md=False&page=1&UserKey=test_key")
    f = "test_fixtures/sources_client_organic_search_keywords_good_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        client.organic_search_keywords("example.com", 1, "11-2014", "12-2014", False)

        assert client.full_url == target_url


@httpretty.activate
def test_sources_client_organic_search_keywords_response_from_invalid_api_key():
    expected = {"Error": "user_key_invalid"}
    target_url = ("http://api.similarweb.com/Site/"
                  "example.com/v1/orgsearch?start=11-2014&"
                  "end=12-2014&md=False&page=1&UserKey=invalid_key")
    f = "test_fixtures/sources_client_organic_search_keywords_invalid_api_key_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("invalid_key")
        result = client.organic_search_keywords("example.com", 1, "11-2014", "12-2014", False)

        assert result == expected


@httpretty.activate
def test_sources_client_organic_search_keywords_response_from_malformed_url():
    expected = {"Error": "Malformed or Unknown URL"}
    target_url = ("http://api.similarweb.com/Site/"
                  "bad_url/v1/orgsearch?start=11-2014&"
                  "end=12-2014&md=False&page=1&UserKey=test_key")
    f = "test_fixtures/sources_client_organic_search_keywords_url_malformed_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        result = client.organic_search_keywords("bad_url", 1, "11-2014", "12-2014", False)

        assert result == expected


@httpretty.activate
def test_sources_client_organic_search_keywords_response_from_malformed_url_incl_http():
    expected = {"Error": "Malformed or Unknown URL"}
    target_url = ("http://api.similarweb.com/Site/"
                  "http://example.com/v1/orgsearch?start=11-2014&"
                  "end=12-2014&md=False&page=1&UserKey=test_key")
    f = "test_fixtures/sources_client_organic_search_keywords_url_with_http_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        result = client.organic_search_keywords("http://example.com", 1, "11-2014", "12-2014", False)

        assert result == expected


@httpretty.activate
def test_sources_client_organic_search_keywords_response_from_bad_page():
    expected = {"Error": "The field Page is invalid."}
    target_url = ("http://api.similarweb.com/Site/"
                  "example.com/v1/orgsearch?start=11-2014&"
                  "end=12-2014&md=False&page=0&UserKey=test_key")
    f = "test_fixtures/sources_client_organic_search_keywords_page_bad_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        result = client.organic_search_keywords("example.com", 0, "11-2014", "12-2014", False)

        assert result == expected


@httpretty.activate
def test_sources_client_organic_search_keywords_response_from_bad_start_date():
    expected = {"Error": "The value '14-2014' is not valid for Start."}
    target_url = ("http://api.similarweb.com/Site/"
                  "example.com/v1/orgsearch?start=14-2014&"
                  "end=12-2014&md=False&page=0&UserKey=test_key")
    f = "test_fixtures/sources_client_organic_search_keywords_start_bad_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        result = client.organic_search_keywords("example.com", 0, "14-2014", "12-2014", False)

        assert result == expected


@httpretty.activate
def test_sources_client_organic_search_keywords_response_from_bad_end_date():
    expected = {"Error": "The value '0-2014' is not valid for End."}
    target_url = ("http://api.similarweb.com/Site/"
                  "example.com/v1/orgsearch?start=11-2014&"
                  "end=0-2014&md=False&page=0&UserKey=test_key")
    f = "test_fixtures/sources_client_organic_search_keywords_end_bad_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        result = client.organic_search_keywords("example.com", 0, "11-2014", "0-2014", False)

        assert result == expected


@httpretty.activate
def test_sources_client_organic_search_keywords_response_out_of_order_dates():
    expected = {"Error": "Date range is not valid"}
    target_url = ("http://api.similarweb.com/Site/"
                  "example.com/v1/orgsearch?start=12-2014&"
                  "end=9-2014&md=False&page=0&UserKey=test_key")
    f = "test_fixtures/sources_client_organic_search_keywords_out_of_order_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        result = client.organic_search_keywords("example.com", 0, "12-2014", "9-2014", False)

        assert result == expected


@httpretty.activate
def test_sources_client_organic_search_keywords_response_empty_response():
    expected = {"Error": "Unknown Error"}
    target_url = ("http://api.similarweb.com/Site/"
                  "example.com/v1/orgsearch?start=11-2014&"
                  "end=12-2014&md=False&page=0&UserKey=test_key")
    f = "test_fixtures/sources_client_organic_search_keywords_empty_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        result = client.organic_search_keywords("example.com", 0, "11-2014", "12-2014", False)

        assert result == expected


@httpretty.activate
def test_sources_client_organic_search_keywords_response_from_good_inputs():
    target_url = ("http://api.similarweb.com/Site/"
                  "example.com/v1/orgsearch?start=11-2014&"
                  "end=12-2014&md=False&page=0&UserKey=test_key")
    f = "test_fixtures/sources_client_organic_search_keywords_good_response.json"
    with open(f) as data_file:
        stringified = json.dumps(json.load(data_file))
        expected = json.loads(stringified) # <~ TODO noodle a better resultant data structure
        httpretty.register_uri(httpretty.GET, target_url, body=stringified)
        client = SourcesClient("test_key")
        result = client.organic_search_keywords("example.com", 0, "11-2014", "12-2014", False)

        assert result == expected


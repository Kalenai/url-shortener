from urllib.parse import urlparse
from datetime import datetime, timedelta
from flask import request
from tests.base import BaseTestCase
from app import db
from app.models import UrlLink


class TestApiService(BaseTestCase):
    """
    Test the API for the URL Shortener Service.
    """
    def test_should_return_original_and_new_url_when_passed_valid_url(self):
        url = "https://github.com/Kalenai/url-shortener"
        response = self.client.get("/new/" + url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, dict(original_url=url,
                                             short_url=request.url_root + UrlLink.query.filter_by(url=url).first().url_key))

    def test_should_return_error_400_when_passed_invalid_url(self):
        url = "hello world!"
        response = self.client.get("/new/" + url)
        self.assertEqual(response.status_code, 400)

    def test_should_redirect_to_original_url_when_passed_valid_url_link(self):
        url = "https://github.com/Kalenai/url-shortener"
        url_key = "pretty-bird"
        url_link = UrlLink(url_key, url)
        db.session.add(url_link)
        db.session.commit()
        response = self.client.get("/" + url_key, follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.location).geturl(), url)

    def test_should_return_error_404_when_passed_invalid_url_link(self):
        url_key = "ugly-bird"
        url_link = UrlLink("pretty-bird", "https://github.com/Kalenai/url-shortener")
        db.session.add(url_link)
        db.session.commit()
        response = self.client.get("/" + url_key)
        self.assertEqual(response.status_code, 404)

    def test_should_initialize_created_date_to_today_when_url_link_is_created(self):
        url_key = "pretty-bird"
        url_link, created_time = UrlLink(url_key, "https://github.com/Kalenai/url-shortener"), datetime.utcnow()
        db.session.add(url_link)
        db.session.commit()
        self.assertTrue(UrlLink.query.filter_by(url_key=url_key).first().created - created_time < timedelta(seconds=10))

    def test_should_update_last_used_date_in_db_when_url_link_is_used(self):
        url_key = "pretty-bird"
        url_link = UrlLink(url_key, "https://github.com/Kalenai/url-shortener")
        db.session.add(url_link)
        db.session.commit()
        self.assertTrue(UrlLink.query.filter_by(url_key=url_key).first().last_used is None)
        response = self.client.get("/" + url_key)
        self.assertTrue(UrlLink.query.filter_by(url_key=url_key).first().last_used -
                        UrlLink.query.filter_by(url_key=url_key).first().created > timedelta(seconds=0))

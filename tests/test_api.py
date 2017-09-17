from .base import BaseTestCase


class TestApiService(BaseTestCase):
    """
    Test the API for the URL Shortener Service.
    """
    def should_return_original_and_new_url_when_passed_valid_url(self):
        pass

    def should_return_error_400_when_passed_invalid_url(self):
        pass

    def should_redirect_to_original_url_when_passed_valid_url_link(self):
        pass

    def should_return_error_404_when_passed_invalid_url_link(self):
        pass

    def should_initialize_created_date_to_today_when_url_link_is_created(self):
        pass

    def should_update_last_used_date_in_db_when_url_link_is_used(self):
        pass

import os
import unittest
import json

from app import App, handle_mentions

class TestingMethods(unittest.TestCase):

    def test_index(self):
        tester = App.test_client()
        response = tester.get('/')
        self.assertEqual(response.data, b'Welcome to our server !!')

    def test_event_hooke_token_failure(self):
        tester = App.test_client()
        mock_json_dict = {
            'token' : {},
            'type' : 'url_verification'

        }
        response = tester.get('/slack/events', json={"json_dict": mock_json_dict})
        self.assertEqual(response.status_code, 404)

    def test_handle_mentions_fail(self):
        mock_event_data= {'token': '7Ib6bXFUptn52u7TdjBjqMqe', 'team_id': 'T02KYHXGHJ6', 'api_app_id': 'A02KYJL0A9H', 'event': {'client_msg_id': '3fb9758f-ca84-4d22-95ec-0303eeefd1c6', 'type': 'app_mention', 'text': '<@U02KRSFHYMC>!H', 'user': 'U02L0QF4X7E', 'ts': '1639171546.008100', 'team': 'T02KYHXGHJ6', 'blocks': [{'type': 'rich_text', 'block_id': 'FIp2', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'user', 'user_id': 'U02KRSFHYMC'}, {'type': 'text', 'text': '!AP True Sully2'}]}]}], 'channel': 'C02LB6AB7B3', 'event_ts': '1639171546.008100'}, 'type': 'event_callback', 'event_id': 'Ev02PXGNQVJT', 'event_time': 1639171546, 'authorizations': [{'enterprise_id': None, 'team_id': 'T02KYHXGHJ6', 'user_id': 'U02KRSFHYMC', 'is_bot': True, 'is_enterprise_install': False}], 'is_ext_shared_channel': False, 'event_context': '4-eyJldCI6ImFwcF9tZW50aW9uIiwidGlkIjoiVDAyS1lIWEdISjYiLCJhaWQiOiJBMDJLWUpMMEE5SCIsImNpZCI6IkMwMkxCNkFCN0IzIn0'}
        response = handle_mentions(event_data=mock_event_data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
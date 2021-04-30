from io import BytesIO
import pytest


class TestIndex:
    def setup(self):
        self.test_file = (BytesIO(b'The quick brown fox jumped lazily over the dog!'), 'test_file.txt')

    @staticmethod
    def test_get_index(client):
        res = client.get('/')
        assert res.status_code == 200

    def test_post_index(self, client):
        test_words = 'fox, dog, over'
        res = client.post(
            data={
                'secretFile': self.test_file,
                'sensitiveWords': test_words
            },
            content_type='multipart/form-data'
        )

        assert res.status_code == 200
        file = self.download_file(client)
        expected_output = b'The quick brown XXXXXXXX jumped lazily XXXXXXXX the XXXXXXXX!'

        assert file.data == expected_output

    def test_post_no_file(self, client):
        test_words = 'fox, dog, over'
        res = client.post(data={'sensitiveWords': test_words})
        assert res.status_code == 400

    def test_post_no_redact_words_sent(self, client):
        res = client.post(data={'secretFile': self.test_file})
        assert res.status_code == 400

    def test_post_no_words_found_to_redact(self, client):
        test_words = 'python, redact, cars'
        res = client.post(data={'secretFile': self.test_file, 'sensitiveWords': test_words})

        assert res.status_code == 200
        file = self.download_file(client)
        expected_output = b'The quick brown fox jumped lazily over the dog!'

        assert file.data == expected_output

    @staticmethod
    @pytest.mark.skip(reason='This test is broken right now because of the change to the file download.')
    def download_file(client):
        # TODO: this test has broken with the new way files are downloaded.
        #   It will need to be rewritten
        return client.post('/download-file')

    def teardown(self):
        pass

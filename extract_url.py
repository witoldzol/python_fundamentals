import unittest


def drop_protocol(url: str) -> str:
    if 'http' in url or 'https' in url:
        return ''.join(url.split('//')[1:])
    return url


def drop_sub_domain(url):
    print(f'url = {url}')
    if 'www' in url:
        return '.'.join(url.split('.')[1:])
    return url


def extract_domain(url):
    return url.split('.')[0]


def domain_name(url: str):
    no_protocol = drop_protocol(url)
    no_subdomain = drop_sub_domain(no_protocol)
    return extract_domain(no_subdomain)

def better_domain_name(url:str):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]

class TestExtractor(unittest.TestCase):

    def test_extractor(self):
        self.assertEqual(domain_name("http://google.com"), "google")
        self.assertEqual(domain_name("http://google.co.jp"), "google")
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")
        self.assertEqual(domain_name("https://youtube.com"), "youtube")
        self.assertEqual(better_domain_name("http://google.com"), "google")
        self.assertEqual(better_domain_name("http://google.co.jp"), "google")
        self.assertEqual(better_domain_name("www.xakep.ru"), "xakep")
        self.assertEqual(better_domain_name("https://youtube.com"), "youtube")

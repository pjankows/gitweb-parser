try:
    from html.parser import HTMLParser
except ImportError:
    from HTMLParser import HTMLParser


class GitwebHTMLParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        self.files = {}
        self.dirs = {}
        self.in_td_list = False
        self.in_td_link = False
        self.current_item_name = None
        super(GitwebHTMLParser, self).__init__(*args, **kwargs)

    def _handle_td(self, attrs):
        if 'class' in attrs and attrs['class'] == 'list':
            self.in_td_list = True
        if 'class' in attrs and attrs['class'] == 'link':
            self.in_td_link = True

    def _handle_a(self, attrs):
        if self.in_td_link and 'href' in attrs:
            if 'a=tree' in attrs['href']:
                self.dirs[self.current_item_name] = attrs['href']
            if 'a=blob_plain' in attrs['href']:
                self.files[self.current_item_name] = attrs['href']

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self._handle_td(dict(attrs))
        if tag == 'a':
            self._handle_a(dict(attrs))

    def handle_data(self, data):
        if self.in_td_list:
            self.current_item_name = data

    def handle_endtag(self, tag):
        if tag == 'td' and (self.in_td_link or self.in_td_list):
            self.in_td_list = False
            self.in_td_link = False

import webbrowser
class GoogleSearch():
    def browse_item(self,*search_items):
        for search_item in search_items:
            url=f"https://www.google.com/search?q={search_item}"
            webbrowser.open_new_tab(url)

class UrlBrowse():
    def browse_url(self,*search_url):
        for url in search_url:
            webbrowser.open_new_tab(url)
            

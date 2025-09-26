import webbrowser

def validate_url(func):
  def wrapper(url):
    if "." in url:
      func(url)
      print("URL is valid and opened.")
    else:
      print("Invalid URL")
  return wrapper

@validate_url
def open_url(url):
  webbrowser.open(url)


open_url("https://www.example.com")
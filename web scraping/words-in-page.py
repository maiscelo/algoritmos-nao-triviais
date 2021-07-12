import nltk

from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import urllib.request
import plotly.io as pio
page =  urllib.request.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')
html_plain = page.read()
print(html_plain)
soup = BeautifulSoup(html_plain,'html.parser')
soup_text = soup.get_text(strip = True)
ready_text = soup_text.lower()
print(ready_text)
tokens = []
for t in ready_text.split():
    tokens.append(t)
nltk.download('stopwords')
stop_words = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stop_words:
        clean_tokens.remove(token)
print(clean_tokens)
freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print('Word: ' + str(key) + ', Quantity:' + str(val)
high_freq = dict()
for key, val in freq.items():
    if (val > 10):
        high_freq[key] = val
 #Note: to pass keys and values of high_freq dictionary, I had to convert them to list when passing them
fig = dict({
    "data": [{"type": "bar",
              "x": list(high_freq.keys()),
              "y": list(high_freq.values())}],
    "layout": {"title": {"text": "Most frequently used words in the page"}, "xaxis": {"categoryorder":"total descending"}}
})
pio.show(fig)

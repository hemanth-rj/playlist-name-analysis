import pandas as pd
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

file_path = r'<include path>'
playlists_df = pd.read_csv(file_path, encoding='latin-1')
playlists = playlists_df['playlist_name'].tolist()
playlists_cleaned = [re.sub(r'[^\w\s]', '', playlist.lower()) for playlist in playlists]
all_words = ' '.join(playlists_cleaned).split()
stop_words = set(stopwords.words('english'))
all_words_filtered = [word for word in all_words if word not in stop_words]
word_counts = Counter(all_words_filtered)
df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])
df = df.sort_values(by='Frequency', ascending=False)
print(df.head(20))
df.to_csv(r'C:\Users\rj_he\Desktop\Hoopr\Product\Music\consumer_playlist_word_frequency.csv', index=False)

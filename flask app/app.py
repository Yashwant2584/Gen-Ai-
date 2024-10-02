#flask app
from flask import Flask, request, render_template
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the dataset from the backend (local CSV file)
def load_books_data():
    return pd.read_csv('books.csv')

df = load_books_data()

# Check if necessary columns exist in the dataset
if 'Title' not in df.columns or 'Genre' not in df.columns:
    raise Exception("The dataset must contain at least 'Title' and 'Genre' columns.")

# Create a column for recommendation (concatenating Genre if needed)
df['features'] = df['Genre']

# Convert the 'features' (i.e., Genre) into vectors using CountVectorizer
cv = CountVectorizer()
vector_matrix = cv.fit_transform(df['features'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(vector_matrix)

# Function to get the index of a book title
def get_index_from_title(title):
    return df[df.Title == title].index.values[0]

# Function to get the title from the index
def get_title_from_index(index):
    return df.iloc[index]['Title']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the book title from the form
        book_title = request.form.get('book_title')
        if book_title:
            # Get the index of the selected book
            book_index = get_index_from_title(book_title)

            # Get list of similarity scores for the selected book
            similar_books = list(enumerate(cosine_sim[book_index]))

            # Sort the books based on similarity scores
            sorted_similar_books = sorted(similar_books, key=lambda x: x[1], reverse=True)[1:6]

            # Get the titles of the recommended books
            recommended_books = [get_title_from_index(index) for index, _ in sorted_similar_books]

            return render_template('index.html', book_title=book_title, recommended_books=recommended_books)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


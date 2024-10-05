Here is a basic **README.md** file for your Flask-based Book Recommendation System:

---

# Book Recommendation System (Flask)

This project is a simple **Book Recommendation System** built using **Flask**. It recommends books based on their genres using the **Cosine Similarity** technique.

## Features
- Displays a list of book titles.
- Recommends the top 5 similar books based on the genre of the selected book.
- Simple web interface to choose a book and view recommendations.

## Technologies Used
- **Flask**: A micro web framework for Python.
- **Pandas**: For data manipulation and handling the dataset.
- **scikit-learn**: For calculating cosine similarity between genres.
- **HTML**: For the frontend structure.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/book-recommendation-system-flask.git
cd book-recommendation-system-flask
```

### 2. Install Dependencies
First, ensure you have Python installed. Then, install the required Python packages using `pip`:
```bash
pip install flask pandas scikit-learn
```

### 3. Dataset
Ensure you have a **books.csv** file containing at least two columns:
- `Title`: The title of the book.
- `Genre`: The genre of the book.

The CSV file should be placed in the project directory.

Example of `books.csv`:

| Title          | Genre         |
|----------------|---------------|
| Book 1         | Fiction       |
| Book 2         | Thriller      |
| Book 3         | Romance       |
| ...            | ...           |

### 4. Run the Flask App
To start the Flask application, run the following command:
```bash
python app.py
```

The app will run on `http://127.0.0.1:5000/`.

### 5. Access the Web Interface
Open your browser and navigate to `http://127.0.0.1:5000/`. You will see a dropdown menu to select a book title, and after submitting, the system will display 5 similar books based on genre.

## How It Works
1. The dataset (`books.csv`) is loaded.
2. The `Genre` column is vectorized using **CountVectorizer** from scikit-learn.
3. **Cosine Similarity** is calculated between the genre vectors.
4. Based on the selected book's genre, the system recommends the top 5 books with similar genres.

## File Structure

```bash
book-recommendation-system-flask/
│
├── app.py                # Main Flask application
├── books.csv             # Dataset containing books and genres
├── templates/
│   └── index.html        # HTML file for the user interface
├── README.md             # Project README file
```

## Screenshots
### Home Page
<img src="path_to_screenshot" width="500" alt="Home page">

### Book Recommendation
<img src="path_to_screenshot" width="500" alt="Book recommendations">

## Contributing
If you'd like to contribute to this project, feel free to submit a pull request or raise an issue.

## License
This project is open source and available under the MIT License.

---

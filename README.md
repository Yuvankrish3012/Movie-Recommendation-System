# Movie-Recommendation-System

This project recommends movies based on their content such as genres, keywords, cast, and crew using **TF-IDF Vectorization** and **Cosine Similarity**. It features a user-friendly frontend built with Streamlit for interactive movie selection and recommendations.

---

## 📂 Dataset

- 📁 Dataset Used: [TMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Files:
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`

---

## ⚙️ Techniques Used

| Component       | Details                                |
|-----------------|-----------------------------------------|
| Vectorizer      | TF-IDF (max 5000 features, English stopwords) |
| Similarity      | Cosine Similarity on combined text fields |
| Features Used   | Overview, Genres, Keywords, Cast, Director |
| Recommendation  | Top 5 most similar movies to selected title |
| Frontend        | Streamlit UI                           |

---

## 📊 Visualizations

### 🔹 Top Movie Keywords

![image](https://github.com/user-attachments/assets/57b6a054-0765-4e5c-a3c8-39fa3277d036)


### 🔹 Top Movie Genres

![image](https://github.com/user-attachments/assets/2aeb7c1e-c3ce-45ad-8a49-b39bf84ce2bb)


### 🔹 Movie Releases Per Decade

![image](https://github.com/user-attachments/assets/cdf8f2da-8282-4dca-bd64-2c6047dc1de6)


---

## 🧪 Evaluation Metrics (Simulated)

These metrics are simulated to show evaluation format. Recommender systems are best evaluated using ranking-based metrics (e.g., Precision@K).

✅ Evaluation Metrics (Simulated)
Accuracy : 0.80
Precision : 1.00
Recall : 0.67
F1 Score : 0.80

yaml
Copy
Edit

---

## 🎥 Sample Recommendation Output

Example input:
```python
recommend("The Dark Knight")
📋 Output:

pgsql
Copy
Edit
Top 5 movies similar to 'The Dark Knight':
The Dark Knight Rises
Batman Begins
Batman Returns
Batman Forever
Batman v Superman: Dawn of Justice

💻 Streamlit Frontend

✨ Features:
Dropdown menu to select any movie

Button to get instant recommendations

Clean output listing 5 similar movies

📷 UI Screenshot

![image](https://github.com/user-attachments/assets/4cec2811-23ff-4c39-9627-91d59341c087)


🚀 Run the App Locally
1. Install Requirements
bash
Copy
Edit
pip install streamlit scikit-learn pandas numpy
2. Launch the App
bash
Copy
Edit
streamlit run "D:/ML PROJECTS/Movie Recommendation System/movie_recommender_app.py"
📁 Project Structure
sql
Copy
Edit
📂 Movie Recommendation System
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── movie_titles.pkl
├── movie_similarity.pkl
├── movie_recommender_app.py
├── top_keywords.png
├── top_genres.png
├── movies_per_decade.png
├── README.md
🚧 To-Do / Future Work
 Add poster thumbnails using TMDB API

 Add genre filters

 Integrate collaborative filtering (optional)

 Deploy to Streamlit Cloud

👨‍💻 Developed By
V. Yuvan Krishnan
Student, SRM Institute of Science & Technology

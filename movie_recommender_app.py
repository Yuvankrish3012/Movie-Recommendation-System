import streamlit as st
import pickle
import numpy as np

# Load the model and similarity matrix using full path
movies = pickle.load(open("D:/ML PROJECTS/Movie Recommendation System/movie_titles.pkl", "rb"))
similarity = pickle.load(open("D:/ML PROJECTS/Movie Recommendation System/movie_similarity.pkl", "rb"))

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = list(enumerate(similarity[index]))
    movie_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    return [movies.iloc[i[0]].title for i in movie_list]

# Streamlit UI
st.set_page_config(page_title="🎬 Movie Recommendation App", layout="centered")
st.title("🎬 Movie Recommender System")
st.write("Select a movie and get 5 similar movie recommendations.")

# Dropdown
selected_movie_name = st.selectbox("Choose a movie", movies['title'].values)

# Button
if st.button("Show Recommendations"):
    recommendations = recommend(selected_movie_name)
    st.subheader("✅ Recommended Movies:")
    for title in recommendations:
        st.write(f"• {title}")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
st.title("Netflix Data Analysis")
df = pd.read_csv('netflix_titles.csv')

# Data Cleaning
st.subheader("Data Overview")
st.write(df.info())

df.fillna("Unknown", inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
wrong_ratings = ['74 min', '84 min', '66 min']
df.loc[df['rating'].isin(wrong_ratings), 'rating'] = "Unknown"

type_counts = df["type"].value_counts()
st.subheader("Movies vs. TV Shows")
st.bar_chart(type_counts)

# Top 10 Genres
genres = df["listed_in"].str.split(", ").explode().value_counts().head(10)
st.subheader("Top 10 Genres")
st.bar_chart(genres)

# Release Year Distribution
st.subheader("Release Trend Over Years")
fig, ax = plt.subplots()
sns.histplot(df["release_year"], bins=15, kde=True, color="red", ax=ax)
st.pyplot(fig)

# Top 10 Countries Producing Content
top_countries = df["country"].value_counts().head(10)
st.subheader("Top 10 Countries Producing Content")
st.bar_chart(top_countries)

# Content Ratings
top_ratings = df["rating"].value_counts()
st.subheader("Content Ratings Distribution")
st.bar_chart(top_ratings)

# Monthly Additions Trend
df['month_added'] = df['date_added'].dt.month_name()
monthly_counts = df['month_added'].value_counts()[["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]]
st.subheader("Monthly Additions Trend")
st.bar_chart(monthly_counts)

# Top 10 Directors
top_directors = df[df['director'] != "Unknown"]['director'].value_counts().head(10)
st.subheader("Top 10 Most Frequent Directors on Netflix")
st.bar_chart(top_directors)

# Top 10 Actors
top_actors = df[df['cast'] != "Unknown"]['cast'].str.split(", ").explode().value_counts().head(10)
st.subheader("Top 10 Actors with Most Appearances on Netflix")
st.bar_chart(top_actors)

# Movie Durations
df['duration_minutes'] = df['duration'].str.extract('(\d+)').astype(float)
st.subheader("Movie Durations")
fig, ax = plt.subplots()
sns.histplot(df[df['type'] == "Movie"]["duration_minutes"].dropna(), bins=30, kde=True, color="purple", ax=ax)
st.pyplot(fig)

# Longest & Shortest Movies
longest_movies = df[df['type'] == "Movie"].nlargest(5, 'duration_minutes')[['title', 'duration_minutes']]
st.subheader("Top 5 Longest Movies")
st.write(longest_movies)

shortest_movies = df[df['type'] == "Movie"].nsmallest(5, 'duration_minutes')[['title', 'duration_minutes']]
st.subheader("Top 5 Shortest Movies")
st.write(shortest_movies)

# Longest TV Shows
tv_shows = df[df['type'] == "TV Show"]
tv_shows['season_count'] = tv_shows['duration'].str.extract('(\d+)').astype(float)
longest_tv_shows = tv_shows.nlargest(10, 'season_count')[['title', 'season_count']]
st.subheader("Top 10 Longest TV Shows")
st.write(longest_tv_shows)

# Movies vs. TV Shows in Top 10 Countries
st.subheader("Movies vs. TV Shows in Top 10 Countries")
fig, ax = plt.subplots()
sns.countplot(y=df["country"], hue=df["type"], order=df["country"].value_counts().head(10).index, palette="coolwarm", ax=ax)
st.pyplot(fig)

# Distribution of Movie Durations
st.subheader("Distribution of Movie Durations")
fig, ax = plt.subplots()
sns.histplot(df[df['type'] == "Movie"]["duration_minutes"].dropna(), bins=30, kde=True, color="purple", ax=ax)
st.pyplot(fig)

# Top 10 Countries with Most TV Shows
st.subheader("Top 10 Countries with Most TV Shows")
tv_shows_by_country = df[(df['type'] == "TV Show") & (df['country'] != "Unknown")]['country'].value_counts().head(10)
st.bar_chart(tv_shows_by_country)

# Top 10 Countries with Most Movies
st.subheader("Top 10 Countries with Most Movies")
movies_by_country = df[(df['type'] == "Movie") & (df['country'] != "Unknown")]['country'].value_counts().head(10)
st.bar_chart(movies_by_country)

# Distribution of Content Ratings by Type
st.subheader("Distribution of Content Ratings by Type")
fig, ax = plt.subplots()
sns.countplot(y=df['rating'], hue=df['type'], order=df['rating'].value_counts().index, palette="coolwarm", ax=ax)
st.pyplot(fig)

# Top 10 Longest TV Shows
st.subheader("Top 10 Longest TV Shows by Number of Seasons")
longest_tv_shows = tv_shows.nlargest(10, 'season_count')[['title', 'season_count']]
st.write(longest_tv_shows)

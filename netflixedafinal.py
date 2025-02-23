import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Netflix EDA Dashboard")

# Load Data
df = pd.read_csv('netflix_titles.csv')  #loads the file
df.fillna("Unknown", inplace=True)  #fills the blank space with unknown
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')  #changes the date into number values

# Movies vs TV Shows
st.subheader("Movies vs. TV Shows")
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.countplot(x=df["type"], palette="magma", ax=ax) #this places the graph with the color palette on the given axes
ax.set_title("Movies vs. TV Shows")  #sets the title
st.pyplot(fig) #to display the graph

# Top 10 Genres
st.subheader("Top 10 Genres")
genres = df["listed_in"].str.split(", ").explode().value_counts().head(10)
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.barplot(y=genres.index, x=genres.values, palette="viridis", ax=ax)  #this places the graph with the color palette on the given axes
ax.set_title("Top 10 Genres")  #sets the title
st.pyplot(fig) #to display the graph

# Release Trend Over Years
st.subheader("Release Trend Over Years")
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.histplot(df["release_year"], bins=15, kde=True, color="red", ax=ax)  #this places the graph with the color palette on the given axes
ax.set_title("Release Trend Over Years")  #sets the title
st.pyplot(fig) #to display the graph

# Top 10 Countries Producing Content
st.subheader("Top 10 Countries Producing Content")
countries = df["country"].value_counts().head(10)
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.barplot(y=countries.index, x=countries.values, palette="plasma", ax=ax)  #this places the graph with the color palette on the given axes
ax.set_title("Top 10 Countries Producing Content")  #sets the title
st.pyplot(fig)  #to display the graph

# Content Ratings Distribution
st.subheader("Content Ratings Distribution")
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.barplot(y=df['rating'].value_counts().index, x=df['rating'].value_counts().values, palette="magma", ax=ax)
ax.set_title("Content Ratings Distribution")  #sets the title
st.pyplot(fig)  #to display the graph

# Monthly Additions Trend
st.subheader("Monthly Additions Trend")
df['month_added'] = df['date_added'].dt.month_name()
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.countplot(x=df['month_added'], order=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], palette="coolwarm", ax=ax)  #this places the graph with the color palette on the given axes
ax.set_title("Monthly Additions Trend")  #sets the title
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)  #to display the graph

# Top 10 Most Frequent Directors
st.subheader("Top 10 Most Frequent Directors")
top_directors = df[df['director'] != "Unknown"]['director'].value_counts().head(10)
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.barplot(y=top_directors.index, x=top_directors.values, palette="rocket", ax=ax)
ax.set_title("Top 10 Most Frequent Directors")  #sets the title
st.pyplot(fig)  #to display the graph

# Movies vs TV Shows in Top 10 Countries
st.subheader("Movies vs TV Shows in Top 10 Countries")
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.countplot(y=df["country"], hue=df["type"], order=df["country"].value_counts().head(10).index, palette="coolwarm", ax=ax)
ax.set_title("Movies vs TV Shows in Top 10 Countries")  #sets the title
st.pyplot(fig)  #to display the graph

# Distribution of Movie Durations
st.subheader("Distribution of Movie Durations")
df['duration_minutes'] = df['duration'].str.extract('(\d+)').astype(float)
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.histplot(df[df['type'] == "Movie"]['duration_minutes'].dropna(), bins=30, kde=True, color="purple", ax=ax)
ax.set_title("Distribution of Movie Durations")  #sets the title
st.pyplot(fig)  #to display the graph

# Top 5 Longest and Shortest Movies on Netflix
st.subheader("Top 5 Longest Movies on Netflix")
longest_movies = df[df['type'] == "Movie"].nlargest(5, 'duration_minutes')
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.barplot(y=longest_movies['title'], x=longest_movies['duration_minutes'], palette="Reds_r", ax=ax)  #this places the graph with the color palette on the given axes
ax.set_title("Top 5 Longest Movies")  #sets the title
st.pyplot(fig)  #to display the graph

st.subheader("Top 5 Shortest Movies on Netflix")
shortest_movies = df[df['type'] == "Movie"].nsmallest(5, 'duration_minutes')
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.barplot(y=shortest_movies['title'], x=shortest_movies['duration_minutes'], palette="Blues_r", ax=ax)  #this places the graph with the color palette on the given axes
ax.set_title("Top 5 Shortest Movies")  #sets the title
st.pyplot(fig)  #to display the graph

# Most Common Number of Seasons in TV Shows
st.subheader("Most Common Number of Seasons in TV Shows")
tv_shows = df[df['type'] == "TV Show"]
tv_shows['season_count'] = tv_shows['duration'].str.extract('(\d+)').astype(float)
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.histplot(tv_shows['season_count'].dropna(), bins=15, kde=True, color="purple", ax=ax)
ax.set_title("Most Common Number of Seasons")  #sets the title
st.pyplot(fig)  #to display the graph

# Top 10 Actors with Most Appearances
st.subheader("Top 10 Actors with Most Appearances")
top_celebrities = df[df['cast'] != "Unknown"]['cast'].str.split(", ").explode().value_counts().head(10)
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.barplot(y=top_celebrities.index, x=top_celebrities.values, palette="rocket", ax=ax)  #this places the graph with the color palette on the given axes
ax.set_title("Top 10 Actors on Netflix")  #sets the title
st.pyplot(fig)  #to display the graph

# TV Shows by Country
st.subheader("Top 10 Countries with Most TV Shows (Excluding Unknown)")
tv_shows_by_country = df[(df['type'] == "TV Show") & (df['country'] != "Unknown")]['country'].value_counts().head(10)
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.barplot(y=tv_shows_by_country.index, x=tv_shows_by_country.values, palette="viridis", ax=ax)  #this places the graph with the color palette on the given axes
ax.set_title("Top 10 Countries with Most TV Shows")  #sets the title
st.pyplot(fig)  #to display the graph

# Movies by Country
st.subheader("Top 10 Countries with the Most Movies on Netflix (Excluding Unknown)")
movies_by_country = df[(df['type'] == "Movie") & (df['country'] != "Unknown")]['country'].value_counts().head(10)
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.barplot(y=movies_by_country.index, x=movies_by_country.values, palette="viridis", ax=ax)  #this places the graph with the color palette on the given axes
ax.set_title("Top 10 Countries with the Most Movies")  #sets the title
st.pyplot(fig)  #to display the graph

# Content Ratings by Type
st.subheader("Distribution of Content Ratings by Type (Movie vs. TV Show)")
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.countplot(y=df['rating'], hue=df['type'], order=df['rating'].value_counts().index, palette="coolwarm", ax=ax)
ax.set_title("Content Ratings by Type")  #sets the title
st.pyplot(fig)  #to display the graph

# Top 10 Longest TV Shows
st.subheader("Top 10 Longest TV Shows")
longest_tv_shows = tv_shows.nlargest(10, 'season_count')
fig, ax = plt.subplots()  #creates a new figure and a set of subplots
sns.barplot(y=longest_tv_shows['title'], x=longest_tv_shows['season_count'], palette="Reds_r", ax=ax)  #this places the graph with the color palette on the given axes
ax.set_title("Top 10 Longest TV Shows")  #sets the title
st.pyplot(fig)  #to display the graph

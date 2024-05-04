import streamlit as st
import pandas as pd

# Function to read championship data from CSV file
def read_championship_data(championship_data):
    try:
        return pd.read_csv(championship_data)
    except FileNotFoundError:
        st.error(f"File '{championship_data}' not found.")
        return pd.DataFrame()

# Function to read player data from CSV file
def read_player_data(player_data):
    try:
        return pd.read_csv(player_data)
    except FileNotFoundError:
        st.error(f"File '{player_data}' not found.")
        return None

# Function to view championship details
def view_championship_details(sport, category, year, cricket_data, basketball_data):
    data = cricket_data if sport == "Cricket" else basketball_data
    if not data.empty and year in data['Year'].values:
        details = data[(data['Year'] == year) & (data['Category'] == category)]
        if not details.empty:
            winner = details.iloc[0]['Winner']
            runner_up = details.iloc[0]['Runner-up']
            st.info(f"Winner: {winner}")
            st.info(f"Runner-up: {runner_up}")
        else:
            st.info(f"No championship details found for {category} {sport} in {year}.")
    else:
        st.info(f"No championship details found for {category} {sport} in {year}.")

# Function to search player details
def search_player(player_name, player_data):
    player_details = ""
    if player_data is not None:
        for index, row in player_data.iterrows():
            if row['Player Name'] == player_name:
                player_details += f"Player details for {player_name}:\n"
                for column, value in row.items():
                    player_details += f"{column.lower()}: {value}\n"
                break
        if not player_details:
            player_details = f"Player '{player_name}' not found."
    else:
        player_details = "Player data not loaded."
    for line in player_details.split('\n'):
        st.info(line)

# Main function
def main():
    # Load data from files
    cricket_data = read_championship_data("cricket_championship_data.csv")
    basketball_data = read_championship_data("basketball_championship_data.csv")
    player_data = read_player_data("player_data.csv")

    # Title
    # Title and Image
    st.image("data:image/png;base64,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", use_column_width=200)
    st.title("Championship History Tracker")

    # Sidebar
    st.sidebar.subheader("Options")
    sport = st.sidebar.selectbox("Select Sport:", ("Cricket", "Basketball"), index=0)
    category = st.sidebar.selectbox("Select Category:", ("T20", "IPL", "Test", "ODI", "NBA Finals", "SABA"), index=0)
    year = st.sidebar.number_input("Enter Year:", min_value=2000, max_value=2025, value=2020)

    # Championship details
    view_championship_details(sport, category, year, cricket_data, basketball_data)

    # Player search
    st.sidebar.subheader("Search Player")
    player_name = st.sidebar.text_input("Enter Player Name:")
    search_button = st.sidebar.button("Search")
    if search_button:
        search_player(player_name, player_data)

if __name__ == "__main__":
    main()
# spotify_program.py
# Anas Chowdhury
# A terminal-based application to process and plot data based on given user input and provided data values.
#

import numpy as np
import matplotlib.pyplot as plt

# ******************************************************************************************************
column_names = ['title', 'artist(s)', 'release', 'num_of_streams', 'bpm', 'key', 'mode', 'danceability', 'valence', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'speechiness']
data = np.genfromtxt('spotify_data.csv', delimiter = ',', skip_header = True, dtype = str)
# ******************************************************************************************************


# ******************************************************************************************************
# DEFINE BONUS CLASS
class Song:
    """A class used to create a Song object.

        Attributes:
            title (str): String that represents the song's title
            artist (str): String that represents the song's artist
            key (str): String that represents the song's key
            mode (str): String that represents the song's mode
            release (float): Float that represents the song's release year
            num_of_streams (float): Float that represents the song's number of streams
            bpm (float): Float that represents the song's beats per minute
            danceability (float): Float that represents the song's danceability
            valence (float): Float that represents the song's valence
            energy (float): Float that represents the song's energy
            acousticness (float): Float that represents the song's acousticness
            instrumentalness (float): Float that represents the song's instrumentalness
            liveness (float): Float that represents the song's liveness
            speechiness (float): Float that represents the song's speechiness
            percentages (list): List containing all the values for danceability through to speechiness
            
    """
    def __init__(self, song_array):
        """Constructor method that sets up the initial state of the new instance.

        Parameters:
        self -- automatically references the instance being created
        song_array -- The row of the data array that corresponds to the bonus row number entered by the user

        Return Value:
        There is no return value. This is a void function and so the value returned is None.

        """
        # Save the title, artist, key, and mode column of the row, song_array as Strings
        self.title = song_array[0]      # Save the title from the 1st column
        self.artist = song_array[1]     # Save the artist from the 2nd column
        self.key = song_array[5]        # Save the key from the 6th column
        self.mode = song_array[6]       # Save the mode from the 7th column

        # Save the remaining ten features as float values
        self.release = float(song_array[2])                 # Save the release from the 3rd column
        self.num_of_streams = float(song_array[3])          # Save the num_of_streams from the 4th column
        self.bpm = float(song_array[4])                     # Save the bpm from the 5th column
        self.danceability = float(song_array[7])            # Save the danceability from the 8th column
        self.valence = float(song_array[8])                 # Save the valence from the 9th column
        self.energy = float(song_array[9])                  # Save the energy from the 10th column
        self.acousticness = float(song_array[10])           # Save the acousticness from the 11th column
        self.instrumentalness = float(song_array[11])       # Save the instrumentalness from the 12th column
        self.liveness = float(song_array[12])               # Save the liveness from the 13th column
        self.speechiness = float(song_array[13])            # Save the speechiness from the 14th column

        # Define the list containing all the values for danceability through to speechiness
        self.percentages = [self.danceability, self.valence, self.energy, self.acousticness, self.instrumentalness, self.liveness, self.speechiness]
    
    def plot_graph(self):
        """Instance method that plots the bar graph for the chosen song.

        Parameters:
        self -- automatically references the instance

        Return Value:
        There is no return value. This is a void function and so the value returned is None.

        """
        features = column_names[7:14] # Store a copy of the list, column_names, from element at index locations of 7 to 14 (not including 14) in features

        # Create and print plot
        plt.figure(figsize=[12,7])                  # Create a new 12 x 7 inch figure for the plot to appear in
        plt.bar(features, self.percentages)         # Create a bar graph where features is on the x-axis and self.percentages is on the y-axis
        plt.yticks(range(0, 101, 10))               # Make the y-axis start at 0 and end at 100, incrementing by a value of 10 along the axis
        plt.xlabel('Feature')                       # Make the label for the x-axis "Feature"
        plt.ylabel('Percentage')                    # Make the label for the y-axis "Percentage"
        plt.title(f'Song Stats for {self.title}')   # Make the title for the plot "Song Stats for" followed by the title of the song
        plt.savefig('bonus_graph')                  # Save the figure in the current working directory with the filename "bonus_graph.png"
        plt.show()                                  # Display the figure and all the objects the figure contains


# ******************************************************************************************************
# DEFINE FUNCTIONS HERE

def feature_stats(input_value):
    """Calculates the highest value, lowest value, and mean value for the desired song feature. This is done by 
    converting data values in a specified column of the data array into a new array, and then analyzing that array 
    to find the highest, lowest, and mean values.

    Parameter:
    input_value -- int representing the menu input option entered by the user. It represents the column of the data array from which the song feature data is to be analyzed.

    Return Value:
    highest_value_index -- int representing the index of the maximum value in the one-dimensional array, converted_data.

    """
    converted_data = np.array([row[input_value] for row in data], dtype='float') # List comprehension that converts data values in the column specified by input_value into a one-dimensional array
    highest_value_index = np.argmax(converted_data)         # Use the NumPy function argmax() to find the index of the max value in converted_data
    
    print(f'Highest value: {int(max(converted_data))}')     # Output the highest value of the desired song feature to the screen
    print(f'Lowest value: {int(min(converted_data))}')      # Output the lowest value of the desired song feature to the screen
    print(f'Mean value: {int(np.mean(converted_data))}')    # Output the mean value of the desired song feature to the screen

    return highest_value_index      # Return the value of highest_value_index

    

def age_stats(input_value):
    """Calculates the total span of release years in the data. It then prints the artist, key, and mode of the 
    oldest song in the data.

    Parameter:
    input_value -- int representing the menu input option entered by the user, which is 2 in this case. It represents the column of the data array from which the song feature data is to be analyzed.

    Return Value:
    There is no return value. This is a void function and so the value returned is None.

    """
    years = np.array([row[input_value] for row in data], dtype='int')       # List comprehension that converts data values in the column specified by input_value into a one-dimensional array
    year_span = max(years) - min(years)                                     # Calculate the difference between the maximum and minimum values in the years array. This represents the total span of release years.

    oldest_song_row = np.argmin(years)               # Use the NumPy function argmin() to find the index of the minimum value in the years array
    oldest_song_artist = data[oldest_song_row, 1]    # Stores the artist of the oldest song, which is located in the second column (index 1) of the row with the oldest song
    oldest_song_key = data[oldest_song_row, 5]       # Stores the key of the oldest song, which is located in the sixth column (index 5) of the row with the oldest song
    oldest_song_mode = data[oldest_song_row, 6]      # Stores the mode of the oldest song, which is located in the seventh column (index 6) of the row with the oldest song

    print(f'Span of years: {year_span}')                                            # Print out the total span of release years in the data
    print(f'Artist of oldest song: {oldest_song_artist}')                           # Print out the artist of the oldest song
    print(f'Key and mode of oldest song: {oldest_song_key} {oldest_song_mode}')     # Print out the key and mode of the oldest song


# ******************************************************************************************************
# DEFINE MAIN CODE

def main():
    print("Spotify Statistics\n")          # Print out the course name followed by "Spotify Statistics"
    print("Song analysis options: ")                # Print out the menu of song analysis options
    for menu, option in enumerate(column_names):    # The enumerate() function is used to access the index location and string for each element in the list, column_names
        print(menu, option)                         # Print out the menu number as well as the song analysis option
    print("Choose -1 to end the program.")          # Print out the message that entering -1 will end the program

    # Continue main code below
    user_choice = 0                                         # Set user_choice to 0. user_choice will store the menu uption entered by the user
    
    while user_choice != -1:                                # while loop that will run as long as user_choice is not equal to -1, which would only occur when the user wants to end the program    
        if user_choice < 0 or user_choice > 13:             # Check to see if user_choice is less than 0 or greater than 13 (The code in this if block would execute if the user entered an invalid menu option)
            print('You must enter a valid menu option.')    # Print out to the user that they need to enter a valid menu option
        
        elif user_choice == 2:                              # Check to see if user_choice is equal to 2
            age_stats(user_choice)                          # Call the function age_stats, passing in user_choice as an argument.
        
        elif user_choice != 0 and user_choice != 1 and user_choice != 5 and user_choice != 6:           # Check to see if user_choice is not equal to 0, 1, 5, and 6 (Nothing should happen if the user enters 0, 1, 5, or 6)    
            top_song_row = feature_stats(user_choice)                                                   # Call the function feature_stats, passing in user_choice as an argument. The index value returned by feature_stats (highest_value_index) is stored in top_song_row 
            print(f'Top song in selected feature: {data[top_song_row, 0]}')                             # Print out the top song in the selected feature, which is located within the data array, in the first column (index 0) of the row specified by top_song_row
        
        user_choice = int(input('\nPlease enter a song feature to analyze: '))                          # Prompt the user to enter a song feature to analyze


    # Create and print danceability vs. bpm plot
    danceability = np.array([row[7] for row in data], dtype='int')      # List comprehension that converts data values in the 8th column (index 7) into a one-dimensional array
    bpm = np.array([row[4] for row in data], dtype='int')               # List comprehension that converts data values in the 5th column (index 4) into a one-dimensional array

    plt.figure(figsize=[12,7]) # Create a new 12 x 7 inch figure for the plot to appear in
    # Create a scatter plot, which shows pairs of x and y coordinates, where bpm is on the x-axis and danceability is on the y-axis.
    # The color of the points are blue, and the data is labeled "Song Stats"
    plt.scatter(bpm, danceability, color='b', label='Song Stats')
    plt.title('Danceability vs. Beats per Minute')          # Make the title of the graph "Danceability vs. Beats per Minute"
    plt.xlabel('BPM')                                       # Make the label for the x-axis "BPM"
    plt.ylabel('Danceability')                              # Make the label for the y-axis "Danceability"
    plt.legend()                                            # Make the legend for the plot. The location of the legend is 'best' (default value), which is where there is the least plot overlap
    plt.savefig('danceability_vs_bpm.png')                  # Save the figure in the current working directory with the filename "danceability_vs_bpm.png"

    # Create bonus Song object (optional)
    bonus_row_number = int(input('Bonus - Enter any row number: '))     # Prompt the user for a bonus row number
    bonus_row = data[bonus_row_number]                                  # Stores the specified row from the data array in bonus_row
    bonus_song = Song(bonus_row)                                        # Create an instance of the Song class called bonus_song, passing in bonus_row as an argument
    
    # Create and print bonus plot (optional)
    bonus_song.plot_graph()                     # Calls the instance method, plot_graph() to print the bonus plot


if __name__ == '__main__':
    main()


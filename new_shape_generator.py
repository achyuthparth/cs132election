import max_heap
import geopandas as gpd
import matplotlib.pyplot as plt

def generator(from_file, to_file):
    # getting test file
    al_shape = gpd.read_file(from_file)

    # creating geo data frame
    al_prez = gpd.GeoDataFrame()

    # create subset with only presidents and geometry
    al_prez = al_prez.set_geometry(al_shape["geometry"])
    add_columns = []
    for col in al_shape:
        if col[3:6] == "PRE":
            add_columns.append(col)

    # adding filtered columns with presidents
    for col in add_columns:
        al_prez[col] = al_shape[col]

    # finding the winners by row and saving as a separate column
    numeric_columns = al_prez.select_dtypes(include='number')  # Select only numeric columns
    max_indices = numeric_columns.idxmax(axis=1)  # Get the index of max value for each row
    al_prez["winners"] = max_indices

    # using heap to extract the maximum from each row
    win_count = []
    for index, row in al_prez.iterrows():
        numeric_values = al_prez.loc[index, numeric_columns.columns].tolist() # get the row of the numbers
        heap = max_heap.MaxHeap(20)
        for item in numeric_values:
            heap.insert(item)
        max_val = heap.extractMax()
        win_count.append(max_val)

    al_prez["win_count"] = win_count

    # setting the color depending on the winner of that particular row
    for i, winner in enumerate(al_prez["winners"]):
        if winner[6] == "R": color = "red"
        elif winner[6] == "D": color = "blue"
        elif winner[6] == "G": color = "green"
        elif winner[6] == "L": color = "yellow"
        else: color = "grey"
        
        al_prez.loc[i, "max_color"] = color

    gpd.GeoDataFrame.to_file(to_file)
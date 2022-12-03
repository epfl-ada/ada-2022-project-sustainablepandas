import pandas as pd
import time
import googlemaps
import os

input_file = "breweries.csv"
result_file = "result.csv"
folder_path = "./Data/RateBeer"
df = pd.read_csv(os.path.join(folder_path, input_file), delimiter=',')
df = df.rename(columns={"id": "brewery_id"})
df['latitude'] = "NA"
df['longitude'] = "NA"

# Read the txt file which contains the API key:
API_KEY = 'AIzaSyCeiFJl4at2Us5ibVnGmJw6CeeyzRNGxLc'
map_client = googlemaps.Client(API_KEY)

# Function to get the info of each brewery place:
def get_place_info(location_name):
    try:
        response = map_client.places(query=location_name)
        results = response.get('results')[0]
        return results

    except Exception as e:
        print(e)
        return None


def callback(dataframe, nb_iteration, save_on_iteration=10):
    if nb_iteration % save_on_iteration == 0:
        dataframe.to_csv(os.path.join(folder_path, result_file))

# Using google API, get the rating, the number of ratings, the latitude and longitude
# of each brewery, we wont run the code here because it takes a lot of time
# We created an excel with the results.

start = time.time()

for i, row in df[17311:].iterrows():
    print(i)
    if i % 1000 == 0:
        # do some stuff
        stop = time.time()
        duration = stop - start
        print(duration / 60)
    place_address = row["name"] + " " + row["location"]
    try:
        place_info = get_place_info(place_address)

        # If we want, we can get some other info from the google API.
        df.iloc[i, df.columns.get_loc("latitude")] = place_info['geometry']['location']['lat']
        df.iloc[i, df.columns.get_loc("longitude")] = place_info['geometry']['location']['lng']

        # For now, we focus on getting the longitude and lattitude.
    except (KeyError, NameError, TypeError):
        pass
    finally:
        callback(df, i)

df.to_csv(os.path.join(folder_path, result_file))

import os
import requests


class CSVDownloader:
    
    def download(self, url, path_to_download="data"):
        # create folder if it doesn't exist
        os.makedirs(path_to_download, exist_ok=True)

        # file name from URL
        file_name = url.split("/")[-1]
        print(file_name)
        file_path = os.path.join(path_to_download, file_name)
        print(file_path)

        # download file
        response = requests.get(url)

        if response.status_code == 200:
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"File downloaded successfully: {file_path}")
        else:
            print("Failed to download file")


# URL
titanic_dataset_github_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"

# create object
obj = CSVDownloader()

# call method
obj.download(titanic_dataset_github_url, path_to_download="data")
import glob
from dotenv import load_dotenv
import os
from ingest import ingest
import pathlib
load_dotenv()


env_file_path = ".env"

# Check if the file exists
if os.path.exists(env_file_path):
    # Open the file and read its contents
    with open(env_file_path, "r") as file:
        # Read all lines from the file
        env_contents = file.readlines()
        # Print each line
        for line in env_contents:
            print(line.strip())
else:
    print(f"The file '{env_file_path}' does not exist.")


# Examples of the vars from the .env file
#ROOT_FOLDER=/home/j/programming/work/October_data
#SCICAT_URL=https://mwet.lbl.gov/api/v3
#USERNAME=username
#INGEST_USER=username
#PASSWORD=password
#INGEST_SPEC=als_11012_igor OR als_11012_scattering OR als_11012_nexafs

ROOT_FOLDER = os.getenv("ROOT_FOLDER")
SCICAT_URL = os.getenv("SCICAT_URL")
USERNAME = os.getenv("USERNAME")
INGEST_USER = os.getenv("INGEST_USER")
PASSWORD = os.getenv("PASSWORD")
INGEST_SPEC = os.getenv("INGEST_SPEC")
DERIVED_FOLDER = os.getenv("DERIVED_FOLDER")

assert type(ROOT_FOLDER) == str and len(ROOT_FOLDER) != 0 
assert type(SCICAT_URL) == str and len(SCICAT_URL) != 0 
assert type(USERNAME) == str and len(USERNAME) != 0 
assert type(PASSWORD) == str and len(PASSWORD) != 0 
assert type(INGEST_USER) == str and len(INGEST_USER) != 0 
assert type(INGEST_SPEC) == str and len(INGEST_SPEC) != 0 

is_derived_folder = False

ROOT_FOLDER = pathlib.Path(ROOT_FOLDER)

pattern = None
ingestor_location = None
override_iterator = False
ingest_files_iter = []
if INGEST_SPEC == "als_nmr":
    pattern = f"{ROOT_FOLDER}/*.csv"
    ingestor_location = pathlib.Path(os.getcwd(), "als_nmr.py")
else:
    raise Exception("Environment variable 'INGEST_SPEC' is invalid.")

if override_iterator is False:
    ingest_files_iter = glob.iglob(pattern)

for ingest_file_str in ingest_files_iter:
    ingest_file_path = pathlib.Path(ingest_file_str)
    if ingest_file_path.exists():
        print(ingest_file_path)
        if is_derived_folder is False:
            ingest(ingestor_location, ingest_file_path, None,  INGEST_USER, SCICAT_URL, token=None, username=USERNAME, password=PASSWORD)
        else:
            ingest(ingestor_location, ingest_file_path, pathlib.Path(DERIVED_FOLDER), INGEST_USER, SCICAT_URL, token=None, username=USERNAME, password=PASSWORD)

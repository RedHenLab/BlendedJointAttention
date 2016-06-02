import glob     # Import glob to easily loop over files
import pympi    # Import pympi to work with elan files
import string   # Import string to get the punctuation data

# Define some variables for later use
corpus_root = 'Test_EAF/'
corpus_root1 = 'Result_files'
print glob.glob("Result_files/*")
output_file = '{}/annotation_with_timestamp.txt'.format(corpus_root1)

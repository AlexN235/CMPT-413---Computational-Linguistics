NOTE: This was a group project for a computational linguistics cource at SFU that I have reuploaded to github. I personal only written the code in the word2vec.py, yelp_data_extraction.py and cbow.ipynb files.


The goal of this project was to test and compare the effectiveness of word2vec:continuous bag of words model against the TF-IDF model on yelp reviews. 

data extraction - contain python code to extract, clean, crop the original dataset to only contain a star rating and the review. Also contain the first 100,000 reviews that were already cleaned and cropped using yelp_data.extraction.py.

main - contain the code for our models, the ipynb files to run them and data that could be used to run the code

To run, we used google colab:
 - TF-IDF model: import sentiment.ipynb to google colab and place tfidf.py and data.zip to google colab's local folders.

- word2vec:cbow model: import cbow.ipynb to google colab and place the word2vec and data.zip to google colab's local folders.

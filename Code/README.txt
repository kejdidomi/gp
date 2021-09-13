CLASSIFICATION OF LAPTOP COMPUTER MARKET USING FUZZY CLUSTERING: CASE STUDY ALBANIAN MARKET 

Inside this folder you will find 4 folders containing images and 15 files of different types.


DATASET_FINAL.xlsx is an Excel file containing the dataset used throughout the project.

DATASET_FINAL.csv is a coma separated values file created from DATASET_FINAL.xlsx file. It is used by view_heatmap.py, graph_with_2.py, 
graph_with_3.py, automated2.py, automated3.py, automatedR2.py, and automatedR3.py files.

raw.txt is a text file containing the source code of a webpage I used to extract information. It is used by extract.py to create saved.bin file and data.json file. These files are not of great importance and are merely here to show the method I used to gather data.

Files graph_with_2.py and graph_with_3.py ask the user to input a feature, compute a graph for that feature (with 2 and 3 clusters respectively) and save the image of the graph in images2 and images3 folders respectively. A problem with these files is that they compute a graph ata a time and full population of images2 and images3 folder would require a lot of time (38 graphs). To solve this, automated2.py and automated3.py were created: they dont show the graph but just save it in the corresponding folder. All graphs have descriptive names. Files automatedR2.py and automatedR3.py do a similar task as the previous 2 files respectively, but they build graphs that are more descriptive and contain extra elements better described on the paper.

As of now, all information is ready to be accessed in image folders. If we change the database then files with the prefix automatic are to be run. 
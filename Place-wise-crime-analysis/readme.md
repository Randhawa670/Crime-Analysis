# Collection of Places data and tagging crime with the place category
In this, you will find scripts folder containing scripts that can be used for getting data (place polygons) related to places from wikimapia, getting place polygons with 30m boundary areas included and associating crime reports with the place categories. Also, in this you will find data folder contaning raw data of places like parks, mosques, banl, city-gate, food, parkings, policestation, religion, trainstation and travel. 

Scripts listed in the folder are get_places_data_park.py, clean.py, make_boundaries.py, and associate_crime.py.  
Here is the description of the function of each script:

* get_places_data_park.py : 
  In this script, we request wikimapia for the information it have on all the tag places in lahore of the particular category such as parks and save this information in raw pickle format.
  
* clean.py :
 This script reads the raw information about the places and extract from it necessary attributes such as : title and shape polygon of every tag place of that category. After extracting, this scripts save these attributes in a formatted list in a pickle file. 
 
* make_boundaries.py :
 This script reads the shapes polygon attribute of the places and make a new polygon with 30m boundary areas for every place. Then this script save this new polygon with other attribute of that places in the same pickle file generated above.
 
* associate_crime.py :
 This script reads the formatted places and the reports. Then it tag each report with the place category using latlong information in report and polygon of formatted places. This results in a dataframe with new place category attribute associated with each report.
 



1) We read the json file and loaded into the script to convert all null values to None values 
2) For Q1, we used a infinite float as the base price to compare with other prices so that the cheapest prices stays at the end on the loop

3) FOr Q2, Pulled out the room name("the key for the value of cheapest price") inside the previous loop only and fetched the guests key value.

4) For Q3, again loaded json object within the "taxes" key to parse easily and added both price and sum of both taxes.

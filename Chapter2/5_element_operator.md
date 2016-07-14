#Element_operator
 - $exists
   - matches docs that hav specified field
   -> db.movieDetails.find({"tomato.meter":{$exists:true}}).count()
    362
   > db.movieDetails.find({"tomato.meter":{$exists:false}}).count()
   1933

 - $type
   - selects doc if field is of specified type
   -> db.moviesScratch.find({"_id":{$type:"string"}}).count()
    4



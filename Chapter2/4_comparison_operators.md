#comparison_operators
 - $gte : greater then equal to:
 -> db.movieDetails.find({runtime:{$gte:90}},{runtime:1,_id:0})
  { "runtime" : 175 }
  { "runtime" : 116 }
  { "runtime" : 106 }
  { "runtime" : 152 }

 -> db.movieDetails.find({runtime:{$gte:90,$lte:120}},{runtime:1,_id:0})
 -> db.movieDetails.find({"tomato.meter":{$gte:95},runtime:{$gt:180}},{runtime:1,title:1,_id:0})
  { "title" : "Lagaan: Once Upon a Time in India", "runtime" : 224 }
  { "title" : "The Godfather: Part II", "runtime" : 202 }
 -> db.movieDetails.find({rated:{$ne:"UNRATED"}}).count()
  2263
 -> db.movieDetails.find({rated:{$in:["G","PG"]}}).count()
  139

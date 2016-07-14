#regex_operator
 -> db.movieDetails.find({"awards.text":{$regex: /^Won\s.*/}}).count()
  83

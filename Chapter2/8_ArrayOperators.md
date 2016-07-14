#Array Operators
  > db.movieDetails.find({       genres:{$all: ["Comedy","Crime","Drama"]}       }).count()
   8

  - $size
  -> db.movieDetails.find({countries:{$size:1}}).count()
   1915

> db.movieDetails.find({boxOffice:{$elemMatch:{country:"UK",revenue:{$gt:15}}}})


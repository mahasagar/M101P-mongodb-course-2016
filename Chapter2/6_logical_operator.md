#logical_operator
 - $or operator:
 > db.movieDetails.find({$or:[{"tomato.meter":{$gt:95}},{"metacritic":{$gt:88}}]}).count()
 39
 - find({$or[{},{}]});

 - $and operator
 -> db.movieDetails.find({$and:[{"tomato.meter":{$gt:95}},{"metacritic":{$gt:88}}]}).count()
  12
 - above query is same as
  db.movieDetails.find({{"tomato.meter":{$gt:95}},{"metacritic":{$gt:88}}}).count()
 - db.movieDetails.find({$and:
            [{"metacritic":{$ne:null}},
             {"metacritic":{$exists:true}}
             ]
            });

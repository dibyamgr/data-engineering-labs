# Problem Statement

Project to determine the ratings of a movie using the movie-lens dataset.

## Tools and technologies to be used
1. Hadoop 
2. Hive

## UseCases
* List all the movies and the number of ratings
* List all the users and the number of ratings they have done for a movie
* List all the Movie IDs which have been rated (Movie Id with at least one user rating it)
* List all the Users who have rated the movies (Users who have rated at least one movie)
* List of all the User with the max ,min ,average ratings they have given against any movie
* List all the Movies with the max ,min, average ratings given by any user

## Submissions
1. [x] DDL commands used to create the tables
2. [x] Movie table needs to be partitioned on column genres.
3. [x] Rating table needs to be partitioned on userId and bucketed on rating column with number of buckets as 5
4. [x] DML commands to generate the results

## Schema
### Movie
`movieId: Int, title: String, genres: String`

### Rating
`userId: Int, movieId: Int, rating: Double, timestamp: String`



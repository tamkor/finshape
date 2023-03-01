# Book keeper

## To run the application
1. cd finshape
2. docker compose up

## Description of the webservices

auto generated (detailed) description with examples about the services can be found on:
- about the book keeper, where you can add and get books: http://localhost:8080/docs
- about the stats, where you can get statistics about the stored books: http://localhost:8081/docs

## to run docker containers manually one by one

  1. docker network create bk-net
  2. cd finshape/database
  3. docker run -p 5432:5432 --net bk-net --name db --rm -it $(docker build -q .)
  4. cd finshape/stats
  5. docker run -p 8081:8081 --net bk-net --name stats --rm -it $(docker build -q .)
  6. cd finshape/book_keeper
  7. docker run -p 8080:8080 --net bk-net --name book-keeper --rm -it $(docker build -q .)

## to run the webservices without docker
- stats
  - open the stats folder in your favourite editor
  - set the following environmental variables:
    - DATABASE_URL=postgresql://postgres:postgrespw@localhost:5432/mydb
    - STATSHOST=localhost
    - STATSPORT=8081
- book_keeper
  - open the book_keeper folder in your favourite editor
  - set the following environmental variables:
    - BKHOST=0.0.0.0
    - BKPORT=8080
    - DATABASE_URL=postgresql://postgres:postgrespw@localhost:5432/mydb
    - STATS_URL=http://localhost:8081;
    - STATSHOST=localhost;
    - STATSPORT=8081
- books_keeper service will require stats service for handling the PUT and POST requests (for the stats update notification)
- both book_keeper and stats will require the database, you can start that from another command line with:
  - cd database
  - docker run -p 5432:5432 --name db --rm -it $(docker build -q .)
 

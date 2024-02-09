# start a docker container with a postgres database for development

docker run \
    --name srda-test \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=srdatest \
    -p 5432:5432 \
    -d \
    pgvector/pgvector:pg16
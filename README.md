dvc init
dvc repro
dvc dag
dvc metrics show

docker build -t razamehar/telcocustomerchurnapp:latest .
docker run -d -p 8080:8080 razamehar/telcocustomerchurnapp:latest

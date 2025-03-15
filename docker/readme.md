docker build -f alp.Dockerfile -t alpine-linux .

docker run -it --rm -p 5900:5900 alpine-linux



docker build -f Dockerfile -t ubuntu-linux .

docker run -it --rm -p 5900:5900 ubuntu-linux

docker compose up --build -d
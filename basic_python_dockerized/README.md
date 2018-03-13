to build the basic image, I run: docker build -t friendlyhello .

-t just names the image to something useful.

docker image ls - will show the image i created.  It's not running yet though.

to run the app, I can do: docker run -p 4000:80 friendlyhello

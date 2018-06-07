CC = gcc
CPP = g++

FLAGS = -lm -pthread -O3 -march=native -Wall -funroll-loops -Wno-unused-result

all: metapath2vec distance

metapath2vec : metapath2vec.cpp
	$(CPP) metapath2vec.cpp -o metapath2vec $(FLAGS)

distance : distance.c
	$(CC) distance.c -o distance $(FLAGS)

clean:
	rm -rf metapath2vec distance

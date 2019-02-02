CC = g++
CCFLAGS = -o main.exe main.cpp cpp-base64/base64.cpp fractal.cpp -O2

ifeq ($(OS),Windows_NT)
	CCFLAGS += -lgdi32
else
	CCFLAGS += -L/usr/X11R6/lib -lm -lpthread -lX11
endif

build:
	$(CC) $(CCFLAGS)
clean:
	rm -f *.exe
	rm -f *.txt
	rm -f *.jpg
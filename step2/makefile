CC = g++
CCFLAGS = -o main.exe main.cpp cpp-base64/base64.cpp pattern.cpp -O2

ifeq ($(OS),Windows_NT)
	CCFLAGS += -lgdi32
else
	UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Linux)
        CCFLAGS += -L/usr/X11R6/lib -lm -lpthread -lX11
    endif
    ifeq ($(UNAME_S),Darwin)
        CCFLAGS += -lm -lpthread -I/usr/X11R6/include -L/usr/X11R6/lib -lm -lpthread -lX11
    endif
endif

debug:
	$(CC) $(CCFLAGS) -D DEBUG
build:
	$(CC) $(CCFLAGS)
clean:
	rm -f *.exe
	rm -f *.txt
	rm -f *.jpg
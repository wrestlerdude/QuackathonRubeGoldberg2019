# QuackathonRubeGoldberg2019
An utterly useless, but stupidly complex programatically made Rube Goldberg machine for the 2019 Quackathon.

## Build:
### Calculator, dotgame, tumblr, qr
All laravel projects. Just use `php artisan serve` from the directories

### Step 2: 
Requires GCC. Works on Windows + Linux + MacOS. If on MacOS make sure to have X11 installed, https://www.xquartz.org , although the graphical output won't work only the .txt.
<br />Get the required libraries by running
```
git submodule update --init --recursive
``` 
```
cd step2
```
```
make build
```
```
./main.exe
```

### Step 3:
Requires Node.js dependencies to be installed first
```
npm install --save express pug body-parser js-base64 request
```

Uses Bootstrap 4.2.1 and jQuery 3.3.1
```
yarn add bootstrap jquery
```

Run using
```
npm start
```

### Step 6:
Requires Python 3. That's about it.<br />
Just run 
```
python3 start.py
```
and enjoy the fireworks


#### order:
tumblr<br />
(Step X)shebang<br />
dot game<br />
step2<br />
cat facts<br />
VR<br />
step6<br />
QR<br />
(Step X)blockchain<br />
calculator<br />
 

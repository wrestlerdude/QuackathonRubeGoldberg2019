# QuackathonRubeGoldberg2019
An utterly useless, but stupidly complex programatically made Rube Goldberg machine for the 2019 Quackathon.

## Build:
### Calculator, dotgame, tumblr, qr
All laravel projects. Just use `php artisan serve` from the directories

### Step 2: 
Requires GCC. Works on Windows + Linux + MacOS. If on MacOS make sure to have X11 installed, [https://www.xquartz.org/)] , although the graphical output won't work only the .txt.
<br />Once cloned make sure to run 
`git submodule update --init --recursive` to get the appropiate libraries.
<br />Then run<br />
`cd step2`<br />
`make build`<br />
`./main.exe`

### Step 3:
Requires Node.js dependencies to be installed first
```
npm install --save express pug body-parser js-base64
```

Uses Bootstrap 4.2.1 and jQuery 3.3.1
```
yarn add bootstrap jquery
```

Run using
```
npm start
```
or
```
nodemon
```

### Step 6:
Requires Python 3. That's about it.<br />
Just run 'python3 start.py' and enjoy the fireworks


#### order:
tumblr
shebang
dot game
picture
cat facts
VR
text adventure
QR
blockchain
calculator
 

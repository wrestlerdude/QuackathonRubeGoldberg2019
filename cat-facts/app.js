const express = require('express');
const path = require('path');
const base64 = require('js-base64').Base64;
const bodyParser = require('body-parser');
const request = require('request');

const app = express();

// Parse inputs sent from web form
app.use(bodyParser.urlencoded({ extended: false }));

// Set public folder
app.use(express.static(path.join(__dirname, 'public')));

// Set the view engine to Pug
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

var decoded, encoded;
var facts = [{ fact:
    "When a cats rubs up against you, the cat is marking you with it's scent claiming ownership.",
   length: 91 }];
var passwd = "";

app.get('/', (req, res) => {
    res.render('index', {
        title: 'Cat Facts',
    });
    
});
app.get('/cat-fact', (req, res) => {
    request('https://catfact.ninja/facts?limit=1', { json: true }, (err, res, body) => {
        if (err) {
            console.log(err);
        }
        facts = body.data;
    });
    passwd = generatePass(10);
    res.render('cat-fact', {
        facts: facts,
        passwd: passwd
    });
});
// get method for encode page
app.get('/encode', (req, res) => {
    res.render('encode', {
        title: 'Encoded String to Better Encoded String',
        encoded: '',
        correct: null

    });
    encoded = "";
});

// post method for encode page
app.post('/encode', (req, res) => {

    decoded = base64.decode(base64.decode(req.body.encoded));
    console.log(decoded);
    encoded = base64.encode(rot13(decoded));

    res.render('encode', {
        title: 'Encoded String to Better Encoded String',
        encoded: encoded,
        correct: passwd === req.body.password
    });
});

app.listen(1337, () => {
    console.log('Server started on port 1337...');
});

function generatePass(length) {
    var charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var output = '';
    for(var i = 0; i < length; i++) {
        output += charset[Math.floor(Math.random()*charset.length)];
    }
    return output;
}

function rot13(str) {
    var input     = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    var output    = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm';
    var index     = x => input.indexOf(x);
    var translate = x => index(x) > -1 ? output[index(x)] : x;
    return str.split('').map(translate).join('');
}
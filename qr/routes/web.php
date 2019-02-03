<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::post('/qr', function(\Illuminate\Http\Request $request) {
    $raw = $request->message;

    $base32 = new Tuupola\Base32;

    $decoded = base64_decode($base32->decode(base64_decode($raw)));

    $message = $base32->encode(strrev($decoded));

    return view('qr', compact('message'));
});

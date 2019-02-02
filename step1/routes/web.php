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

Route::post('/game', function(\Illuminate\Http\Request $request) {

    $decoded = base64_decode(base64_decode($request->message));

    $reversed = strrev($decoded);
    $message = base64_encode($reversed);

    return view('game', compact('message'));
});

Route::get('/test', function () {
    $message = "Test";
    return view('game', compact('message'));
});


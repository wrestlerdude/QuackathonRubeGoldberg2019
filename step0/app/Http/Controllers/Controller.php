<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Support\Facades\Request;
use Tumblr\API\Client;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;

    public function submit(\Illuminate\Http\Request $request)
    {

        $message = $request->message;

        $reversed = strrev($message);

        $client = new Client(
            env("TUMBLR_CONSUMER"),
            env("TUMBLR_SECRET"),
            env("TUMBLR_TOKEN"),
            env("TUMBLR_TOKEN_SECRET")
        );

// Make the request
        //dd($client->getUserInfo());

        $post = [
            "type" => "text",
            "title" => base64_encode($reversed),
        ];

        $client->createPost(env("TUMBLR_URL"), $post);

        return view("success");


    }
}

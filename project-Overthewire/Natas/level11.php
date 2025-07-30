<?php

/**
 * Overthewire平台Level11
 *
 * @category Null
 * @package  Module
 * @author   Bin <h.bingo@qq.com>
 * @license  MIT License
 * @version  GIT: 0.1
 * @link     https://github.com
 */

$originalString = json_encode(array("showpassword" => "no", "bgcolor" => "#ffffff"));
$cookieString = base64_decode("HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GdGdfVXRnTRg%3D");

echo $originalString ^ $cookieString;
echo "\n";

$key = "eDWo";
$newString = json_encode(array("showpassword" => "yes", "bgcolor" => "#ffffff"));
$newCookieString = "";

for ($i = 0; $i < strlen($newString); $i++) {
    $newCookieString .= $key[$i % strlen($key)] ^ $newString[$i];
}

echo base64_encode($newCookieString);

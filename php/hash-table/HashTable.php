<?php

$array = [];
$array['a'] = 1001;
$array['b'] = 'Hello World';
$array['c'] = '999999';
$array['d'] = true;
$array['e'] = 99.99;
$array['f'] = ['P', 'H', 'P'];
$array['g'] = new \stdClass();
$array['g']->method = function () {
    return 'this is a method';
};
$array['h'] = null;
$array['i'] = fopen(__DIR__ . '/../.gitignore', 'r');

foreach ($array as $key => $val) {
    if (is_array($val)) {
        $val = implode('', $val);
    } elseif (is_object($val)) {
        $func = $val->method;
        $val = $func();
    }

    echo gettype($val), "\t", $key, ' => ', $val, PHP_EOL;
}

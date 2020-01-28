<?php

require __DIR__ . '/BruteForceSearch.php';

class BruteForceSearchTest
{
    public static function main(): void
    {
        var_dump(BruteForceSearch::search('890', '1234567890'));
        var_dump(BruteForceSearch::search('World', 'Hello World!'));
        var_dump(BruteForceSearch::search('abc', 'abc'));
        var_dump(BruteForceSearch::search('iphone', 'phone'));
    }
}

BruteForceSearchTest::main();

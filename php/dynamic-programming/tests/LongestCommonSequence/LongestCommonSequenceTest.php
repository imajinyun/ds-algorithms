<?php

declare(strict_types=1);

namespace DynamicProgramming\Test\LongestCommonSequence;

use DynamicProgramming\LongestCommonSequence\LongestCommonSequence;
use PHPUnit\Framework\TestCase;

class LongestCommonSequenceTest extends TestCase
{
    public function testLongestCommonSequence(): void
    {
        $expect = [
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 2, 2],
           [1, 1, 2, 3],
        ];
        self::assertSame($expect, LongestCommonSequence::search('fish', 'fosh'));
    }
}

import Data.List ()
import Data.Char(digitToInt)

elem' :: Int -> [[Int]] -> Bool
elem' val = foldr ((||) . elem val) False

sumMissing :: [[Int]] -> [Int] -> Int
sumMissing square seq = sum [sum (square!!i) | i <- [0..4]] - sum [ val | val <- seq, elem' val square ]

check :: [Int] -> [Int] -> Int --only first to win considering rows then columns
check foundRows foundCols = if not . null $ board then head board else -1
    where board = [div i 5 | i <- [0..length foundRows-1], foundRows!!i == 5]++[div j 5 | j <- [0..length foundCols-1], foundCols!!j == 5]

foundUpdate :: Int -> [[Int]] -> [Int] -> [Int] -> ([Int], [Int])
foundUpdate num arr foundRows foundCols = ([foundRows!!i + if elem num (arr!!i) then 1 else 0| i <- [0..length foundRows-1]], [foundCols!!i + if elem num [arr!!(div i 5 + mod i 5)!!k | k <- [0..4]] then 1 else 0| i <- [0..length foundCols-1]])

find :: Int -> [[Int]] -> [Int] -> [Int] -> ([Int], [Int], Int)
find num arr foundRows foundCols = (foundRowsNew, foundColsNew, check foundRowsNew foundColsNew)
    where (foundRowsNew, foundColsNew) = foundUpdate num arr foundRows foundCols

engine :: [Int] -> [Int]  -> [[Int]] -> [Int] -> [Int] -> Int
engine (num:seq) finalSeq arr foundRows foundCols = if ended /= -1 then num*sumMissing [arr!!((5*ended)+i) | i <- [0..4]] (filter (\x -> notElem x seq) finalSeq) else engine seq finalSeq arr fr fc
    where (fr, fc, ended) = find num arr foundRows foundCols

ex1 :: [Int] -> [[Int]] -> Int --launcher
ex1 seq arr = engine seq seq arr [0 | row <- [1..length arr]] [0 | col <- [1..length arr]]

parse :: [String] -> ([Int], [[Int]])
parse xs = ([read num :: Int | num <- wordsWhen (==',') . head $ xs],
            filter (not . null) [[read num :: Int | num <- words line] | line <- tail xs])

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'

main :: IO ()
main = do
    strLines <- readFile "./4/data.txt"
    let (seq, arr) = parse $ lines strLines
    print $ ex1 seq arr

    
import Data.List ()

iIncr :: [Int] -> Int -> [Int]
iIncr xs i
    | length xs < i+1 = []
    | otherwise = if head xs < (xs!!i) then (xs!!i) : iIncr (tail xs) i else iIncr (tail xs) i 

ex1 :: [Int] -> Int
ex1 xs = length . iIncr xs $ 1

ex2 :: [Int] -> Int
ex2 xs = length . iIncr xs $ 3

main :: IO ()
main = do
    strLines <- readFile "1/data.txt"
    let xs = map (\x -> read x :: Int) $ lines strLines
    print $ ex1 xs
    print $ ex2 xs

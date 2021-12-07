import Data.List (sort)

median :: [Int] -> Int
median xs = sort xs!!div (length xs) 2

ex1 :: [Int] -> Int
ex1 locations = sum [abs (med - locations!!i) | i <- [0..length locations -1]]
    where med = median locations

arithmeticSum :: Int -> Int -> Int
arithmeticSum x crabMedian = div (k*(k+1)) 2
    where k = abs (crabMedian - x)

reqFuel :: Int -> [Int] -> Int
reqFuel x = sum . map (\el -> arithmeticSum el x)

ex2 :: [Int] -> Int
ex2 locations = minimum . map (\loc -> reqFuel loc locations) $ [0..length locations -1]

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'

main :: IO ()
main = do
    strLines <- readFile "./7/data.txt"
    let locations = map (\el -> read el :: Int) . wordsWhen (==',') . head . lines $ strLines
    print $ ex1 locations
    print $ ex2 locations
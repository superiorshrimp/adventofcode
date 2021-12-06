update :: [Int] -> [Int]
update day = [if d==8 then rem else if d==6 then day!!(d+1)+rem else day!!(d+1) | d <- [0..length day -1]]
    where rem = head day

engine :: [Int] -> Int -> Int
engine day 0    = sum day
engine day days = engine (update day) (days-1)

ex1 :: [Int] -> Int
ex1 fish = engine [length . filter (==i) $ fish | i <- [0..8]] 80

ex2 :: [Int] -> Int
ex2 fish = engine [length . filter (==i) $ fish | i <- [0..8]] 256

parse :: [String] -> [Int]
parse = map (\x -> read x :: Int) . wordsWhen (==',') . head

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'

main :: IO ()
main = do
    strLines <- readFile "./6/data.txt"
    let arr = parse $ lines strLines
    print $ ex1 arr
    print $ ex2 arr
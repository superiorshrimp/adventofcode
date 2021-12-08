ex1 :: [[String]] -> [[String]] -> Int
ex1 _ output = sum [ sum [ if elem (length digit) [2,3,4,7] then 1 else 0| digit <- line] |line <- output] --can rewrite as filter

intersection :: String -> String -> Int
intersection word1 word2 = sum [if elem letter word2 then 1 else 0 | letter <- word1] --like above

getUnique :: [(Int,String)] -> Int -> String
getUnique lengths len = last . head . filter (\(l, val) -> l == len) $ lengths
    
findDigit :: String -> [(Int,String)] -> String
findDigit number lengths = case length number of
    2 -> "1"
    4 -> "4"
    3 -> "7"
    7 -> "8"
    6 -> if intersection number (getUnique lengths 4) == 4 then "9" else if intersection number (getUnique lengths 2) == 1 then "6" else "0"
    5 -> if intersection number (getUnique lengths 4) == 2 then "2" else if intersection number (getUnique lengths 2) == 2 then "3" else "5"

findNumber :: [String] -> [String] -> Int
findNumber digits output = read (findDigit (head digits) lengths ++ findDigit (digits!!1) lengths ++ findDigit (digits!!2) lengths ++ findDigit (last digits) lengths) :: Int
    where lengths = [(length digit, digit) | digit <- digits]

engine :: [[String]] -> [[String]] -> Int -> Int
engine []             []            sum = sum
engine (digit:digits) (line:output) sum = engine digits output (sum+newSum)
    where newSum = findNumber digit line

ex2 :: [[String]] -> [[String]] -> Int
ex2 digits output = engine digits output 0

parse :: [String] -> ([[String]], [[String]])
parse input = ([words . head $ line | line <- divided] , [words . last $ line | line <- divided])
    where divided = [wordsWhen (=='|') line | line <- input]

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'

main :: IO ()
main = do
    strLines <- readFile "./8/data.txt"
    let (digits, output) = parse . lines $ strLines
    print $ ex1 digits output
    print $ ex2 digits output
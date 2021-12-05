transpose :: [[Int]] -> [[Int]]
transpose ([]:_) = []
transpose x      = map head x : transpose (map tail x)

findMaxX :: [[Int]] -> Int
findMaxX = foldr (\ line -> max (max (head line) (line !! 2))) 0

findMaxY :: [[Int]] -> Int
findMaxY = foldr (\ line -> max (max (line!!1) (line!!3))) 0

drawHor :: [Int] -> [[Int]] -> [[Int]]
drawHor [x1, y1, x2, y2] hmap = take (y1-1) hmap ++ [[if x>=min x1 x2 && x<=max x1 x2 then (if (hmap!!y1!!x)==0 then 1 else 2) else hmap!!y1!!x | x <- [0..(length . head $ hmap) -1]]] ++ drop y1 hmap

drawVer :: [Int] -> [[Int]] -> [[Int]]
drawVer [x1, y1, x2, y2] hmap = take (x1-1) hmap ++ [[if (y>=min y1 y2) && (y<=max y1 y2) then (if (hmap!!y!!(x1-1))==0 then 1 else 2) else hmap!!y!!(x1-1) | y <- [0..(length . head $ hmap) -1]]] ++ drop x1 hmap

draw :: [Int] -> [[Int]] -> [[Int]]
draw [x1, y1, x2, y2] hmap
    | x1 == x2  = transpose . reverse . drawVer [x1, y1, x2, y2] . reverse . transpose $ hmap 
    | y1 == y2  = drawHor [x1, y1, x2, y2] hmap
    | otherwise = hmap

--cos z tymi rotacjiami nie dziala


count2s :: [[Int]] -> Int
count2s = foldr ((+) . (length . filter (== 2))) 0

engine :: [[Int]] -> [[Int]] -> [[Int]]
engine []         hmap = hmap
engine (line:arr) hmap = engine arr (draw line hmap)

ex1 :: [[Int]] -> [[Int]]
ex1 arr = engine arr [[0 | col <- [0..len]]| row <- [0..len]]
    where len = max (findMaxX arr) (findMaxY arr)

removeCommas :: [String] -> [[String]]
removeCommas arr = [wordsWhen (==',') line | line <- arr]

removeArrow :: [String] -> [String]
removeArrow arr = [[ x | x <- line, notElem x "->" ] | line <- arr]

parse :: [String] -> [[Int]]
parse arr = [map (\x -> read x :: Int) (head (almost!!i) ++ almost!!i!!1) | i <- [0..length arr -1]]
    where almost = [removeCommas . words $ line | line <- removeArrow arr]

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'

main :: IO ()
main = do
    strLines <- readFile "./5/data.txt"
    let arr = parse $ lines strLines
    print $ ex1 arr
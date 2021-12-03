import Data.List ()

adjustInput :: [[String]] -> [(String, Int)] 
adjustInput = map (\[x, y] -> (x,read y :: Int))

data Location = MkLocation {horizontal :: Int, aim :: Int, depth :: Int}

ex1 :: [(String, Int)] -> Location -> Int
ex1 []             (MkLocation {horizontal = x, aim = a, depth = y}) = x * y
ex1 ((dir,val):xs) (MkLocation {horizontal = x, aim = a, depth = y}) = case head dir of
    'f' -> ex1 xs (MkLocation (x+val) a y)
    'd' -> ex1 xs (MkLocation x a (y+val))
    'u' -> ex1 xs (MkLocation x a (y-val))

ex2 :: [(String, Int)] -> Location -> Int
ex2 []             (MkLocation {horizontal = x, aim = a, depth = y}) = x * y
ex2 ((dir,val):xs) (MkLocation {horizontal = x, aim = a, depth = y}) = case head dir of
    'f' -> ex2 xs (MkLocation (x+val) a (y+a*val))
    'd' -> ex2 xs (MkLocation x (a+val) y)
    'u' -> ex2 xs (MkLocation x (a-val) y)

main :: IO ()
main = do
    strLines <- readFile "2/data.txt"
    let xs = adjustInput . map words $ lines strLines
    let loc = MkLocation 0 0 0
    print $ ex1 xs loc
    print $ ex2 xs loc

import Data.List ()
import Data.Char(digitToInt)

oppositePositive :: Int -> Int -> Int
oppositePositive a len = 2^len-1-a

toDecimal :: [Int] -> Int
toDecimal [] = 0
toDecimal (x:xs) = x*2^length xs + toDecimal xs

createGamma :: [String] -> Int -> Int -> [Int]
createGamma xs i len
    | i == 0 = []
    | otherwise = (if sum [digitToInt (xs!!j!!(len-i)) | j <- [0..length xs - 1]] > div (length xs) 2 + mod (length xs) 2 then 1 else 0) : createGamma xs (i-1) len

ex1gamma :: [String] -> Int -> Int
ex1gamma xs len = toDecimal (createGamma xs len len)

count1s :: [String] -> Int -> Int
count1s xs i = if (length . filter (== '1') $ [xs!!j!!i | j <- [0..length xs-1]]) >= (div (length xs) 2 + mod (length xs) 2)
    then 1
    else 0

oxGenRating :: [String] -> Int -> Int
oxGenRating xs i
    | length xs == 1 = toDecimal [digitToInt (head xs!!j) :: Int | j <- [0..(length . head) xs - 1]]
    | otherwise = oxGenRating (filter (\x -> digitToInt (x!!i) == count1s xs i) xs) (i+1)

co2scrRating :: [String] -> Int -> Int
co2scrRating xs i
    | length xs == 1 = toDecimal [digitToInt (head xs!!j) :: Int | j <- [0..(length . head) xs - 1]]
    | otherwise = co2scrRating (filter (\x -> digitToInt (x!!i) /= count1s xs i) xs) (i+1)

ex1 :: [String] -> Int
ex1 xs = ex1gamma xs len * oppositePositive (ex1gamma xs len) len
    where len = (length . head) xs

ex2 :: [String] -> Int
ex2 xs = oxGenRating xs 0 * co2scrRating xs 0

main :: IO ()
main = do
    strLines <- readFile "3/data.txt"
    let xs = lines strLines
    print $ ex1 xs
    print $ ex2 xs

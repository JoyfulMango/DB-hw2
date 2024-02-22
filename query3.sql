SELECT COUNT(*)
FROM Categories
GROUP BY Categories.ItemID
HAVING COUNT(*) = 4;

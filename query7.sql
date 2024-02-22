WITH COUNTER AS (
    SELECT *
    FROM Bids B, Categories C
    WHERE B.ItemID = C.ItemID
    AND B.Amount > 100
    GROUP BY C.Category
    HAVING COUNT(*) >= 1
)
SELECT COUNT(*)
FROM COUNTER;


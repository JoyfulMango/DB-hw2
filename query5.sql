SELECT COUNT(*)
FROM Sellers S, Users U
WHERE S.SellerID = U.UserID
AND U.Rating > 1000;

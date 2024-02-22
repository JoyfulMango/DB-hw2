SELECT COUNT(*)
FROM Sellers S, Bidders B
WHERE S.SellerID = B.BidderID;

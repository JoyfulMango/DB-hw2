DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Sellers;
DROP TABLE IF EXISTS Bidders;
DROP TABLE IF EXISTS Bids;
DROP TABLE IF EXISTS Categories;

CREATE TABLE Items(
    ItemID INTEGER,
    Name TEXT NOT NULL,
    Currently TEXT NOT NULL,
    Buy_Price TEXT,
    First_Bid TEXT NOT NULL,
    Number_of_Bids INTEGER NOT NULL,
    Started TEXT NOT NULL,
    Ends TEXT NOT NULL,
    SellerID INTEGER NOT NULL,
    Description TEXT NOT NULL,
    PRIMARY KEY (ItemID),
    FOREIGN KEY (SellerID) REFERENCES Sellers
);

CREATE TABLE Users(
    UserID INTEGER,
    Rating INTEGER NOT NULL,
    PRIMARY KEY (UserID)
);

CREATE TABLE Sellers(
    SellerID INTEGER,
    Location TEXT NOT NULL,
    Country TEXT NOT NULL,
    PRIMARY KEY (SellerID),
    FOREIGN KEY (SellerID) REFERENCES Users
);

CREATE TABLE Bidders(
    BidderID INTEGER,
    Location TEXT,
    Country TEXT,
    PRIMARY KEY (BidderID),
    FOREIGN KEY (BidderID) REFERENCES Users
);

CREATE TABLE Bids(
    BidderID INTEGER,
    ItemID INTEGER,
    Time TEXT NOT NULL,
    Amount TEXT,
    PRIMARY KEY (BidderID, ItemID, Amount)
    FOREIGN KEY (BidderID) REFERENCES Bidders,
    FOREIGN KEY (ItemID) REFERENCES Items
);

CREATE TABLE Categories(
    ItemID INTEGERS,
    Category TEXT,
    PRIMARY KEY (ItemID, Category),
    FOREIGN KEY (ItemID) REFERENCES Items
);

    
    


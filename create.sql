DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Sellers;
DROP TABLE IF EXISTS Bidders;
DROP TABLE IF EXISTS Bids;
DROP TABLE IF EXISTS Categories;

CREATE TABLE Items(
    ItemID INTEGER,
    Name TEXT NOT NULL,
    Currently REAL,
    Buy_Price REAL,
    First_Bid REAL,
    Number_of_Bids INTEGER,
    Started TEXT,
    Ends TEXT,
    SellerID INTEGER,
    Description TEXT,
    PRIMARY KEY (ItemID),
    FOREIGN KEY (SellerID) REFERENCES Sellers
);

CREATE TABLE Users(
    UserID TEXT,
    Rating INTEGER,
    Location TEXT,
    Country TEXT,
    PRIMARY KEY (UserID)
);

CREATE TABLE Sellers(
    SellerID TEXT,
    PRIMARY KEY (SellerID),
    FOREIGN KEY (SellerID) REFERENCES Users
);

CREATE TABLE Bidders(
    BidderID TEXT,
    PRIMARY KEY (BidderID),
    FOREIGN KEY (BidderID) REFERENCES Users
);

CREATE TABLE Bids(
    BidderID TEXT,
    ItemID INTEGER,
    Time TEXT,
    Amount REAL,
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

    
    



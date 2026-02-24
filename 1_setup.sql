-- 1. Create Customers Table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100),
    Country VARCHAR(50),
    JoinDate DATE
);

-- 2. Create Products Table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Category VARCHAR(50),
    ProductName VARCHAR(100),
    Price DECIMAL(10, 2)
);

-- 3. Create Orders Table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    OrderDate DATE,
    Quantity INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- 4. Insert Dummy Data
INSERT INTO Customers VALUES 
(1, 'Alice Johnson', 'USA', '2023-01-15'),
(2, 'Bob Smith', 'UK', '2023-02-20'),
(3, 'Charlie Brown', 'Canada', '2023-03-10'),
(4, 'Diana Prince', 'USA', '2022-11-05'),
(5, 'Evan Wright', 'UK', '2022-08-30');

INSERT INTO Products VALUES 
(101, 'Electronics', 'Laptop Pro', 1200.00),
(102, 'Electronics', 'Smartphone X', 800.00),
(103, 'Furniture', 'Ergo Chair', 350.00),
(104, 'Furniture', 'Standing Desk', 500.00),
(105, 'Accessories', 'Noise Cancelling Headphones', 200.00);

INSERT INTO Orders VALUES 
(1001, 1, 101, '2023-06-01', 1),
(1002, 1, 105, '2023-06-01', 2),
(1003, 2, 103, '2023-01-15', 4),
(1004, 3, 102, '2023-08-10', 1),
(1005, 4, 104, '2022-12-20', 1),
(1006, 5, 101, '2022-09-01', 1),
(1007, 1, 103, '2024-01-20', 1);
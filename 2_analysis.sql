/* PROJECT: Customer Retention Analysis
   GOAL: Identify "High Value" customers (Spent > $500) who are at risk of churning.
*/

WITH CustomerStats AS (
    SELECT 
        c.Name,
        c.Country,
        SUM(p.Price * o.Quantity) as TotalSpent,
        MAX(o.OrderDate) as LastOrderDate
    FROM Customers c
    JOIN Orders o ON c.CustomerID = o.CustomerID
    JOIN Products p ON o.ProductID = p.ProductID
    GROUP BY c.CustomerID, c.Name, c.Country
)

SELECT 
    Name,
    Country,
    TotalSpent,
    LastOrderDate,
    CASE 
        WHEN LastOrderDate < '2023-07-01' THEN 'Churn Risk'
        ELSE 'Active'
    END as CustomerStatus
FROM CustomerStats
WHERE TotalSpent > 500
ORDER BY TotalSpent DESC;
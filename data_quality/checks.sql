-- Missing Customers
SELECT COUNT(*) FROM transactions
WHERE customer_id IS NULL;

-- Invalid Price
SELECT COUNT(*) FROM transactions
WHERE unit_price <= 0;

-- Invalid Quantity (not cancellation)
SELECT COUNT(*) FROM transactions
WHERE quantity < 0
AND invoice_no NOT LIKE 'C%';

-- Duplicate Transactions
SELECT COUNT(*) FROM (
    SELECT invoice_no, stock_code, COUNT(*)
    FROM transactions
    GROUP BY invoice_no, stock_code
    HAVING COUNT(*) > 1
);

-- Missing Descriptions
SELECT COUNT(*) FROM products
WHERE description IS NULL;

-- Cancellation Consistency
SELECT COUNT(*) FROM transactions
WHERE invoice_no LIKE 'C%'
AND quantity > 0;

-- Extreme Outliers
SELECT COUNT(*) FROM transactions
WHERE quantity > 10000 OR unit_price > 10000;
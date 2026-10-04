# Data Quality Framework

## Completeness
- Customer ID should not be null

## Uniqueness
- Invoice + StockCode should be unique

## Validity
- Price must be > 0
- Quantity must be > 0 unless cancellation

## Consistency
- Cancellation invoices (starting with 'C') must have negative quantity
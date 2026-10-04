import sqlite3
from datetime import datetime

# Fix datetime warning
sqlite3.register_adapter(datetime, lambda val: val.isoformat())

DB_PATH = "data/pipeline.db"

checks = [
    ("Missing Customers",
     "SELECT COUNT(*) FROM transactions WHERE customer_id IS NULL",
     "HIGH"),

    ("Invalid Price",
     "SELECT COUNT(*) FROM transactions WHERE unit_price <= 0",
     "HIGH"),

    ("Invalid Quantity",
     "SELECT COUNT(*) FROM transactions WHERE quantity < 0 AND invoice_no NOT LIKE 'C%'",
     "MEDIUM"),

    ("Duplicate Transactions",
     """
     SELECT COUNT(*) FROM (
        SELECT invoice_no, stock_code, COUNT(*)
        FROM transactions
        GROUP BY invoice_no, stock_code
        HAVING COUNT(*) > 1
     )
     """,
     "HIGH"),

    ("Missing Descriptions",
     "SELECT COUNT(*) FROM products WHERE description IS NULL",
     "LOW"),

    ("Cancellation Errors",
     "SELECT COUNT(*) FROM transactions WHERE invoice_no LIKE 'C%' AND quantity > 0",
     "HIGH"),

    ("Outliers",
     "SELECT COUNT(*) FROM transactions WHERE quantity > 10000 OR unit_price > 10000",
     "MEDIUM")
]


def run_checks():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create logging table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data_quality_logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        check_name TEXT,
        result_count INTEGER,
        severity TEXT,
        run_timestamp TEXT
    )
    """)

    results = []

    for name, query, severity in checks:
        cursor.execute(query)
        result = cursor.fetchone()[0]
        results.append((name, result, severity))

        cursor.execute("""
            INSERT INTO data_quality_logs (check_name, result_count, severity, run_timestamp)
            VALUES (?, ?, ?, ?)
        """, (name, result, severity, datetime.now()))

        print(f"{name}: {result}")

    # Data health score
    total_errors = sum(r[1] for r in results)
    health_score = max(0, 100 - total_errors * 0.0001)

    print(f"\n📊 Data Health Score: {health_score:.2f}")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    run_checks()
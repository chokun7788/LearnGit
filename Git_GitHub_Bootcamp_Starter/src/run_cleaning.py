import csv
from pathlib import Path

from src.cleaning import normalize_city, parse_amount

INPUT_PATH = Path("data/sample_orders.csv")
OUTPUT_PATH = Path("outputs/orders_cleaned.csv")
FIELDS = ["order_id", "customer_id", "city", "amount", "status"]


def run() -> int:
    cleaned = []
    seen_ids = set()

    with INPUT_PATH.open("r", encoding="utf-8-sig", newline="") as source:
        for row in csv.DictReader(source):
            order_id = row["order_id"].strip()
            if not order_id or order_id in seen_ids:
                continue

            amount = parse_amount(row["amount"])
            if amount is None:
                continue

            cleaned.append({
                "order_id": order_id,
                "customer_id": row["customer_id"].strip(),
                "city": normalize_city(row["city"]),
                "amount": f"{amount:.2f}",
                "status": row["status"].strip(),
            })
            seen_ids.add(order_id)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as destination:
        writer = csv.DictWriter(destination, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(cleaned)
    return len(cleaned)


if __name__ == "__main__":
    print(f"Saved {run()} cleaned orders to {OUTPUT_PATH}")

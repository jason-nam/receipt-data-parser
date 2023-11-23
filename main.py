from pathlib import Path

from src import group_item_receipt

CSV_FILE_PATH = 'data/input'

def main():
    files = list(Path(CSV_FILE_PATH).glob('*.[cC][sS]*[vV]'))

    for file in files:
        items = group_item_receipt(file=file)
        
        for item in items:
            # print(f"Item: {item['item']}, Quantity: {item['quantity']}, Price: {item['price']}")
            print(f"Item: {item['item']}, Price: {item['price']}")
        print("\n")

if __name__ == "__main__":
    main()

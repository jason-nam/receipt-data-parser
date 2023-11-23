from sklearn.cluster import DBSCAN
import numpy as np
from pathlib import Path
import re

try:
    from .util import read_csv
    from .constants import CSV_FILE_PATH
except:
    from util import read_csv
    from constants import CSV_FILE_PATH

def is_price(text):
    match = re.search(r'(\d+\.\d+)', text)
    if match:
        try:
            float(match.group(1))
            return True
        except ValueError:
            return False
    return False

def is_quantity(text):
    return text.isdigit()

def cluster_lines(data):
    y_coords = np.array([[int(row[1])] for row in data])
    
    # clustering
    clustering = DBSCAN(eps=10, min_samples=1).fit(y_coords)
    labels = clustering.labels_

    # grouping
    clustered_data = {}
    for label, row in zip(labels, data):
        clustered_data.setdefault(label, []).append(row)

    return clustered_data

def group_items(data):
    items = []
    for cluster in data.values():
        item_name = ''
        price_parts = []
        quantity = None

        sorted_cluster = sorted(cluster, key=lambda x: int(x[0]))
        for i, (_, _, _, _, text) in enumerate(sorted_cluster):
            # check text for segments that ends with a period to indicate price digit cutoff
            if text.endswith('.') and i + 1 < len(sorted_cluster) and sorted_cluster[i + 1][4].replace('.', '', 1).isdigit():
                price_parts.append(text + sorted_cluster[i + 1][4])
            elif is_price(text):
                price_parts.append(text)
            # elif is_quantity(text):
            #     quantity = int(text)
            else:
                item_name += text + ' '

        # price
        price = None
        for part in price_parts:
            try:
                potential_price = float(part)
                if price is None or potential_price < price:
                    price = potential_price
            except ValueError:
                continue

        if item_name and price is not None:
            # items.append({'item': item_name.strip(), 'quantity': quantity, 'price': price})
            items.append({'item': item_name.strip(), 'price': price})

        # print(items)

    return items

def group_item_receipt(data=None, file=None):
    if not data:
        try: 
            data = read_csv(file)
        except ValueError:
            print(f"File: {file} is wrong file path or was not given.")
            return None
        
    clustered_data = cluster_lines(data)
    items = group_items(clustered_data)

    return items

def main():
    files = list(Path(CSV_FILE_PATH).glob('*.[cC][sS]*[vV]'))
    
    for file in files:
        data = read_csv(file)
        clustered_data = cluster_lines(data)
        items = group_items(clustered_data)

        for item in items:
            # print(f"Item: {item['item']}, Quantity: {item['quantity']}, Price: {item['price']}")
            print(f"Item: {item['item']}, Price: {item['price']}")
        print("\n")

if __name__ == "__main__":
    main()
    

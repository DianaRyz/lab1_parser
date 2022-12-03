#import random
import csv


def next_element(class_name: str, count: int, csv_path: str = "copy_dataset.csv") -> str or None:

    """
    The function returns the path of the element following count if there is no element
    returns None
        class_name(str): tiger or leopard
        count(int): element number
    """
    element_list = []
    headings = ["Absolute way", "Relative way", "Class"]
    with open(csv_path, "r", encoding="utf8") as f:
        read = csv.DictReader(f, fieldnames=headings, delimiter=";")
        for element in read:
            if element["Class"] == class_name:
                element_list.append([element["Absolute way"], element["Relative way"], element["Class"]])
    if count + 1 < len(element_list):
        element_dict = {headings[k]: element_list[count + 1][k] for k in range(0, len(headings))}
        return element_dict["Absolute way"]
    else:
        return None


if __name__ == "__main__":

    #random_list = list()
    #random.shuffle(random_list)
    for i in range(0, 1100):
        item = next_element("tiger", i)
        print(item)
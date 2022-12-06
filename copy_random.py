import os
import csv
import random
import shutil


def write_copy(item: int, class_name: str, random_path: str, csv_path: str = "copy_random.csv") -> None:
    """
    Record annotation copy element
        item (int): copy number
        class_name (str): tiger or leopard
        random_path (str): path to the another directory
    """

    headings = ["Absolute way", "Relative way", "Class"]
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        write_in_file = csv.DictWriter(
            f, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
        )
        write_in_file.writerow(
            {
                "Absolute way": random_path,
                "Relative way": f"dataset/random_dataset/{str(item).zfill(5)}.jpg",
                "Class": class_name,
            }
        )


def copy_to_random(path_to_dataset: str, path_to_random: str, csv_path: str = "copy_random.csv") -> str or None:

    """
    Copies data with random name
        dataset_path(str): path to the dataset
        random_path(str): path to the copy directory
    """
    if not os.path.exists(path_to_random):
        os.mkdir(path_to_random)

    headings = ["Absolute way", "Relative way", "Class"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
        )
        writer.writeheader()

    random_numbers = list(range(0, 10001))
    random.shuffle(random_numbers)
    random_num1 = random_numbers[: len(random_numbers) // 2]
    random_num2 = random_numbers[len(random_numbers) // 2:]

    class_name = "tiger"
    path_class = path_to_dataset + "/" + class_name
    count_files = len(
        [
            element
            for element in os.listdir(path_class)
            if os.path.isfile(os.path.join(path_class, element))
        ]
    )

    for i in range(0, count_files):
        path = path_class + f"/{str(i).zfill(4)}.jpg"
        new_path = path_to_random + f"/{str(random_num1[i]).zfill(5)}.jpg"
        if os.path.isfile(path):
            shutil.copyfile(path, new_path)
            write_copy(random_num1[i], class_name, new_path, csv_path)

    class_name = "leopard"
    path_class = path_to_dataset + "/" + class_name
    count_files = len(
        [
            element
            for element in os.listdir(path_class)
            if os.path.isfile(os.path.join(path_class, element))
        ]
    )

    for i in range(0, count_files):
        path = path_class + f"/{str(i).zfill(4)}.jpg"
        new_path = path_to_random + f"/{str(random_num2[i]).zfill(5)}.jpg"
        if os.path.isfile(path):
            shutil.copyfile(path, new_path)
            write_copy(random_num2[i], class_name, new_path, csv_path)


if __name__ == "__main__":
    path_dataset = "D:/dataset"
    path_random = "D:/dataset/random_dataset"
    copy_to_random(path_dataset, path_random)
import os
import csv
import shutil


def write_copy(item: int, class_name: str, copy_path: str, csv_path: str = "copy_dataset.csv") -> None:

    """
    Record annotation copyelement
        item (int): copy number
        class_name (str): tiger or leopard
        copy_path (str): path to the copy directory
        csv_path(str, optional): path to the csv-file
    """

    headings = ["Absolute way", "Relative way", "Class"]
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        write_in_file = csv.DictWriter(
            f, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
        )
        write_in_file.writerow(
            {
                "Absolute way": copy_path,
                "Relative way": f"dataset/copy_dataset/{class_name}_{str(item).zfill(4)}.jpg",
                "Class": class_name,
            }
        )


def copy_to_another(path_to_copy: str, path_to_dataset: str, csv_path: str = "copy_dataset.csv") -> str or None:

    """
    Копирует данные из dataset в другую директорию
    Ключевые аргументы:
        path_to_another(str): путь до другой директории
        path_to_dataset(str): путь до dataset
        csv_path(str, optional): путь до csv файла
    """
    if not os.path.exists(path_to_copy):
        os.mkdir(path_to_copy)

    headings = ["Absolute way", "Relative way", "Class"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
        )
        writer.writeheader()

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
        new_path = path_class + f"/{class_name}_{str(i).zfill(4)}.jpg"
        if os.path.isfile(path):
            shutil.copyfile(path, new_path)
            write_copy(i, class_name, new_path, csv_path)

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
        new_path = path_to_copy + f"/{class_name}_{str(i).zfill(4)}.jpg"
        if os.path.isfile(path):
            shutil.copyfile(path, new_path)
            write_copy(i, class_name, new_path, csv_path)


if __name__ == "__main__":
    path_to_dataset = "D:/dataset"
    path_to_another_dataset = "D:/dataset/copy_dataset"
    copy_to_another(path_to_another_dataset, path_to_dataset)
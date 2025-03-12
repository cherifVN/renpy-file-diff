import os

def compare_file_contents(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        content1 = file1.read()
        content2 = file2.read()
        return content1 == content2

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print("Le chemin du dossier est:", script_dir)

    folders = os.listdir(script_dir)
    folder_count = 0
    for folder in folders:
        if os.path.isdir(os.path.join(script_dir, folder)):
            folder_count += 1

    if folder_count != 2:
        print("Le dossier doit contenir exactement 2 dossiers de premier niveau.")
        return

    folder_names = [folder for folder in folders if os.path.isdir(os.path.join(script_dir, folder))]
    folder1_path = os.path.join(script_dir, folder_names[0])
    folder2_path = os.path.join(script_dir, folder_names[1])

    rpy_files1 = [f for f in os.listdir(folder1_path) if f.endswith('.rpy')]
    rpy_files2 = [f for f in os.listdir(folder2_path) if f.endswith('.rpy')]

    same_name_different_content = []
    same_name_same_content = []
    unique_files = []

    for file1 in rpy_files1:
        if file1 in rpy_files2:
            file1_path = os.path.join(folder1_path, file1)
            file2_path = os.path.join(folder2_path, file1)
            if compare_file_contents(file1_path, file2_path):
                same_name_same_content.append(file1)
            else:
                same_name_different_content.append(file1)
        else:
            unique_files.append((file1, folder_names[0]))

    for file2 in rpy_files2:
        if file2 not in rpy_files1:
            unique_files.append((file2, folder_names[1]))

    print("\nFichiers avec le même nom et contenu identique :")
    print(same_name_same_content)

    print("\nFichiers avec le même nom mais un contenu différent :")
    print(same_name_different_content)

    print("\nFichiers uniques dans l'un ou l'autre des dossiers :")
    for file, folder in unique_files:
        print(f"{file} (dans {folder})")

if __name__ == "__main__":
    main()
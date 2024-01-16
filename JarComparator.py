import zipfile
import hashlib

def get_file_hashes(jar_path):
    """
    Extracts files from a JAR and returns a dictionary of file names and their hash values.
    """
    file_hashes = {}
    with zipfile.ZipFile(jar_path, 'r') as jar:
        for file_info in jar.infolist():
            if not file_info.is_dir():
                file_name = file_info.filename
                file_data = jar.read(file_name)
                file_hashes[file_name] = hashlib.md5(file_data).hexdigest()
    return file_hashes

def compare_jars(jar_path1, jar_path2):
    """
    Compares two JAR files and categorizes the differences.
    """
    jar1_hashes = get_file_hashes(jar_path1)
    jar2_hashes = get_file_hashes(jar_path2)

    modified_files = []
    added_files = []
    removed_files = []

    all_files = set(jar1_hashes.keys()).union(set(jar2_hashes.keys()))

    for file in all_files:
        if file in jar1_hashes and file not in jar2_hashes:
            removed_files.append(file)
        elif file not in jar1_hashes and file in jar2_hashes:
            added_files.append(file)
        elif jar1_hashes[file] != jar2_hashes[file]:
            modified_files.append(file)

    return modified_files, added_files, removed_files

# Example usage
jar_path_1 = 'path_to_first_jar.jar'
jar_path_2 = 'path_to_second_jar.jar'
modified_files, added_files, removed_files = compare_jars(jar_path_1, jar_path_2)

print("Modified files:")
for file in modified_files:
    print(file)

print("\nAdded files:")
for file in added_files:
    print(file)

print("\nRemoved files:")
for file in removed_files:
    print(file)

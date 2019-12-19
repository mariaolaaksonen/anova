import os
import argparse


def main(root_dir, label, output_dir, delimiter):
    output_name = root_dir.strip("/").split("/")[-1]
    label_name = "label" + label
    for root, dir_list, file_list in os.walk(root_dir):
        if "skeleton" in root and label_name in root:
            write_file = []
            dir_name = root.split("/")[-2].split("skeleton")[-1]
            output_name_full = output_name + "_" + dir_name + "_" + label_name + ".txt"
            output_path = os.path.join(output_dir, output_name_full)
            for ffile2 in file_list:
                if ".txt" in ffile2:
                    #print(ffile2)
                    ffile2_path = os.path.join(root, ffile2)
                    with open(ffile2_path) as open_file:
                        patient = []
                        for line in open_file:
                            row = line.strip("\n")
                            patient.append(row)
                        write_file.append(patient)
            with open(output_path, "w+") as output_file:
                for i in range(0, len(patient)):
                    write_row = []
                    for row in write_file:
                        write_row.append(row[i])
                    if delimiter == "tab":
                        write_row = "\t".join(write_row) + "\n"
                    else:
                        write_row = delimiter.join(write_row) + "\n"
                    output_file.write(write_row)
            print(f"File {output_path} WRITTEN")
                                



if __name__ == "__main__":
    # Run example: python3 write_brain_files.py --root-dir venla_test/permutation_fromn6/ --output-dir output/ --label 1 --delimiter "tab"
    # Run on python3!
    parser = argparse.ArgumentParser(description='Process data into Aito from csv.')
    parser.add_argument('--root-dir', '-rd', dest='root_dir', type=str, required=True, help="Path to the permutation_from directory")
    parser.add_argument('--output-dir', '-od', dest='output_dir', type=str, required=True, help="Directory where to write files")
    parser.add_argument('--label', '-l', dest='label', type=str, required=True, help="Label for which combined file is created")
    parser.add_argument('--delimiter', '-d', dest='delimiter', type=str, required=True, choices=["tab", ",", ";"], help="How the columns are delimited")

    args = parser.parse_args()
    main(args.root_dir, args.label, args.output_dir, args.delimiter)

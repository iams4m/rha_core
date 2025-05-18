import csv

def export_to_csv(data, filename):
    with open(filename, "w", newline='') as f:
        writer = csv.writer(f)
        for val in data:
            writer.writerow([val])

def export_to_latex(data, title, filename):
    with open(filename, "w") as f:
        f.write(f"\\section*{{{title}}}\n\\begin{{itemize}}\n")
        for i, val in enumerate(data):
            f.write(f"\\item $H_{{{i}}} = {val}$\n")
        f.write("\\end{itemize}")

import  camelot.io as camelot

tables = camelot.read_pdf("data/20230707_Wykaz_funkcji_serwisow.pdf", flavour = "lattice", pages = "1" )


if tables.n > 0:
    # Iterate over each table and print it
    for i, table in enumerate(tables):
        print(f"Table {i + 1}:")
        print(table.df)  # Print the table's DataFrame representation
        print("\n" + "-" * 50 + "\n")  # Separator between tables
        table.df.to_html('extracted_table.html')
else:
    print("No tables found in the PDF.")

import fitz  # PyMuPDF


# # Open the PDF file
# doc = fitz.open("data/20230707_Wykaz_funkcji_serwisow.pdf")
# for page_num in range(1):
#     page = doc[page_num]
#     blocks = page.get_text("blocks")  # Extract blocks of text

#     for block in blocks:
#         text = block[4]
#         if "\t" in text or len(text.splitlines()) > 2:
#             print("Likely a table structure:", text)
#         else:
#             print("Plain text:", text)
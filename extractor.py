import camelot.io as camelot
import fitz  # PyMuPDF

# Define the PDF path
pdf_path = "data/20230707_Wykaz_funkcji_serwisow.pdf"

# Open the PDF with PyMuPDF
doc = fitz.open(pdf_path)

# Loop through each page to extract tables and locate their position
for page_num in range(len(doc)):
    print(f"Processing page {page_num + 1}...")
    page = doc[page_num]
    
    # Step 1: Extract tables with Camelot
    tables = camelot.read_pdf(pdf_path, flavor="stream", pages=str(page_num + 1))
    
    if tables:
        for i, table in enumerate(tables):
            # Get the text content of the table
            table_text = "\n".join(["\t".join(row) for row in table.df.values])

            # Step 2: Extract text blocks with positions using PyMuPDF
            blocks = page.get_text("blocks")
            
            # Identify the block that contains the start and end text of the table
            start_block, end_block = None, None
            for block in blocks:
                x0, y0, x1, y1, block_text = block
                if table_text.startswith(block_text.strip()):
                    start_block = (x0, y0, x1, y1, block_text)
                if table_text.endswith(block_text.strip()):
                    end_block = (x0, y0, x1, y1, block_text)
            
            # Display the found table and its position
            print(f"Table {i + 1} on Page {page_num + 1}:")
            print("Content:\n", table_text)
            if start_block and end_block:
                print(f"Starts at block: {start_block[4]} with coordinates: ({start_block[0]}, {start_block[1]})")
                print(f"Ends at block: {end_block[4]} with coordinates: ({end_block[2]}, {end_block[3]})")
            else:
                print("Could not locate exact start or end position for this table.")
    else:
        print(f"No tables found on page {page_num + 1}.")

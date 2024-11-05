# Re-attempting extraction with a stricter focus on filtering out table-like structures
import fitz
pdf_path = "data/20230707_Wykaz_funkcji_serwisow.pdf"
# Open the PDF file again for refined extraction
document = fitz.open(pdf_path)

# Initialize an empty list to collect non-tabular text blocks
filtered_text = ""

for page_num in range(document.page_count):
    page = document[page_num]
    # Extract text blocks with coordinates
    blocks = page.get_text("blocks")
    
    for block in blocks:
        text = block[4].strip()
        # Basic filtering to exclude blocks that appear like table headers or entries
        # Here, we skip blocks with mostly single-character columns or lines with repetitive structures like "X"
        if not all(len(word) <= 2 for word in text.split()):
            filtered_text += text + "\n\n"
        print()
print(filtered_text[0:1000])
document.close()

# Display the filtered non-tabular text content (first 2000 characters as a snippet)

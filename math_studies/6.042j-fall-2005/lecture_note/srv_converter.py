from __future__ import annotations

import importlib
from pathlib import Path


class SRVConverter:
    def __init__(self, input_dir: Path, output_dir: Path) -> None:
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _extract_pdf_text(pdf_path: Path) -> str:
        """Extract plain text from a PDF file page-by-page."""
        try:
            pypdf = importlib.import_module("pypdf")
        except ImportError as exc:
            raise ImportError(
                "Missing dependency 'pypdf'. Install it with: pip install pypdf"
            ) from exc

        PdfReader = getattr(pypdf, "PdfReader")
        reader = PdfReader(str(pdf_path))
        parts: list[str] = []

        for index, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            text = text.strip()
            parts.append(f"## Page {index}\n\n{text}\n")

        return "\n".join(parts).strip() + "\n"

    def convert_pdf_to_markdown(self, pdf_path: Path) -> Path:
        """Convert one PDF file to a Markdown file with the same stem."""
        if pdf_path.suffix.lower() != ".pdf":
            raise ValueError(f"Expected a .pdf file, got: {pdf_path}")

        markdown_path = self.output_dir / f"{pdf_path.stem}.md"
        markdown_text = self._extract_pdf_text(pdf_path)
        markdown_path.write_text(markdown_text, encoding="utf-8")
        return markdown_path

    def convert_all_pdfs(self) -> list[Path]:
        """Convert all PDF files in input_dir into output_dir."""
        pdf_files = sorted(self.input_dir.glob("*.pdf"))
        outputs: list[Path] = []

        for pdf_file in pdf_files:
            outputs.append(self.convert_pdf_to_markdown(pdf_file))

        return outputs


if __name__ == "__main__":
    base_dir = Path(__file__).parent
    input_pdf_dir = base_dir / "pdf"
    output_markdown_dir = base_dir / "markdown"

    converter = SRVConverter(input_dir=input_pdf_dir, output_dir=output_markdown_dir)
    converted_files = converter.convert_all_pdfs()

    print(f"Converted {len(converted_files)} file(s).")
    for file in converted_files:
        print(file)
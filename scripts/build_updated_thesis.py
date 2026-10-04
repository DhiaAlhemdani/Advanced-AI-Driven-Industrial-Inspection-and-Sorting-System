#!/usr/bin/env python3
"""Build an annotated thesis edition with updated metrics and firmware parameters.

The original PDF is never modified. Install the optional tools first:

    python -m pip install 'pypdf>=5,<7' 'reportlab>=4,<5'
"""

from __future__ import annotations

import argparse
import hashlib
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

EXPECTED_SOURCE_SHA256 = "8dee0b3dbc63031ca2e850f971fe0cfc85b40e3f688d5b190fabdf36dd1d03ed"
REVISION_DATE = "2026-10-04"

# PDF page numbers (not zero-based indices). Original printed page numbers differ.
METRIC_PAGES = {5, 6, 61, 115, 121, 122, 123, 141, 142, 144, 145}
FIRMWARE_PAGES = {
    5,
    41,
    49,
    61,
    81,
    82,
    83,
    84,
    85,
    86,
    106,
    107,
    111,
    112,
    113,
    114,
    120,
    123,
    142,
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def revision_label(page_number: int) -> tuple[str, colors.Color] | None:
    metric = page_number in METRIC_PAGES
    firmware = page_number in FIRMWARE_PAGES
    if metric and firmware:
        return "METRICS + FIRMWARE UPDATED — SEE APPENDED TECHNICAL NOTES", colors.HexColor("#6B3FA0")
    if metric:
        return "METRICS UPDATED — SEE APPENDED TECHNICAL NOTES", colors.HexColor("#A61B1B")
    if firmware:
        return "FIRMWARE SPECIFICATION UPDATED — SEE APPENDED TECHNICAL NOTES", colors.HexColor("#174A7E")
    return None


def draw_overlay(draw: canvas.Canvas, width: float, height: float, page_number: int) -> None:
    """Draw the visible revision marks for one source page."""

    label = revision_label(page_number)
    if page_number == 1:
        draw.setFillColor(colors.HexColor("#17324D"))
        draw.rect(0, height - 10 * mm, width, 10 * mm, fill=1, stroke=0)
        draw.setFillColor(colors.white)
        draw.setFont("Helvetica-Bold", 8.2)
        draw.drawCentredString(width / 2, height - 4.2 * mm, "UPDATED METRICS AND FIRMWARE EDITION — 2026-10-04")
        draw.setFont("Helvetica", 6.3)
        draw.drawCentredString(
            width / 2,
            height - 7.5 * mm,
            "Original preserved separately; technical update follows source page 153.",
        )

    if label is not None:
        message, color = label
        draw.setFillColor(color)
        draw.rect(0, height - 8.5 * mm, width, 8.5 * mm, fill=1, stroke=0)
        draw.setFillColor(colors.white)
        draw.setFont("Helvetica-Bold", 6.8)
        draw.drawCentredString(width / 2, height - 5.4 * mm, message)
        draw.setFillColor(color)
        draw.setFont("Helvetica-Bold", 5.8)
        draw.drawRightString(width - 7 * mm, 5.5 * mm, f"REVISED {REVISION_DATE} · SOURCE PDF PAGE {page_number}")


def overlay_pdf(page_sizes: list[tuple[float, float]]) -> PdfReader:
    """Create one overlay document to avoid cross-reader PDF object collisions."""

    stream = BytesIO()
    draw = canvas.Canvas(stream, pagesize=page_sizes[0])
    draw.setTitle("Updated thesis annotations")
    for page_number, (width, height) in enumerate(page_sizes, start=1):
        draw.setPageSize((width, height))
        draw_overlay(draw, width, height, page_number)
        draw.showPage()
    draw.save()
    stream.seek(0)
    return PdfReader(stream)


def appendix_pdf() -> PdfReader:
    stream = BytesIO()
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="AppendixTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=24,
            textColor=colors.HexColor("#17324D"),
            alignment=TA_CENTER,
            spaceAfter=10 * mm,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallNote",
            parent=styles["BodyText"],
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#444444"),
        )
    )
    styles["Heading1"].textColor = colors.HexColor("#17324D")
    styles["Heading2"].textColor = colors.HexColor("#174A7E")
    styles["BodyText"].leading = 14

    def footer(draw: canvas.Canvas, document: SimpleDocTemplate) -> None:
        draw.saveState()
        draw.setStrokeColor(colors.HexColor("#B8C4CF"))
        draw.line(18 * mm, 14 * mm, A4[0] - 18 * mm, 14 * mm)
        draw.setFont("Helvetica", 7)
        draw.setFillColor(colors.HexColor("#52616B"))
        draw.drawString(18 * mm, 10 * mm, "Metrics and Firmware Technical Update")
        draw.drawRightString(A4[0] - 18 * mm, 10 * mm, f"Appendix page {document.page}")
        draw.restoreState()

    doc = SimpleDocTemplate(
        stream,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=17 * mm,
        bottomMargin=19 * mm,
        title="Metrics and Firmware Technical Update",
        author="Deiaa Ahmed Abdo Lootf",
        subject="Benchmark metrics, sorting counts, and firmware parameters",
    )
    story: list[object] = []

    def para(text: str, style: str = "BodyText") -> None:
        story.append(Paragraph(text, styles[style]))
        story.append(Spacer(1, 2.4 * mm))

    def heading(text: str, level: int = 1) -> None:
        story.append(Paragraph(text, styles[f"Heading{level}"]))

    def table(data: list[list[str]], widths: list[float]) -> None:
        rendered = [[Paragraph(str(cell), styles["SmallNote"]) for cell in row] for row in data]
        item = Table(rendered, colWidths=widths, repeatRows=1, hAlign="LEFT")
        item.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17324D")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#AAB7C4")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 4),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F2F5F7")]),
                ]
            )
        )
        story.append(item)
        story.append(Spacer(1, 4 * mm))

    story.append(Spacer(1, 10 * mm))
    story.append(Paragraph("Metrics and Firmware Technical Update", styles["AppendixTitle"]))
    para("<b>Revision date:</b> 2026-10-04", "BodyText")
    para(
        "This appendix records the benchmark metrics, count-derived sorting rates, and uploaded firmware specification for this edition of "
        "<i>Development of an Intelligent System for Inspection and Sorting Using Computer Vision and Predictive Maintenance</i>. "
        "Every original thesis page is retained, and visible page banners point to these technical notes.",
    )
    para(
        "The original PDF remains available as the historical edition. This update is based on the uploaded source artifacts and does "
        "not represent a new model evaluation or physical hardware retest.",
    )
    heading("Update scope", 1)
    para(
        "Detection metrics, bottle-level inspection, physical routing, timing, and predictive-maintenance simulation are documented as "
        "distinct measurement layers. Each value is labeled with its source, selection rule, denominator, or timing boundary where available.",
    )
    heading("Controlling source artifacts", 2)
    table(
        [
            ["Artifact", "SHA-256", "Role"],
            ["Original thesis", EXPECTED_SOURCE_SHA256, "Historical narrative and aggregate trial claims"],
            ["firmware/sketch_may1a.ino", "c17604dd7799e661291d39fc6f1a9a0e1975ce819ba6ff027c7496b8d31b4c77", "Canonical firmware specification for this revision"],
            ["kaggle/benchmarks/results.csv", "16c19565ecda02816316ea25c7102763e88bb9638a29c2daf7b0bb869270ac57", "Uploaded detector training history"],
        ],
        [34 * mm, 75 * mm, 50 * mm],
    )

    story.append(PageBreak())
    heading("A. Detection-result presentation", 1)
    para(
        "The uploaded CSV records Ultralytics box-detection metrics. These compare predicted boxes with annotations and are listed "
        "independently from bottle-level inspection and physical routing. The attached training configuration identifies a "
        "yolov8l-worldv2 model path; the thesis and notebook also document YOLO-World/YOLOv11 components.",
    )
    table(
        [
            ["Source / selection", "Precision", "Recall", "mAP@0.50", "mAP@0.50:0.95"],
            ["Uploaded CSV, final epoch 121", "97.367%", "98.584%", "99.414%", "94.317%"],
            ["Best mAP@0.50:0.95 row, epoch 117", "95.780%", "98.816%", "99.389%", "94.441%"],
            ["Quick Inference, 24 images / 83 instances", "98.1%", "95.7%", "96.47%", "92.12%"],
        ],
        [55 * mm, 25 * mm, 24 * mm, 26 * mm, 29 * mm],
    )
    para(
        "Peak recall is 100%, first reached at epoch 55. Final-row, selected-checkpoint, peak, and Quick Inference values are identified "
        "by their source and selection context.",
    )
    heading("Runtime inspection scope", 2)
    para(
        "The thesis records an 85–95% inspection/classification range for integrated runtime operation. It is listed independently from "
        "annotation-based box metrics and physical route rates.",
    )

    heading("B. Physical sorting counts and calculated rates", 1)
    table(
        [
            ["Scenario", "Tested", "Routed count", "Count-derived rate"],
            ["SC-01 compliant / pass", "100", "100", "100.00%"],
            ["SC-02 missing cap / rework", "40", "40", "100.00%"],
            ["SC-03 missing label / rework", "35", "35", "100.00%"],
            ["SC-04 label skew / rework", "35", "35", "100.00%"],
            ["SC-05 fluid defect / scrap", "35", "20", "57.14%"],
            ["Overall", "245", "230", "93.88%"],
        ],
        [67 * mm, 25 * mm, 32 * mm, 35 * mm],
    )
    para(
        "The rates are calculated directly from the published scenario counts. An item-level route ledger is required for independent "
        "physical-trial reproduction.",
    )

    story.append(PageBreak())
    heading("C. Canonical firmware parameters for this edition", 1)
    para(
        "The uploaded sketch is the canonical current firmware specification for this edition. A dated board, build, wiring, and trial "
        "record remains necessary for physical-test reproduction.",
    )
    table(
        [
            ["Parameter", "Canonical uploaded-sketch value"],
            ["Serial", "Serial.begin(9600); command and diagnostics share this stream"],
            ["Commands", "A and B only; pass sends no command"],
            ["Servo A", "Pin 9; rest 35 degrees; active 0 degrees; comment: reprocess"],
            ["Servo B", "Pin 10; rest 0 degrees; active 35 degrees; comment: defected"],
            ["Proximity inputs", "Pins 2 and 3; plain INPUT; active when LOW"],
            ["Execution model", "Polling in loop(); no ISR is defined"],
            ["Dwell", "HOLD_TIME = 500 ms"],
            ["Queues", "Independent circular queues, ten characters per route"],
            ["Trigger", "Command becomes pending; corresponding low sensor reading starts motion"],
            ["Diagnostics", "Sensor levels printed approximately once per second"],
        ],
        [46 * mm, 113 * mm],
    )
    heading("Implementation scope", 2)
    para(
        "The sketch implements the documented A/B serial commands, proximity-gated servo motion, independent route queues, and sensor "
        "diagnostics. Acknowledgements, item IDs, framing checksums, pending-command timeouts, queue-overflow reports, distance-based "
        "flight timers, conveyor control, MQTT, and an S command are outside this sketch's implementation scope.",
    )

    story.append(PageBreak())
    heading("D. Timing interpretation", 1)
    table(
        [
            ["Value", "Measurement boundary"],
            ["20.6 ms", "Thesis host-processing sum: 4.2 ms capture + 12.8 ms inference + 3.5 ms OpenCV + 0.1 ms serial."],
            ["2–4 seconds", "Thesis field-of-view-entry to completed-deflection range."],
            ["500 ms", "Programmed active hold in the uploaded sketch after a pending command is sensor-triggered."],
        ],
        [36 * mm, 123 * mm],
    )
    heading("E. Predictive-maintenance scope", 1)
    para(
        "The thesis explicitly uses a Virtual Sensing Simulation Protocol. Its health scores, failure probabilities, dashboard states, "
        "and emergency-state calculations demonstrate formula and interface behavior. They are not predictive accuracy, false-alert rate, "
        "remaining useful life, or field reliability.",
    )
    heading("F. Required evidence for a future verified edition", 1)
    para(
        "A verified edition requires the exact model weights and environment, immutable dataset split, original notebook export, evaluator "
        "command, item-level inspection and route ledger, synchronized timing trace, board/wiring revision, host revision, flashed firmware "
        "or binary checksum, and dated hardware trial. Training data, labels, annotations, notebook, and weights remain external on Kaggle.",
    )

    heading("G. Annotated source-page index", 1)
    para(
        "Metric update banners appear on source PDF pages: " + ", ".join(str(p) for p in sorted(METRIC_PAGES)) + ".",
        "SmallNote",
    )
    para(
        "Firmware banners appear on source PDF pages: " + ", ".join(str(p) for p in sorted(FIRMWARE_PAGES)) + ".",
        "SmallNote",
    )
    para(
        "For the complete machine-readable audit, see README.md, docs/hardware.md, docs/validation.md, and "
        "results/kaggle-benchmark-snapshot.md in the repository.",
        "SmallNote",
    )

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    stream.seek(0)
    return PdfReader(stream)


def build(source: Path, output: Path) -> None:
    actual_hash = sha256(source)
    if actual_hash != EXPECTED_SOURCE_SHA256:
        raise ValueError(
            f"unexpected source thesis hash: expected {EXPECTED_SOURCE_SHA256}, got {actual_hash}"
        )

    reader = PdfReader(source)
    if len(reader.pages) != 153:
        raise ValueError(f"expected 153 source pages, found {len(reader.pages)}")

    # Clone first, then annotate the writer's page objects. Adding individually
    # modified source pages can trigger pypdf's translation cache for shared Word
    # PDF resources and silently omit some merged overlays.
    writer = PdfWriter(clone_from=reader)
    overlays = overlay_pdf(
        [(float(page.mediabox.width), float(page.mediabox.height)) for page in reader.pages]
    )
    for index, overlay in enumerate(overlays.pages):
        writer.pages[index].merge_page(overlay, over=True)

    appendix = appendix_pdf()
    appendix_start = len(writer.pages)
    for page in appendix.pages:
        writer.add_page(page)

    writer.add_metadata(
        {
            "/Title": "Development of an Intelligent System for Inspection and Sorting — Updated Metrics and Firmware Edition",
            "/Author": "Deiaa Ahmed Abdo Lootf",
            "/Subject": "Updated benchmark metrics, sorting counts, and uploaded firmware parameters",
            "/Keywords": "industrial inspection, YOLO, Arduino, benchmark metrics, firmware parameters",
            "/RevisionDate": REVISION_DATE,
            "/OriginalSHA256": EXPECTED_SOURCE_SHA256,
        }
    )
    writer.add_outline_item("Metrics and Firmware Technical Update", appendix_start)

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as handle:
        writer.write(handle)

    print(f"wrote: {output}")
    print(f"pages: {len(writer.pages)} ({len(reader.pages)} original + {len(appendix.pages)} appendix)")
    print(f"sha256: {sha256(output)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("docs/Project Research.pdf"))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/Project Research - Updated Metrics and Firmware.pdf"),
    )
    args = parser.parse_args(argv)
    build(args.source, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

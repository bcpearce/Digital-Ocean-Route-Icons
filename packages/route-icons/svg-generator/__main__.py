import base64

import svg
from colour import Color


def main(event):
    color = Color(event.get("color", "#808080"))
    stroke_color = Color(event.get("color", "#808080"))
    stroke_color.set_saturation(stroke_color.get_saturation() * 0.8)
    stroke_color.set_luminance(stroke_color.get_luminance() * 1.1)

    text = event.get("text", "")
    text_color = Color(event.get("text_color", "white"))
    text_stroke_color = Color(event.get("text_color", "white"))
    text_stroke_color.set_saturation(stroke_color.get_saturation() * 1.2)
    text_stroke_color.set_luminance(text_stroke_color.get_luminance() * 0.8)

    canvas = svg.SVG(
        width=int(event.get("width", 75)),
        height=int(event.get("height", 75)),
        elements=[
            svg.Rect(
                x=5,
                y=15,
                height=42,
                width=65,
                fill=color,
                stroke=stroke_color,
                stroke_width=2,
                rx=5,
            ),
            svg.Style(
                text=f".vignelli{{font: bold 31px Helvetica; fill: {text_color}}}"  # noqa E501
            ),
            svg.Text(
                x="50%",
                y="50%",
                text_anchor="middle",
                dominant_baseline="middle",
                class_=["vignelli"],
                text=text,
                color=text_color,
                stroke=text_stroke_color,
                stroke_width=1,
            ),
        ],
    )
    out = base64.b64encode(canvas.as_str().encode("utf-8")).decode("utf-8")
    return {"body": out, "headers": {"Content-Type": "image/svg+xml"}}

import os
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fpdf import FPDF

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"story": None, "idea": ""}
    )


@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, idea: str = Form(...)):

    if not idea.strip():
        story = "Please enter a comic idea."
    else:
        story = f"""Title: The Amazing Comic

Characters: A Student and a Robot

Panel 1:
The student says, "I have a great comic idea!"

Panel 2:
The student asks the AI robot to create a comic.

Panel 3:
The student says, "{idea}"

Panel 4:
The robot creates a funny story and everyone starts laughing!

Ending:
The student and robot become best friends.

Thank you for using ComicCraft!"""

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"story": story, "idea": idea}
    )


@app.post("/download")
async def download_pdf(idea: str = Form(...)):

    pdf = FPDF()

    # Comic images
    for i in range(1, 5):

        image_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "static",
            "images",
            f"panel{i}.png"
        )

        if os.path.exists(image_path):
            pdf.add_page()
            pdf.image(image_path, x=10, y=10, w=190)

    # Story
    pdf.add_page()

    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 15, "ComicCraft", ln=True, align="C")

    pdf.ln(10)

    pdf.set_font("Arial", "", 12)

    story = f"""ComicCraft - AI Comic Story

Idea:
{idea}

Panel 1:
The student gets a funny idea.

Panel 2:
The student meets an AI robot.

Panel 3:
The robot creates a funny comic.

Panel 4:
Everyone laughs and enjoys the story!

Ending:
The student and robot become best friends.
"""

    pdf.multi_cell(0, 8, story)

    file_path = "ComicCraft_Story.pdf"
    pdf.output(file_path)

    return FileResponse(
        file_path,
        media_type="application/pdf",
        filename="ComicCraft_Story.pdf"
    )
    print("PANEL 1:", os.path.exists("static/images/comic_panels_916/panel1.png"))
print("PANEL 2:", os.path.exists("static/images/comic_panels_916/panel2.png"))
print("PANEL 3:", os.path.exists("static/images/comic_panels_916/panel3.png"))
print("PANEL 4:", os.path.exists("static/images/comic_panels_916/panel4.png"))
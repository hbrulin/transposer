import const

def generate_html(title, key, l, r):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Two Column Layout</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 50px;
            }}
            .title-section {{
                font-size: 2em;
                font-weight: bold;
                margin-left: 20px;  /* Title on the left */
                margin-bottom: 20px;
                align-self: flex-start;
            }}
            .subtitle-section {{
                font-size: 1.5em;
                margin-left: 20px;  /* Subtitle on the left */
                margin-bottom: 20px;
                align-self: flex-start;
            }}
            .container {{
                display: flex;
                justify-content: center;  /* Center the table */
                width: 60%;  /* Adjust width of the table */
            }}
            .column {{
                padding: 20px;
                width: 200px;
            }}
            .column1 {{
                color: blue;
                background-color: #f0f0f0;
            }}
            .column2 {{
                color: red;
                background-color: #e0e0e0;
            }}
            .info {{
                color: black;
            }}
        </style>
    </head>
    <body>
        <div class="title-section">{title}</div>
        <div class="subtitle-section">{key}</div>
        <div class="container">
            <div class="column column1">
    """
    
    # Populate first column
    for i in l:
        tmp = " ".join(map(str, i))
        row_class = "info" if tmp[0] not in const.note_to_midi else ""
        html_content += f"<p class='{row_class}'>{tmp}</p>\n"
    
    html_content += """
            </div>
            <div class="column column2">
    """
    
    # Populate second column
    for i in r:
        tmp = " ".join(map(str, i))
        row_class = "info" if tmp[0] not in const.note_to_midi else ""
        html_content += f"<p class='{row_class}'>{tmp}</p>\n"
    
    html_content += """
            </div>
        </div>
    </body>
    </html>
    """
    
    # Save the file
    filename = "output.html"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    return filename
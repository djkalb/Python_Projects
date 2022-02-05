import webbrowser
with open("sale.html", 'w') as f:
    f.write("""
    <html>

        <body>

            <h1>

                Stay tuned for our amazing summer sale!

            </h1>

            

        </body>

    </html>""")
    
f.close()

webbrowser.open_new("sale.html")

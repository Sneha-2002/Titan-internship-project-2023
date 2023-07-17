from flask import Flask, render_template
import pandas as pd

app=Flask(__name__)

@app.route('/')
def index():
    df=pd.read_excel('data.xlsx')

    table_html = df.to_html(index=False)
    return render_template('Machine.html',table=table_html)
if __name__ == '__main__':
    app.run(debug=True)
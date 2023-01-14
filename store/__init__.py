from flask import Flask, json, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY']='ghyt45rd-ohtf456780u-ijgjhjugde322'

from store import routes
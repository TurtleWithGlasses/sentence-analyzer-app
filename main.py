import PySimpleGUI as sg
from nltk.sentiment import SentimentIntensityAnalyzer

sg.theme("DarkTeal10")

analyzer = SentimentIntensityAnalyzer()
label1 = sg.Text("Type in a sentence below")
input_box = sg.InputText(tooltip="Enter: ")
button = sg.Button("Execute", size=(10,1), mouseover_colors="gray")
label2 = sg.Text("")

layout=[[label1],
       [input_box, button],
       [label2]],

window = sg.Window("My App", layout, font=("Arial", 20))

negativity = []
positivity = []

def get_sentence(sentence):
    score = analyzer.polarity_scores(sentence)
    pos_score = score["pos"]
    neg_score = score["neg"]
    positivity.append(pos_score)
    negativity.append(neg_score)
    label2.update(f"Negativity: {neg_score}, Positivity: {pos_score}")

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Execute":
        get_sentence(values[0])

window.close()
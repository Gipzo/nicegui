#!/usr/bin/env python3
from nice_gui import ui
from datetime import datetime
from matplotlib import pyplot as plt

ui.label('Hello world!')

ui.button('Click me!', on_click=lambda: ui.label('Yes!'))

with ui.card():
    with ui.row():
        ui.label('A')
        ui.label('B')
        with ui.column():
            ui.label('C1')
            ui.label('C2')
            ui.label('C3')

with ui.row():
    ui.label('Time:')
    time = ui.label()
    ui.timer(0.1, lambda: time.set_text(datetime.now().strftime("%X")))

with ui.plot():
    plt.title('Some plot')
    plt.plot(range(10), [x**2 for x in range(10)])

ui.run()

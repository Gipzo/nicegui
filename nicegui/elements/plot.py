from nicegui.elements.element import Element
import justpy as jp
import matplotlib.pyplot as plt
from .element import Element

class Plot(Element):

    def __init__(self, close: bool = True, **kwargs):
        """Plot

        Create a context to configure a `Matplotlib <https://matplotlib.org/>`_ plot

        :param close: weather the figure should be closed after exiting the context; set to False if you want to update it later, default is True
        """

        self.close = close
        self.fig = plt.figure(**kwargs)

        view = jp.Matplotlib()
        view.set_figure(self.fig)

        super().__init__(view, '')

    def __enter__(self):

        plt.figure(self.fig)

        return self

    def __exit__(self, *_):

        self.view.set_figure(plt.gcf())

        if self.close:
            plt.close(self.fig)

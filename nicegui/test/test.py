import justpy as jp
from nicegui.elements.element import Element
from nicegui.globals import page_stack


def _find(view: jp.HTMLBaseComponent, string: str) -> bool:
    for component in view.components:
        if getattr(component, 'text', None) == string:
            return True
        if getattr(component, 'label', None) == string:
            return True
        if _find(component, string):
            return True
    return False


def should_see(string: str) -> None:
    page = page_stack[-1]
    assert _find(page.view, string)


def click(element: Element) -> None:
    getattr(element.view, 'on_click')({})

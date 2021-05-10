"""
This type stub file was generated by pyright.
"""

from abc import ABCMeta
from tkinter import Menubutton

"""
Tools for graphically displaying and interacting with the objects and
processing classes defined by the Toolkit.  These tools are primarily
intended to help students visualize the objects that they create.

The graphical tools are typically built using "canvas widgets", each
of which encapsulates the graphical elements and bindings used to
display a complex object on a Tkinter ``Canvas``.  For example, NLTK
defines canvas widgets for displaying trees and directed graphs, as
well as a number of simpler widgets.  These canvas widgets make it
easier to build new graphical tools and demos.  See the class
documentation for ``CanvasWidget`` for more information.

The ``nltk.draw`` module defines the abstract ``CanvasWidget`` base
class, and a number of simple canvas widgets.  The remaining canvas
widgets are defined by submodules, such as ``nltk.draw.tree``.

The ``nltk.draw`` module also defines ``CanvasFrame``, which
encapsulates a ``Canvas`` and its scrollbars.  It uses a
``ScrollWatcherWidget`` to ensure that all canvas widgets contained on
its canvas are within the scroll region.

Acknowledgements: Many of the ideas behind the canvas widget system
are derived from ``CLIG``, a Tk-based grapher for linguistic data
structures.  For more information, see the CLIG
homepage (http://www.ags.uni-sb.de/~konrad/clig.html).

"""
class CanvasWidget(metaclass=ABCMeta):
    """
    A collection of graphical elements and bindings used to display a
    complex object on a Tkinter ``Canvas``.  A canvas widget is
    responsible for managing the ``Canvas`` tags and callback bindings
    necessary to display and interact with the object.  Canvas widgets
    are often organized into hierarchies, where parent canvas widgets
    control aspects of their child widgets.

    Each canvas widget is bound to a single ``Canvas``.  This ``Canvas``
    is specified as the first argument to the ``CanvasWidget``'s
    constructor.

    Attributes.  Each canvas widget can support a variety of
    "attributes", which control how the canvas widget is displayed.
    Some typical examples attributes are ``color``, ``font``, and
    ``radius``.  Each attribute has a default value.  This default
    value can be overridden in the constructor, using keyword
    arguments of the form ``attribute=value``:

        >>> from nltk.draw.util import TextWidget
        >>> cn = TextWidget(c, 'test', color='red')

    Attribute values can also be changed after a canvas widget has
    been constructed, using the ``__setitem__`` operator:

        >>> cn['font'] = 'times'

    The current value of an attribute value can be queried using the
    ``__getitem__`` operator:

        >>> cn['color']
        red

    For a list of the attributes supported by a type of canvas widget,
    see its class documentation.

    Interaction.  The attribute ``'draggable'`` controls whether the
    user can drag a canvas widget around the canvas.  By default,
    canvas widgets are not draggable.

    ``CanvasWidget`` provides callback support for two types of user
    interaction: clicking and dragging.  The method ``bind_click``
    registers a callback function that is called whenever the canvas
    widget is clicked.  The method ``bind_drag`` registers a callback
    function that is called after the canvas widget is dragged.  If
    the user clicks or drags a canvas widget with no registered
    callback function, then the interaction event will propagate to
    its parent.  For each canvas widget, only one callback function
    may be registered for an interaction event.  Callback functions
    can be deregistered with the ``unbind_click`` and ``unbind_drag``
    methods.

    Subclassing.  ``CanvasWidget`` is an abstract class.  Subclasses
    are required to implement the following methods:

      - ``__init__``: Builds a new canvas widget.  It must perform the
        following three tasks (in order):
          - Create any new graphical elements.
          - Call ``_add_child_widget`` on each child widget.
          - Call the ``CanvasWidget`` constructor.
      - ``_tags``: Returns a list of the canvas tags for all graphical
        elements managed by this canvas widget, not including
        graphical elements managed by its child widgets.
      - ``_manage``: Arranges the child widgets of this canvas widget.
        This is typically only called when the canvas widget is
        created.
      - ``_update``: Update this canvas widget in response to a
        change in a single child.

    For a ``CanvasWidget`` with no child widgets, the default
    definitions for ``_manage`` and ``_update`` may be used.

    If a subclass defines any attributes, then it should implement
    ``__getitem__`` and ``__setitem__``.  If either of these methods is
    called with an unknown attribute, then they should propagate the
    request to ``CanvasWidget``.

    Most subclasses implement a number of additional methods that
    modify the ``CanvasWidget`` in some way.  These methods must call
    ``parent.update(self)`` after making any changes to the canvas
    widget's graphical elements.  The canvas widget must also call
    ``parent.update(self)`` after changing any attribute value that
    affects the shape or position of the canvas widget's graphical
    elements.

    :type __canvas: Tkinter.Canvas
    :ivar __canvas: This ``CanvasWidget``'s canvas.

    :type __parent: CanvasWidget or None
    :ivar __parent: This ``CanvasWidget``'s hierarchical parent widget.
    :type __children: list(CanvasWidget)
    :ivar __children: This ``CanvasWidget``'s hierarchical child widgets.

    :type __updating: bool
    :ivar __updating: Is this canvas widget currently performing an
        update?  If it is, then it will ignore any new update requests
        from child widgets.

    :type __draggable: bool
    :ivar __draggable: Is this canvas widget draggable?
    :type __press: event
    :ivar __press: The ButtonPress event that we're currently handling.
    :type __drag_x: int
    :ivar __drag_x: Where it's been moved to (to find dx)
    :type __drag_y: int
    :ivar __drag_y: Where it's been moved to (to find dy)
    :type __callbacks: dictionary
    :ivar __callbacks: Registered callbacks.  Currently, four keys are
        used: ``1``, ``2``, ``3``, and ``'drag'``.  The values are
        callback functions.  Each callback function takes a single
        argument, which is the ``CanvasWidget`` that triggered the
        callback.
    """
    def __init__(self, canvas, parent=..., **attribs) -> None:
        """
        Create a new canvas widget.  This constructor should only be
        called by subclass constructors; and it should be called only
        "after" the subclass has constructed all graphical canvas
        objects and registered all child widgets.

        :param canvas: This canvas widget's canvas.
        :type canvas: Tkinter.Canvas
        :param parent: This canvas widget's hierarchical parent.
        :type parent: CanvasWidget
        :param attribs: The new canvas widget's attributes.
        """
        ...
    
    def bbox(self):
        """
        :return: A bounding box for this ``CanvasWidget``. The bounding
            box is a tuple of four coordinates, *(xmin, ymin, xmax, ymax)*,
            for a rectangle which encloses all of the canvas
            widget's graphical elements.  Bounding box coordinates are
            specified with respect to the coordinate space of the ``Canvas``.
        :rtype: tuple(int, int, int, int)
        """
        ...
    
    def width(self):
        """
        :return: The width of this canvas widget's bounding box, in
            its ``Canvas``'s coordinate space.
        :rtype: int
        """
        ...
    
    def height(self):
        """
        :return: The height of this canvas widget's bounding box, in
            its ``Canvas``'s coordinate space.
        :rtype: int
        """
        ...
    
    def parent(self):
        """
        :return: The hierarchical parent of this canvas widget.
            ``self`` is considered a subpart of its parent for
            purposes of user interaction.
        :rtype: CanvasWidget or None
        """
        ...
    
    def child_widgets(self):
        """
        :return: A list of the hierarchical children of this canvas
            widget.  These children are considered part of ``self``
            for purposes of user interaction.
        :rtype: list of CanvasWidget
        """
        ...
    
    def canvas(self):
        """
        :return: The canvas that this canvas widget is bound to.
        :rtype: Tkinter.Canvas
        """
        ...
    
    def move(self, dx, dy):
        """
        Move this canvas widget by a given distance.  In particular,
        shift the canvas widget right by ``dx`` pixels, and down by
        ``dy`` pixels.  Both ``dx`` and ``dy`` may be negative, resulting
        in leftward or upward movement.

        :type dx: int
        :param dx: The number of pixels to move this canvas widget
            rightwards.
        :type dy: int
        :param dy: The number of pixels to move this canvas widget
            downwards.
        :rtype: None
        """
        ...
    
    def moveto(self, x, y, anchor=...):
        """
        Move this canvas widget to the given location.  In particular,
        shift the canvas widget such that the corner or side of the
        bounding box specified by ``anchor`` is at location (``x``,
        ``y``).

        :param x,y: The location that the canvas widget should be moved
            to.
        :param anchor: The corner or side of the canvas widget that
            should be moved to the specified location.  ``'N'``
            specifies the top center; ``'NE'`` specifies the top right
            corner; etc.
        """
        ...
    
    def destroy(self):
        """
        Remove this ``CanvasWidget`` from its ``Canvas``.  After a
        ``CanvasWidget`` has been destroyed, it should not be accessed.

        Note that you only need to destroy a top-level
        ``CanvasWidget``; its child widgets will be destroyed
        automatically.  If you destroy a non-top-level
        ``CanvasWidget``, then the entire top-level widget will be
        destroyed.

        :raise ValueError: if this ``CanvasWidget`` has a parent.
        :rtype: None
        """
        ...
    
    def update(self, child):
        """
        Update the graphical display of this canvas widget, and all of
        its ancestors, in response to a change in one of this canvas
        widget's children.

        :param child: The child widget that changed.
        :type child: CanvasWidget
        """
        ...
    
    def manage(self):
        """
        Arrange this canvas widget and all of its descendants.

        :rtype: None
        """
        ...
    
    def tags(self):
        """
        :return: a list of the canvas tags for all graphical
            elements managed by this canvas widget, including
            graphical elements managed by its child widgets.
        :rtype: list of int
        """
        ...
    
    def __setitem__(self, attr, value):
        """
        Set the value of the attribute ``attr`` to ``value``.  See the
        class documentation for a list of attributes supported by this
        canvas widget.

        :rtype: None
        """
        ...
    
    def __getitem__(self, attr):
        """
        :return: the value of the attribute ``attr``.  See the class
            documentation for a list of attributes supported by this
            canvas widget.
        :rtype: (any)
        """
        ...
    
    def __repr__(self):
        """
        :return: a string representation of this canvas widget.
        :rtype: str
        """
        ...
    
    def hide(self):
        """
        Temporarily hide this canvas widget.

        :rtype: None
        """
        ...
    
    def show(self):
        """
        Show a hidden canvas widget.

        :rtype: None
        """
        ...
    
    def hidden(self):
        """
        :return: True if this canvas widget is hidden.
        :rtype: bool
        """
        ...
    
    def bind_click(self, callback, button=...):
        """
        Register a new callback that will be called whenever this
        ``CanvasWidget`` is clicked on.

        :type callback: function
        :param callback: The callback function that will be called
            whenever this ``CanvasWidget`` is clicked.  This function
            will be called with this ``CanvasWidget`` as its argument.
        :type button: int
        :param button: Which button the user should use to click on
            this ``CanvasWidget``.  Typically, this should be 1 (left
            button), 3 (right button), or 2 (middle button).
        """
        ...
    
    def bind_drag(self, callback):
        """
        Register a new callback that will be called after this
        ``CanvasWidget`` is dragged.  This implicitly makes this
        ``CanvasWidget`` draggable.

        :type callback: function
        :param callback: The callback function that will be called
            whenever this ``CanvasWidget`` is clicked.  This function
            will be called with this ``CanvasWidget`` as its argument.
        """
        ...
    
    def unbind_click(self, button=...):
        """
        Remove a callback that was registered with ``bind_click``.

        :type button: int
        :param button: Which button the user should use to click on
            this ``CanvasWidget``.  Typically, this should be 1 (left
            button), 3 (right button), or 2 (middle button).
        """
        ...
    
    def unbind_drag(self):
        """
        Remove a callback that was registered with ``bind_drag``.
        """
        ...
    


class TextWidget(CanvasWidget):
    """
    A canvas widget that displays a single string of text.

    Attributes:
      - ``color``: the color of the text.
      - ``font``: the font used to display the text.
      - ``justify``: justification for multi-line texts.  Valid values
        are ``left``, ``center``, and ``right``.
      - ``width``: the width of the text.  If the text is wider than
        this width, it will be line-wrapped at whitespace.
      - ``draggable``: whether the text can be dragged by the user.
    """
    def __init__(self, canvas, text, **attribs) -> None:
        """
        Create a new text widget.

        :type canvas: Tkinter.Canvas
        :param canvas: This canvas widget's canvas.
        :type text: str
        :param text: The string of text to display.
        :param attribs: The new canvas widget's attributes.
        """
        ...
    
    def __setitem__(self, attr, value):
        ...
    
    def __getitem__(self, attr):
        ...
    
    def text(self):
        """
        :return: The text displayed by this text widget.
        :rtype: str
        """
        ...
    
    def set_text(self, text):
        """
        Change the text that is displayed by this text widget.

        :type text: str
        :param text: The string of text to display.
        :rtype: None
        """
        ...
    
    def __repr__(self):
        ...
    


class SymbolWidget(TextWidget):
    """
    A canvas widget that displays special symbols, such as the
    negation sign and the exists operator.  Symbols are specified by
    name.  Currently, the following symbol names are defined: ``neg``,
    ``disj``, ``conj``, ``lambda``, ``merge``, ``forall``, ``exists``,
    ``subseteq``, ``subset``, ``notsubset``, ``emptyset``, ``imp``,
    ``rightarrow``, ``equal``, ``notequal``, ``epsilon``.

    Attributes:

    - ``color``: the color of the text.
    - ``draggable``: whether the text can be dragged by the user.

    :cvar SYMBOLS: A dictionary mapping from symbols to the character
        in the ``symbol`` font used to render them.
    """
    SYMBOLS = ...
    def __init__(self, canvas, symbol, **attribs) -> None:
        """
        Create a new symbol widget.

        :type canvas: Tkinter.Canvas
        :param canvas: This canvas widget's canvas.
        :type symbol: str
        :param symbol: The name of the symbol to display.
        :param attribs: The new canvas widget's attributes.
        """
        ...
    
    def symbol(self):
        """
        :return: the name of the symbol that is displayed by this
            symbol widget.
        :rtype: str
        """
        ...
    
    def set_symbol(self, symbol):
        """
        Change the symbol that is displayed by this symbol widget.

        :type symbol: str
        :param symbol: The name of the symbol to display.
        """
        ...
    
    def __repr__(self):
        ...
    
    @staticmethod
    def symbolsheet(size=...):
        """
        Open a new Tkinter window that displays the entire alphabet
        for the symbol font.  This is useful for constructing the
        ``SymbolWidget.SYMBOLS`` dictionary.
        """
        ...
    


class AbstractContainerWidget(CanvasWidget):
    """
    An abstract class for canvas widgets that contain a single child,
    such as ``BoxWidget`` and ``OvalWidget``.  Subclasses must define
    a constructor, which should create any new graphical elements and
    then call the ``AbstractCanvasContainer`` constructor.  Subclasses
    must also define the ``_update`` method and the ``_tags`` method;
    and any subclasses that define attributes should define
    ``__setitem__`` and ``__getitem__``.
    """
    def __init__(self, canvas, child, **attribs) -> None:
        """
        Create a new container widget.  This constructor should only
        be called by subclass constructors.

        :type canvas: Tkinter.Canvas
        :param canvas: This canvas widget's canvas.
        :param child: The container's child widget.  ``child`` must not
            have a parent.
        :type child: CanvasWidget
        :param attribs: The new canvas widget's attributes.
        """
        ...
    
    def child(self):
        """
        :return: The child widget contained by this container widget.
        :rtype: CanvasWidget
        """
        ...
    
    def set_child(self, child):
        """
        Change the child widget contained by this container widget.

        :param child: The new child widget.  ``child`` must not have a
            parent.
        :type child: CanvasWidget
        :rtype: None
        """
        ...
    
    def __repr__(self):
        ...
    


class BoxWidget(AbstractContainerWidget):
    """
    A canvas widget that places a box around a child widget.

    Attributes:
      - ``fill``: The color used to fill the interior of the box.
      - ``outline``: The color used to draw the outline of the box.
      - ``width``: The width of the outline of the box.
      - ``margin``: The number of pixels space left between the child
        and the box.
      - ``draggable``: whether the text can be dragged by the user.
    """
    def __init__(self, canvas, child, **attribs) -> None:
        """
        Create a new box widget.

        :type canvas: Tkinter.Canvas
        :param canvas: This canvas widget's canvas.
        :param child: The child widget.  ``child`` must not have a
            parent.
        :type child: CanvasWidget
        :param attribs: The new canvas widget's attributes.
        """
        ...
    
    def __setitem__(self, attr, value):
        ...
    
    def __getitem__(self, attr):
        ...
    


class OvalWidget(AbstractContainerWidget):
    """
    A canvas widget that places a oval around a child widget.

    Attributes:
      - ``fill``: The color used to fill the interior of the oval.
      - ``outline``: The color used to draw the outline of the oval.
      - ``width``: The width of the outline of the oval.
      - ``margin``: The number of pixels space left between the child
        and the oval.
      - ``draggable``: whether the text can be dragged by the user.
      - ``double``: If true, then a double-oval is drawn.
    """
    def __init__(self, canvas, child, **attribs) -> None:
        """
        Create a new oval widget.

        :type canvas: Tkinter.Canvas
        :param canvas: This canvas widget's canvas.
        :param child: The child widget.  ``child`` must not have a
            parent.
        :type child: CanvasWidget
        :param attribs: The new canvas widget's attributes.
        """
        ...
    
    def __setitem__(self, attr, value):
        ...
    
    def __getitem__(self, attr):
        ...
    
    RATIO = ...


class ParenWidget(AbstractContainerWidget):
    """
    A canvas widget that places a pair of parenthases around a child
    widget.

    Attributes:
      - ``color``: The color used to draw the parenthases.
      - ``width``: The width of the parenthases.
      - ``draggable``: whether the text can be dragged by the user.
    """
    def __init__(self, canvas, child, **attribs) -> None:
        """
        Create a new parenthasis widget.

        :type canvas: Tkinter.Canvas
        :param canvas: This canvas widget's canvas.
        :param child: The child widget.  ``child`` must not have a
            parent.
        :type child: CanvasWidget
        :param attribs: The new canvas widget's attributes.
        """
        ...
    
    def __setitem__(self, attr, value):
        ...
    
    def __getitem__(self, attr):
        ...
    


class BracketWidget(AbstractContainerWidget):
    """
    A canvas widget that places a pair of brackets around a child
    widget.

    Attributes:
      - ``color``: The color used to draw the brackets.
      - ``width``: The width of the brackets.
      - ``draggable``: whether the text can be dragged by the user.
    """
    def __init__(self, canvas, child, **attribs) -> None:
        """
        Create a new bracket widget.

        :type canvas: Tkinter.Canvas
        :param canvas: This canvas widget's canvas.
        :param child: The child widget.  ``child`` must not have a
            parent.
        :type child: CanvasWidget
        :param attribs: The new canvas widget's attributes.
        """
        ...
    
    def __setitem__(self, attr, value):
        ...
    
    def __getitem__(self, attr):
        ...
    


class SequenceWidget(CanvasWidget):
    """
    A canvas widget that keeps a list of canvas widgets in a
    horizontal line.

    Attributes:
      - ``align``: The vertical alignment of the children.  Possible
        values are ``'top'``, ``'center'``, and ``'bottom'``.  By
        default, children are center-aligned.
      - ``space``: The amount of horizontal space to place between
        children.  By default, one pixel of space is used.
      - ``ordered``: If true, then keep the children in their
        original order.
    """
    def __init__(self, canvas, *children, **attribs) -> None:
        """
        Create a new sequence widget.

        :type canvas: Tkinter.Canvas
        :param canvas: This canvas widget's canvas.
        :param children: The widgets that should be aligned
            horizontally.  Each child must not have a parent.
        :type children: list(CanvasWidget)
        :param attribs: The new canvas widget's attributes.
        """
        ...
    
    def __setitem__(self, attr, value):
        ...
    
    def __getitem__(self, attr):
        ...
    
    def __repr__(self):
        ...
    
    children = ...
    def replace_child(self, oldchild, newchild):
        """
        Replace the child canvas widget ``oldchild`` with ``newchild``.
        ``newchild`` must not have a parent.  ``oldchild``'s parent will
        be set to None.

        :type oldchild: CanvasWidget
        :param oldchild: The child canvas widget to remove.
        :type newchild: CanvasWidget
        :param newchild: The canvas widget that should replace
            ``oldchild``.
        """
        ...
    
    def remove_child(self, child):
        """
        Remove the given child canvas widget.  ``child``'s parent will
        be set ot None.

        :type child: CanvasWidget
        :param child: The child canvas widget to remove.
        """
        ...
    
    def insert_child(self, index, child):
        """
        Insert a child canvas widget before a given index.

        :type child: CanvasWidget
        :param child: The canvas widget that should be inserted.
        :type index: int
        :param index: The index where the child widget should be
            inserted.  In particular, the index of ``child`` will be
            ``index``; and the index of any children whose indices were
            greater than equal to ``index`` before ``child`` was
            inserted will be incremented by one.
        """
        ...
    


class StackWidget(CanvasWidget):
    """
    A canvas widget that keeps a list of canvas widgets in a vertical
    line.

    Attributes:
      - ``align``: The horizontal alignment of the children.  Possible
        values are ``'left'``, ``'center'``, and ``'right'``.  By
        default, children are center-aligned.
      - ``space``: The amount of vertical space to place between
        children.  By default, one pixel of space is used.
      - ``ordered``: If true, then keep the children in their
        original order.
    """
    def __init__(self, canvas, *children, **attribs) -> None:
        """
        Create a new stack widget.

        :type canvas: Tkinter.Canvas
        :param canvas: This canvas widget's canvas.
        :param children: The widgets that should be aligned
            vertically.  Each child must not have a parent.
        :type children: list(CanvasWidget)
        :param attribs: The new canvas widget's attributes.
        """
        ...
    
    def __setitem__(self, attr, value):
        ...
    
    def __getitem__(self, attr):
        ...
    
    def __repr__(self):
        ...
    
    children = ...
    def replace_child(self, oldchild, newchild):
        """
        Replace the child canvas widget ``oldchild`` with ``newchild``.
        ``newchild`` must not have a parent.  ``oldchild``'s parent will
        be set to None.

        :type oldchild: CanvasWidget
        :param oldchild: The child canvas widget to remove.
        :type newchild: CanvasWidget
        :param newchild: The canvas widget that should replace
            ``oldchild``.
        """
        ...
    
    def remove_child(self, child):
        """
        Remove the given child canvas widget.  ``child``'s parent will
        be set ot None.

        :type child: CanvasWidget
        :param child: The child canvas widget to remove.
        """
        ...
    
    def insert_child(self, index, child):
        """
        Insert a child canvas widget before a given index.

        :type child: CanvasWidget
        :param child: The canvas widget that should be inserted.
        :type index: int
        :param index: The index where the child widget should be
            inserted.  In particular, the index of ``child`` will be
            ``index``; and the index of any children whose indices were
            greater than equal to ``index`` before ``child`` was
            inserted will be incremented by one.
        """
        ...
    


class SpaceWidget(CanvasWidget):
    """
    A canvas widget that takes up space but does not display
    anything.  A ``SpaceWidget`` can be used to add space between
    elements.  Each space widget is characterized by a width and a
    height.  If you wish to only create horizontal space, then use a
    height of zero; and if you wish to only create vertical space, use
    a width of zero.
    """
    def __init__(self, canvas, width, height, **attribs) -> None:
        """
        Create a new space widget.

        :type canvas: Tkinter.Canvas
        :param canvas: This canvas widget's canvas.
        :type width: int
        :param width: The width of the new space widget.
        :type height: int
        :param height: The height of the new space widget.
        :param attribs: The new canvas widget's attributes.
        """
        ...
    
    def set_width(self, width):
        """
        Change the width of this space widget.

        :param width: The new width.
        :type width: int
        :rtype: None
        """
        ...
    
    def set_height(self, height):
        """
        Change the height of this space widget.

        :param height: The new height.
        :type height: int
        :rtype: None
        """
        ...
    
    def __repr__(self):
        ...
    


class ScrollWatcherWidget(CanvasWidget):
    """
    A special canvas widget that adjusts its ``Canvas``'s scrollregion
    to always include the bounding boxes of all of its children.  The
    scroll-watcher widget will only increase the size of the
    ``Canvas``'s scrollregion; it will never decrease it.
    """
    def __init__(self, canvas, *children, **attribs) -> None:
        """
        Create a new scroll-watcher widget.

        :type canvas: Tkinter.Canvas
        :param canvas: This canvas widget's canvas.
        :type children: list(CanvasWidget)
        :param children: The canvas widgets watched by the
            scroll-watcher.  The scroll-watcher will ensure that these
            canvas widgets are always contained in their canvas's
            scrollregion.
        :param attribs: The new canvas widget's attributes.
        """
        ...
    
    def add_child(self, canvaswidget):
        """
        Add a new canvas widget to the scroll-watcher.  The
        scroll-watcher will ensure that the new canvas widget is
        always contained in its canvas's scrollregion.

        :param canvaswidget: The new canvas widget.
        :type canvaswidget: CanvasWidget
        :rtype: None
        """
        ...
    
    def remove_child(self, canvaswidget):
        """
        Remove a canvas widget from the scroll-watcher.  The
        scroll-watcher will no longer ensure that the new canvas
        widget is always contained in its canvas's scrollregion.

        :param canvaswidget: The canvas widget to remove.
        :type canvaswidget: CanvasWidget
        :rtype: None
        """
        ...
    


class CanvasFrame(object):
    """
    A ``Tkinter`` frame containing a canvas and scrollbars.
    ``CanvasFrame`` uses a ``ScrollWatcherWidget`` to ensure that all of
    the canvas widgets contained on its canvas are within its
    scrollregion.  In order for ``CanvasFrame`` to make these checks,
    all canvas widgets must be registered with ``add_widget`` when they
    are added to the canvas; and destroyed with ``destroy_widget`` when
    they are no longer needed.

    If a ``CanvasFrame`` is created with no parent, then it will create
    its own main window, including a "Done" button and a "Print"
    button.
    """
    def __init__(self, parent=..., **kw) -> None:
        """
        Create a new ``CanvasFrame``.

        :type parent: Tkinter.BaseWidget or Tkinter.Tk
        :param parent: The parent ``Tkinter`` widget.  If no parent is
            specified, then ``CanvasFrame`` will create a new main
            window.
        :param kw: Keyword arguments for the new ``Canvas``.  See the
            documentation for ``Tkinter.Canvas`` for more information.
        """
        ...
    
    def print_to_file(self, filename=...):
        """
        Print the contents of this ``CanvasFrame`` to a postscript
        file.  If no filename is given, then prompt the user for one.

        :param filename: The name of the file to print the tree to.
        :type filename: str
        :rtype: None
        """
        ...
    
    def scrollregion(self):
        """
        :return: The current scroll region for the canvas managed by
            this ``CanvasFrame``.
        :rtype: 4-tuple of int
        """
        ...
    
    def canvas(self):
        """
        :return: The canvas managed by this ``CanvasFrame``.
        :rtype: Tkinter.Canvas
        """
        ...
    
    def add_widget(self, canvaswidget, x=..., y=...):
        """
        Register a canvas widget with this ``CanvasFrame``.  The
        ``CanvasFrame`` will ensure that this canvas widget is always
        within the ``Canvas``'s scrollregion.  If no coordinates are
        given for the canvas widget, then the ``CanvasFrame`` will
        attempt to find a clear area of the canvas for it.

        :type canvaswidget: CanvasWidget
        :param canvaswidget: The new canvas widget.  ``canvaswidget``
            must have been created on this ``CanvasFrame``'s canvas.
        :type x: int
        :param x: The initial x coordinate for the upper left hand
            corner of ``canvaswidget``, in the canvas's coordinate
            space.
        :type y: int
        :param y: The initial y coordinate for the upper left hand
            corner of ``canvaswidget``, in the canvas's coordinate
            space.
        """
        ...
    
    def destroy_widget(self, canvaswidget):
        """
        Remove a canvas widget from this ``CanvasFrame``.  This
        deregisters the canvas widget, and destroys it.
        """
        ...
    
    def remove_widget(self, canvaswidget):
        ...
    
    def pack(self, cnf=..., **kw):
        """
        Pack this ``CanvasFrame``.  See the documentation for
        ``Tkinter.Pack`` for more information.
        """
        ...
    
    def destroy(self, *e):
        """
        Destroy this ``CanvasFrame``.  If this ``CanvasFrame`` created a
        top-level window, then this will close that window.
        """
        ...
    
    def mainloop(self, *args, **kwargs):
        """
        Enter the Tkinter mainloop.  This function must be called if
        this frame is created from a non-interactive program (e.g.
        from a secript); otherwise, the frame will close as soon as
        the script completes.
        """
        ...
    


class ShowText(object):
    """
    A ``Tkinter`` window used to display a text.  ``ShowText`` is
    typically used by graphical tools to display help text, or similar
    information.
    """
    def __init__(self, root, title, text, width=..., height=..., **textbox_options) -> None:
        ...
    
    def find_dimentions(self, text, width, height):
        ...
    
    def destroy(self, *e):
        ...
    
    def mainloop(self, *args, **kwargs):
        """
        Enter the Tkinter mainloop.  This function must be called if
        this window is created from a non-interactive program (e.g.
        from a secript); otherwise, the window will close as soon as
        the script completes.
        """
        ...
    


class EntryDialog(object):
    """
    A dialog box for entering
    """
    def __init__(self, parent, original_text=..., instructions=..., set_callback=..., title=...) -> None:
        ...
    


class ColorizedList(object):
    """
    An abstract base class for displaying a colorized list of items.
    Subclasses should define:
      - ``_init_colortags``, which sets up Text color tags that
        will be used by the list.
      - ``_item_repr``, which returns a list of (text,colortag)
        tuples that make up the colorized representation of the
        item.
    :note: Typically, you will want to register a callback for
        ``'select'`` that calls ``mark`` on the given item.
    """
    def __init__(self, parent, items=..., **options) -> None:
        """
        Construct a new list.

        :param parent: The Tk widget that contains the colorized list
        :param items: The initial contents of the colorized list.
        :param options:
        """
        ...
    
    def get(self, index=...):
        """
        :return: A list of the items contained by this list.
        """
        ...
    
    def set(self, items):
        """
        Modify the list of items contained by this list.
        """
        ...
    
    def unmark(self, item=...):
        """
        Remove highlighting from the given item; or from every item,
        if no item is given.
        :raise ValueError: If ``item`` is not contained in the list.
        :raise KeyError: If ``item`` is not marked.
        """
        ...
    
    def mark(self, item):
        """
        Highlight the given item.
        :raise ValueError: If ``item`` is not contained in the list.
        """
        ...
    
    def markonly(self, item):
        """
        Remove any current highlighting, and mark the given item.
        :raise ValueError: If ``item`` is not contained in the list.
        """
        ...
    
    def view(self, item):
        """
        Adjust the view such that the given item is visible.  If
        the item is already visible, then do nothing.
        """
        ...
    
    def add_callback(self, event, func):
        """
        Register a callback function with the list.  This function
        will be called whenever the given event occurs.

        :param event: The event that will trigger the callback
            function.  Valid events are: click1, click2, click3,
            space, return, select, up, down, next, prior, move
        :param func: The function that should be called when
            the event occurs.  ``func`` will be called with a
            single item as its argument.  (The item selected
            or the item moved to).
        """
        ...
    
    def remove_callback(self, event, func=...):
        """
        Deregister a callback function.  If ``func`` is none, then
        all callbacks are removed for the given event.
        """
        ...
    
    def pack(self, cnf=..., **kw):
        ...
    
    def grid(self, cnf=..., **kw):
        ...
    
    def focus(self):
        ...
    


class MutableOptionMenu(Menubutton):
    def __init__(self, master, values, **options) -> None:
        ...
    
    def add(self, value):
        ...
    
    def set(self, value):
        ...
    
    def remove(self, value):
        ...
    
    def __getitem__(self, name):
        ...
    
    def destroy(self):
        """Destroy this widget and the associated menu."""
        ...
    


def demo():
    """
    A simple demonstration showing how to use canvas widgets.
    """
    ...

if __name__ == "__main__":
    ...
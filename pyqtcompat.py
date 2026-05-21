# Copyright (c) 2026 Jifeng Wu
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
import sys

from detect_qt_binding import QtBindings, detect_qt_binding

__all__ = [
    "QtBindings",
    "QT_BINDING",
    "IS_PYQT",
    "IS_PYSIDE",
    "IS_QT6",
    "QtSignal",
    "QTimer",
    "QImage",
    "QPixmap",
    "QColor",
    "QPainter",
    "QPen",
    "QScreen",
    "QAbstractSlider",
    "QApplication",
    "QCheckBox",
    "QComboBox",
    "QDesktopServices",
    "QDesktopWidget",
    "QFileDialog",
    "QFrame",
    "QGroupBox",
    "QHBoxLayout",
    "QLabel",
    "QLineEdit",
    "QMainWindow",
    "QMessageBox",
    "QPushButton",
    "QScrollArea",
    "QSizePolicy",
    "QSlider",
    "QVBoxLayout",
    "QWidget",
    "QTextEdit",
    "QRect",
    "QRegion",
    "Format_RGB32",
    "Format_ARGB32",
    "Format_RGB888",
    "QT_KEEP_ASPECT_RATIO",
    "QT_SMOOTH_TRANSFORMATION",
    "QT_ALIGN_CENTER",
    "QT_HORIZONTAL",
    "QT_SCROLLBAR_ALWAYS_OFF",
    "QT_SCROLLBAR_AS_NEEDED",
    "QSIZEPOLICY_EXPANDING",
    "QT_FRAMELESS_WINDOW_HINT",
    "QT_WINDOW_STAYS_ON_TOP_HINT",
    "QT_WA_TRANSLUCENT_BACKGROUND",
    "QT_CROSS_CURSOR",
    "QT_LEFT_BUTTON",
    "QT_KEY_ESCAPE",
    "SLIDER_SINGLE_STEP_ADD",
    "SLIDER_SINGLE_STEP_SUB",
    "SLIDER_PAGE_STEP_ADD",
    "SLIDER_PAGE_STEP_SUB",
    "SLIDER_MOVE",
    "exec_qapplication",
    "execute",
    "get_or_create_q_application",
    "get_buffer",
    "qimage_get_buffer",
    "get_primary_screen_geometry",
    "get_primary_screen_size",
    "grab_primary_screen_pixmap",
]

SUPPORTED_QT_BINDINGS_MESSAGE = (
    "We require one of PyQt6, PySide6, PyQt5, PySide2, PyQt4, or PySide. "
    "None of these packages were detected in your Python environment."
)

QT_BINDING = detect_qt_binding()
if QT_BINDING is None:
    raise ImportError(SUPPORTED_QT_BINDINGS_MESSAGE)

qt_binding = QT_BINDING
detected_qt_binding = QT_BINDING

IS_PYQT = False
IS_PYSIDE = False
IS_QT6 = False

QtCore = None
QtGui = None
QtWidgets = None

Qt = None
Signal = None
pyqtSignal = None
QtSignal = None
QTimer = None

QImage = None
QPixmap = None
QColor = None
QPainter = None
QPen = None
QScreen = None

QAbstractSlider = None
QApplication = None
QCheckBox = None
QComboBox = None
QDesktopServices = None
QDesktopWidget = None
QFileDialog = None
QFrame = None
QGroupBox = None
QHBoxLayout = None
QLabel = None
QLineEdit = None
QMainWindow = None
QMessageBox = None
QPushButton = None
QScrollArea = None
QSizePolicy = None
QSlider = None
QVBoxLayout = None
QWidget = None
QTextEdit = None
QRect = None
QRegion = None

QIMAGE_FORMAT_RGB32 = None
QIMAGE_FORMAT_ARGB32 = None
QIMAGE_FORMAT_RGB888 = None
Format_RGB32 = None
Format_ARGB32 = None
Format_RGB888 = None

QT_KEEP_ASPECT_RATIO = None
QT_SMOOTH_TRANSFORMATION = None
QT_ALIGN_CENTER = None
QT_HORIZONTAL = None
QT_SCROLLBAR_ALWAYS_OFF = None
QT_SCROLLBAR_AS_NEEDED = None
QSIZEPOLICY_EXPANDING = None

QT_FRAMELESS_WINDOW_HINT = None
QT_WINDOW_STAYS_ON_TOP_HINT = None
QT_WA_TRANSLUCENT_BACKGROUND = None
QT_CROSS_CURSOR = None
QT_LEFT_BUTTON = None
QT_KEY_ESCAPE = None

SLIDER_SINGLE_STEP_ADD = None
SLIDER_SINGLE_STEP_SUB = None
SLIDER_PAGE_STEP_ADD = None
SLIDER_PAGE_STEP_SUB = None
SLIDER_MOVE = None

if QT_BINDING == QtBindings.PyQt6:
    import PyQt6.QtCore as QtCore
    import PyQt6.QtGui as QtGui
    import PyQt6.QtWidgets as QtWidgets
    from PyQt6.QtCore import Qt, QRect, QTimer, pyqtSignal
    from PyQt6.QtGui import QImage, QPixmap, QColor, QPainter, QPen, QRegion, QScreen
    from PyQt6.QtWidgets import (
        QAbstractSlider,
        QApplication,
        QCheckBox,
        QComboBox,
        QFileDialog,
        QFrame,
        QGroupBox,
        QHBoxLayout,
        QLabel,
        QLineEdit,
        QMainWindow,
        QMessageBox,
        QPushButton,
        QScrollArea,
        QSizePolicy,
        QSlider,
        QTextEdit,
        QVBoxLayout,
        QWidget,
    )

    Signal = pyqtSignal
    QtSignal = pyqtSignal
    IS_PYQT = True
    IS_QT6 = True

    QIMAGE_FORMAT_RGB32 = QImage.Format.Format_RGB32
    QIMAGE_FORMAT_ARGB32 = QImage.Format.Format_ARGB32
    QIMAGE_FORMAT_RGB888 = QImage.Format.Format_RGB888
    Format_RGB32 = QIMAGE_FORMAT_RGB32
    Format_ARGB32 = QIMAGE_FORMAT_ARGB32
    Format_RGB888 = QIMAGE_FORMAT_RGB888

    QT_KEEP_ASPECT_RATIO = Qt.AspectRatioMode.KeepAspectRatio
    QT_SMOOTH_TRANSFORMATION = Qt.TransformationMode.SmoothTransformation
    QT_ALIGN_CENTER = Qt.AlignmentFlag.AlignCenter
    QT_HORIZONTAL = Qt.Orientation.Horizontal
    QT_SCROLLBAR_ALWAYS_OFF = Qt.ScrollBarPolicy.ScrollBarAlwaysOff
    QT_SCROLLBAR_AS_NEEDED = Qt.ScrollBarPolicy.ScrollBarAsNeeded
    QSIZEPOLICY_EXPANDING = QSizePolicy.Policy.Expanding

    QT_FRAMELESS_WINDOW_HINT = Qt.WindowType.FramelessWindowHint
    QT_WINDOW_STAYS_ON_TOP_HINT = Qt.WindowType.WindowStaysOnTopHint
    QT_WA_TRANSLUCENT_BACKGROUND = Qt.WidgetAttribute.WA_TranslucentBackground
    QT_CROSS_CURSOR = Qt.CursorShape.CrossCursor
    QT_LEFT_BUTTON = Qt.MouseButton.LeftButton
    QT_KEY_ESCAPE = Qt.Key.Key_Escape

    SLIDER_SINGLE_STEP_ADD = QAbstractSlider.SliderAction.SliderSingleStepAdd.value
    SLIDER_SINGLE_STEP_SUB = QAbstractSlider.SliderAction.SliderSingleStepSub.value
    SLIDER_PAGE_STEP_ADD = QAbstractSlider.SliderAction.SliderPageStepAdd.value
    SLIDER_PAGE_STEP_SUB = QAbstractSlider.SliderAction.SliderPageStepSub.value
    SLIDER_MOVE = QAbstractSlider.SliderAction.SliderMove.value
elif QT_BINDING == QtBindings.PySide6:
    import PySide6.QtCore as QtCore
    import PySide6.QtGui as QtGui
    import PySide6.QtWidgets as QtWidgets
    from PySide6.QtCore import Qt, QRect, QTimer, Signal
    from PySide6.QtGui import QImage, QPixmap, QColor, QPainter, QPen, QRegion, QScreen
    from PySide6.QtWidgets import (
        QAbstractSlider,
        QApplication,
        QCheckBox,
        QComboBox,
        QFileDialog,
        QFrame,
        QGroupBox,
        QHBoxLayout,
        QLabel,
        QLineEdit,
        QMainWindow,
        QMessageBox,
        QPushButton,
        QScrollArea,
        QSizePolicy,
        QSlider,
        QTextEdit,
        QVBoxLayout,
        QWidget,
    )

    pyqtSignal = Signal
    QtSignal = Signal
    IS_PYSIDE = True
    IS_QT6 = True

    QIMAGE_FORMAT_RGB32 = QImage.Format.Format_RGB32
    QIMAGE_FORMAT_ARGB32 = QImage.Format.Format_ARGB32
    QIMAGE_FORMAT_RGB888 = QImage.Format.Format_RGB888
    Format_RGB32 = QIMAGE_FORMAT_RGB32
    Format_ARGB32 = QIMAGE_FORMAT_ARGB32
    Format_RGB888 = QIMAGE_FORMAT_RGB888

    QT_KEEP_ASPECT_RATIO = Qt.AspectRatioMode.KeepAspectRatio
    QT_SMOOTH_TRANSFORMATION = Qt.TransformationMode.SmoothTransformation
    QT_ALIGN_CENTER = Qt.AlignmentFlag.AlignCenter
    QT_HORIZONTAL = Qt.Orientation.Horizontal
    QT_SCROLLBAR_ALWAYS_OFF = Qt.ScrollBarPolicy.ScrollBarAlwaysOff
    QT_SCROLLBAR_AS_NEEDED = Qt.ScrollBarPolicy.ScrollBarAsNeeded
    QSIZEPOLICY_EXPANDING = QSizePolicy.Policy.Expanding

    QT_FRAMELESS_WINDOW_HINT = Qt.WindowType.FramelessWindowHint
    QT_WINDOW_STAYS_ON_TOP_HINT = Qt.WindowType.WindowStaysOnTopHint
    QT_WA_TRANSLUCENT_BACKGROUND = Qt.WidgetAttribute.WA_TranslucentBackground
    QT_CROSS_CURSOR = Qt.CursorShape.CrossCursor
    QT_LEFT_BUTTON = Qt.MouseButton.LeftButton
    QT_KEY_ESCAPE = Qt.Key.Key_Escape

    SLIDER_SINGLE_STEP_ADD = QAbstractSlider.SliderAction.SliderSingleStepAdd.value
    SLIDER_SINGLE_STEP_SUB = QAbstractSlider.SliderAction.SliderSingleStepSub.value
    SLIDER_PAGE_STEP_ADD = QAbstractSlider.SliderAction.SliderPageStepAdd.value
    SLIDER_PAGE_STEP_SUB = QAbstractSlider.SliderAction.SliderPageStepSub.value
    SLIDER_MOVE = QAbstractSlider.SliderAction.SliderMove.value
elif QT_BINDING == QtBindings.PyQt5:
    import PyQt5.QtCore as QtCore
    import PyQt5.QtGui as QtGui
    import PyQt5.QtWidgets as QtWidgets
    from PyQt5.QtCore import Qt, QRect, QTimer, pyqtSignal
    from PyQt5.QtGui import QImage, QPixmap, QColor, QPainter, QPen, QRegion, QScreen
    from PyQt5.QtWidgets import (
        QAbstractSlider,
        QApplication,
        QCheckBox,
        QComboBox,
        QFileDialog,
        QFrame,
        QGroupBox,
        QHBoxLayout,
        QLabel,
        QLineEdit,
        QMainWindow,
        QMessageBox,
        QPushButton,
        QScrollArea,
        QSizePolicy,
        QSlider,
        QTextEdit,
        QVBoxLayout,
        QWidget,
    )

    Signal = pyqtSignal
    QtSignal = pyqtSignal
    IS_PYQT = True

    QIMAGE_FORMAT_RGB32 = QImage.Format_RGB32
    QIMAGE_FORMAT_ARGB32 = QImage.Format_ARGB32
    QIMAGE_FORMAT_RGB888 = QImage.Format_RGB888
    Format_RGB32 = QIMAGE_FORMAT_RGB32
    Format_ARGB32 = QIMAGE_FORMAT_ARGB32
    Format_RGB888 = QIMAGE_FORMAT_RGB888

    QT_KEEP_ASPECT_RATIO = Qt.KeepAspectRatio
    QT_SMOOTH_TRANSFORMATION = Qt.SmoothTransformation
    QT_ALIGN_CENTER = Qt.AlignCenter
    QT_HORIZONTAL = Qt.Horizontal
    QT_SCROLLBAR_ALWAYS_OFF = Qt.ScrollBarAlwaysOff
    QT_SCROLLBAR_AS_NEEDED = Qt.ScrollBarAsNeeded
    QSIZEPOLICY_EXPANDING = QSizePolicy.Expanding

    QT_FRAMELESS_WINDOW_HINT = Qt.FramelessWindowHint
    QT_WINDOW_STAYS_ON_TOP_HINT = Qt.WindowStaysOnTopHint
    QT_WA_TRANSLUCENT_BACKGROUND = Qt.WA_TranslucentBackground
    QT_CROSS_CURSOR = Qt.CrossCursor
    QT_LEFT_BUTTON = Qt.LeftButton
    QT_KEY_ESCAPE = Qt.Key_Escape

    SLIDER_SINGLE_STEP_ADD = int(QAbstractSlider.SliderAction.SliderSingleStepAdd)
    SLIDER_SINGLE_STEP_SUB = int(QAbstractSlider.SliderAction.SliderSingleStepSub)
    SLIDER_PAGE_STEP_ADD = int(QAbstractSlider.SliderAction.SliderPageStepAdd)
    SLIDER_PAGE_STEP_SUB = int(QAbstractSlider.SliderAction.SliderPageStepSub)
    SLIDER_MOVE = int(QAbstractSlider.SliderAction.SliderMove)
elif QT_BINDING == QtBindings.PySide2:
    import PySide2.QtCore as QtCore
    import PySide2.QtGui as QtGui
    import PySide2.QtWidgets as QtWidgets
    from PySide2.QtCore import Qt, QRect, QTimer, Signal
    from PySide2.QtGui import QImage, QPixmap, QColor, QPainter, QPen, QRegion, QScreen
    from PySide2.QtWidgets import (
        QAbstractSlider,
        QApplication,
        QCheckBox,
        QComboBox,
        QFileDialog,
        QFrame,
        QGroupBox,
        QHBoxLayout,
        QLabel,
        QLineEdit,
        QMainWindow,
        QMessageBox,
        QPushButton,
        QScrollArea,
        QSizePolicy,
        QSlider,
        QTextEdit,
        QVBoxLayout,
        QWidget,
    )

    pyqtSignal = Signal
    QtSignal = Signal
    IS_PYSIDE = True

    QIMAGE_FORMAT_RGB32 = QImage.Format_RGB32
    QIMAGE_FORMAT_ARGB32 = QImage.Format_ARGB32
    QIMAGE_FORMAT_RGB888 = QImage.Format_RGB888
    Format_RGB32 = QIMAGE_FORMAT_RGB32
    Format_ARGB32 = QIMAGE_FORMAT_ARGB32
    Format_RGB888 = QIMAGE_FORMAT_RGB888

    QT_KEEP_ASPECT_RATIO = Qt.KeepAspectRatio
    QT_SMOOTH_TRANSFORMATION = Qt.SmoothTransformation
    QT_ALIGN_CENTER = Qt.AlignCenter
    QT_HORIZONTAL = Qt.Horizontal
    QT_SCROLLBAR_ALWAYS_OFF = Qt.ScrollBarAlwaysOff
    QT_SCROLLBAR_AS_NEEDED = Qt.ScrollBarAsNeeded
    QSIZEPOLICY_EXPANDING = QSizePolicy.Expanding

    QT_FRAMELESS_WINDOW_HINT = Qt.FramelessWindowHint
    QT_WINDOW_STAYS_ON_TOP_HINT = Qt.WindowStaysOnTopHint
    QT_WA_TRANSLUCENT_BACKGROUND = Qt.WA_TranslucentBackground
    QT_CROSS_CURSOR = Qt.CrossCursor
    QT_LEFT_BUTTON = Qt.LeftButton
    QT_KEY_ESCAPE = Qt.Key_Escape

    SLIDER_SINGLE_STEP_ADD = int(QAbstractSlider.SliderAction.SliderSingleStepAdd)
    SLIDER_SINGLE_STEP_SUB = int(QAbstractSlider.SliderAction.SliderSingleStepSub)
    SLIDER_PAGE_STEP_ADD = int(QAbstractSlider.SliderAction.SliderPageStepAdd)
    SLIDER_PAGE_STEP_SUB = int(QAbstractSlider.SliderAction.SliderPageStepSub)
    SLIDER_MOVE = int(QAbstractSlider.SliderAction.SliderMove)
elif QT_BINDING == QtBindings.PyQt4:
    import PyQt4.QtCore as QtCore
    import PyQt4.QtGui as QtGui
    from PyQt4.QtCore import Qt, QRect, QTimer, pyqtSignal
    from PyQt4.QtGui import (
        QAbstractSlider,
        QApplication,
        QCheckBox,
        QColor,
        QComboBox,
        QDesktopServices,
        QDesktopWidget,
        QFileDialog,
        QFrame,
        QGroupBox,
        QHBoxLayout,
        QImage,
        QLabel,
        QLineEdit,
        QMainWindow,
        QMessageBox,
        QPainter,
        QPen,
        QPixmap,
        QPushButton,
        QRegion,
        QScrollArea,
        QSizePolicy,
        QSlider,
        QTextEdit,
        QVBoxLayout,
        QWidget,
    )

    QtWidgets = QtGui
    Signal = pyqtSignal
    QtSignal = pyqtSignal
    IS_PYQT = True

    QIMAGE_FORMAT_RGB32 = QImage.Format_RGB32
    QIMAGE_FORMAT_ARGB32 = QImage.Format_ARGB32
    QIMAGE_FORMAT_RGB888 = QImage.Format_RGB888
    Format_RGB32 = QIMAGE_FORMAT_RGB32
    Format_ARGB32 = QIMAGE_FORMAT_ARGB32
    Format_RGB888 = QIMAGE_FORMAT_RGB888

    QT_KEEP_ASPECT_RATIO = Qt.KeepAspectRatio
    QT_SMOOTH_TRANSFORMATION = Qt.SmoothTransformation
    QT_ALIGN_CENTER = Qt.AlignCenter
    QT_HORIZONTAL = Qt.Horizontal
    QT_SCROLLBAR_ALWAYS_OFF = Qt.ScrollBarAlwaysOff
    QT_SCROLLBAR_AS_NEEDED = Qt.ScrollBarAsNeeded
    QSIZEPOLICY_EXPANDING = QSizePolicy.Expanding

    QT_FRAMELESS_WINDOW_HINT = Qt.FramelessWindowHint
    QT_WINDOW_STAYS_ON_TOP_HINT = Qt.WindowStaysOnTopHint
    QT_WA_TRANSLUCENT_BACKGROUND = Qt.WA_TranslucentBackground
    QT_CROSS_CURSOR = Qt.CrossCursor
    QT_LEFT_BUTTON = Qt.LeftButton
    QT_KEY_ESCAPE = Qt.Key_Escape

    SLIDER_SINGLE_STEP_ADD = QAbstractSlider.SliderSingleStepAdd
    SLIDER_SINGLE_STEP_SUB = QAbstractSlider.SliderSingleStepSub
    SLIDER_PAGE_STEP_ADD = QAbstractSlider.SliderPageStepAdd
    SLIDER_PAGE_STEP_SUB = QAbstractSlider.SliderPageStepSub
    SLIDER_MOVE = QAbstractSlider.SliderMove
elif QT_BINDING == QtBindings.PySide:
    import PySide.QtCore as QtCore
    import PySide.QtGui as QtGui
    from PySide.QtCore import Qt, QRect, QTimer, Signal
    from PySide.QtGui import (
        QAbstractSlider,
        QApplication,
        QCheckBox,
        QColor,
        QComboBox,
        QDesktopServices,
        QDesktopWidget,
        QFileDialog,
        QFrame,
        QGroupBox,
        QHBoxLayout,
        QImage,
        QLabel,
        QLineEdit,
        QMainWindow,
        QMessageBox,
        QPainter,
        QPen,
        QPixmap,
        QPushButton,
        QRegion,
        QScrollArea,
        QSizePolicy,
        QSlider,
        QTextEdit,
        QVBoxLayout,
        QWidget,
    )

    QtWidgets = QtGui
    pyqtSignal = Signal
    QtSignal = Signal
    IS_PYSIDE = True

    QIMAGE_FORMAT_RGB32 = QImage.Format_RGB32
    QIMAGE_FORMAT_ARGB32 = QImage.Format_ARGB32
    QIMAGE_FORMAT_RGB888 = QImage.Format_RGB888
    Format_RGB32 = QIMAGE_FORMAT_RGB32
    Format_ARGB32 = QIMAGE_FORMAT_ARGB32
    Format_RGB888 = QIMAGE_FORMAT_RGB888

    QT_KEEP_ASPECT_RATIO = Qt.KeepAspectRatio
    QT_SMOOTH_TRANSFORMATION = Qt.SmoothTransformation
    QT_ALIGN_CENTER = Qt.AlignCenter
    QT_HORIZONTAL = Qt.Horizontal
    QT_SCROLLBAR_ALWAYS_OFF = Qt.ScrollBarAlwaysOff
    QT_SCROLLBAR_AS_NEEDED = Qt.ScrollBarAsNeeded
    QSIZEPOLICY_EXPANDING = QSizePolicy.Expanding

    QT_FRAMELESS_WINDOW_HINT = Qt.FramelessWindowHint
    QT_WINDOW_STAYS_ON_TOP_HINT = Qt.WindowStaysOnTopHint
    QT_WA_TRANSLUCENT_BACKGROUND = Qt.WA_TranslucentBackground
    QT_CROSS_CURSOR = Qt.CrossCursor
    QT_LEFT_BUTTON = Qt.LeftButton
    QT_KEY_ESCAPE = Qt.Key_Escape

    SLIDER_SINGLE_STEP_ADD = int(QAbstractSlider.SliderAction.SliderSingleStepAdd)
    SLIDER_SINGLE_STEP_SUB = int(QAbstractSlider.SliderAction.SliderSingleStepSub)
    SLIDER_PAGE_STEP_ADD = int(QAbstractSlider.SliderAction.SliderPageStepAdd)
    SLIDER_PAGE_STEP_SUB = int(QAbstractSlider.SliderAction.SliderPageStepSub)
    SLIDER_MOVE = int(QAbstractSlider.SliderAction.SliderMove)
else:
    raise ImportError(SUPPORTED_QT_BINDINGS_MESSAGE)


del detect_qt_binding
del SUPPORTED_QT_BINDINGS_MESSAGE
del qt_binding
del detected_qt_binding
del QtCore
del QtGui
del QtWidgets
del Qt
del Signal
del pyqtSignal
del QIMAGE_FORMAT_RGB32
del QIMAGE_FORMAT_ARGB32
del QIMAGE_FORMAT_RGB888


def exec_qapplication(app):
    # type: (QApplication) -> int
    if IS_QT6:
        return getattr(app, "exec")()
    return app.exec_()


def execute(q_application):
    # type: (QApplication) -> int
    return exec_qapplication(q_application)


def get_or_create_q_application(argv=None):
    # type: (object) -> QApplication
    q_application = QApplication.instance()
    if q_application is None:
        if argv is None:
            argv = sys.argv
        q_application = QApplication(argv)
    return q_application


def qimage_get_buffer(qimage):
    # type: (QImage) -> object
    buffer_object = qimage.constBits()
    if IS_PYQT:
        if QT_BINDING == QtBindings.PyQt4:
            buffer_object.setsize(qimage.byteCount())
        else:
            buffer_object.setsize(qimage.sizeInBytes())
    return buffer_object


def get_buffer(qimage):
    # type: (QImage) -> object
    return qimage_get_buffer(qimage)


def get_primary_screen_geometry():
    # type: () -> object
    get_or_create_q_application()
    if QDesktopWidget is not None:
        desktop_widget = QDesktopWidget()
        return desktop_widget.screenGeometry()
    primary_screen = QApplication.primaryScreen()
    return primary_screen.geometry()


def get_primary_screen_size():
    # type: () -> tuple
    geometry = get_primary_screen_geometry()
    return geometry.width(), geometry.height()


def grab_primary_screen_pixmap():
    # type: () -> QPixmap
    get_or_create_q_application()
    if QDesktopWidget is not None:
        desktop_widget = QDesktopWidget()
        geometry = desktop_widget.screenGeometry()
        return QPixmap.grabWindow(
            desktop_widget.winId(), 0, 0, geometry.width(), geometry.height()
        )
    primary_screen = QApplication.primaryScreen()
    geometry = primary_screen.geometry()
    return primary_screen.grabWindow(0, 0, 0, geometry.width(), geometry.height())

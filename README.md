# pyqtcompat

A single-module Qt binding compatibility layer for PyQt6, PySide6, PyQt5, PySide2, PyQt4, and PySide.

## Installation

Install the package with:

```bash
pip install pyqtcompat
```

You must also have at least one supported Qt binding installed in your Python environment:

- PyQt6
- PySide6
- PyQt5
- PySide2
- PyQt4
- PySide

The module uses [`detect-qt-binding`](https://pypi.org/project/detect-qt-binding/) to choose the active binding.

## Usage

Import the normalized Qt names from `pyqtcompat` instead of importing directly from a specific binding:

```python
from pyqtcompat import QApplication, QLabel, QT_ALIGN_CENTER, execute

application = QApplication([])
label = QLabel('Hello from pyqtcompat')
label.setAlignment(QT_ALIGN_CENTER)
label.show()
raise SystemExit(execute(application))
```

Cross-binding window with a frameless, translucent, stay-on-top overlay:

```python
from pyqtcompat import (
    QApplication, QTextEdit, QRect, QRegion,
    QT_FRAMELESS_WINDOW_HINT,
    QT_WINDOW_STAYS_ON_TOP_HINT,
    QT_WA_TRANSLUCENT_BACKGROUND,
    QT_CROSS_CURSOR,
    QT_LEFT_BUTTON,
    QT_KEY_ESCAPE,
    get_or_create_q_application,
    execute,
)

application = get_or_create_q_application()
text_edit = QTextEdit()
text_edit.setWindowFlags(
    QT_FRAMELESS_WINDOW_HINT | QT_WINDOW_STAYS_ON_TOP_HINT
)
text_edit.setAttribute(QT_WA_TRANSLUCENT_BACKGROUND)
text_edit.setCursor(QT_CROSS_CURSOR)
# Check button or key presses against QT_LEFT_BUTTON / QT_KEY_ESCAPE as needed
text_edit.show()
raise SystemExit(execute(application))
```

You can also inspect which binding was selected:

```python
from pyqtcompat import QT_BINDING

print(QT_BINDING)
```

## Public API

`pyqtcompat` defines `__all__` at the top of the module. These names are the intended application-facing imports.

Binding and module-level names:

- `QtBindings`
- `QT_BINDING`
- `IS_PYQT`, `IS_PYSIDE`, `IS_QT6`
- `QtSignal`

Common Qt classes exported directly:

- `QTimer`
- `QImage`, `QPixmap`, `QColor`, `QPainter`, `QPen`, `QScreen`
- `QRect`, `QRegion`
- `QAbstractSlider`
- `QApplication`
- `QCheckBox`, `QComboBox`, `QDesktopServices`, `QDesktopWidget`, `QFileDialog`
- `QFrame`, `QGroupBox`, `QHBoxLayout`, `QLabel`, `QLineEdit`
- `QMainWindow`, `QMessageBox`, `QPushButton`, `QScrollArea`
- `QSizePolicy`, `QSlider`, `QTextEdit`, `QVBoxLayout`, `QWidget`

Compatibility constants exported directly:

- `Format_RGB32`, `Format_ARGB32`, `Format_RGB888`
- `QT_KEEP_ASPECT_RATIO`, `QT_SMOOTH_TRANSFORMATION`, `QT_ALIGN_CENTER`, `QT_HORIZONTAL`
- `QT_SCROLLBAR_ALWAYS_OFF`, `QT_SCROLLBAR_AS_NEEDED`
- `QSIZEPOLICY_EXPANDING`
- `QT_FRAMELESS_WINDOW_HINT`, `QT_WINDOW_STAYS_ON_TOP_HINT`, `QT_WA_TRANSLUCENT_BACKGROUND`
- `QT_CROSS_CURSOR`, `QT_LEFT_BUTTON`, `QT_KEY_ESCAPE`
- `SLIDER_SINGLE_STEP_ADD`, `SLIDER_SINGLE_STEP_SUB`, `SLIDER_PAGE_STEP_ADD`, `SLIDER_PAGE_STEP_SUB`, `SLIDER_MOVE`

Helper functions exported directly:

- `exec_qapplication(app)`
  - Purpose: Run the Qt application event loop with the correct cross-binding call style.
  - Returns: the integer exit code returned by the event loop.
- `execute(q_application)`
  - Purpose: Alias for `exec_qapplication()` for codebases already using that name.
  - Returns: the integer exit code returned by the event loop.
- `get_or_create_q_application(argv=None)`
  - Purpose: Return the existing `QApplication` instance, or create one if none exists yet.
  - Returns: a `QApplication` instance.
- `get_buffer(qimage)`
  - Purpose: Return a Python buffer-compatible view of the pixel memory of a `QImage`, handling PyQt/PySide differences.
  - Returns: a binding-specific buffer object suitable for zero-copy access.
- `qimage_get_buffer(qimage)`
  - Purpose: Same as `get_buffer()`; provided as the explicit `QImage`-named form.
  - Returns: a binding-specific buffer object suitable for zero-copy access.
- `get_primary_screen_geometry()`
  - Purpose: Read the geometry of the primary screen using the correct API for old and new Qt bindings.
  - Returns: a Qt rectangle object describing the primary screen bounds.
- `get_primary_screen_size()`
  - Purpose: Get the primary screen width and height as plain Python values.
  - Returns: a `(width, height)` tuple of integers.
- `grab_primary_screen_pixmap()`
  - Purpose: Capture the full primary screen into a pixmap using the correct API for the active binding.
  - Returns: a `QPixmap` containing the screen capture.

Example using `QImage` buffer access:

```python
from pyqtcompat import QImage, Format_RGB32, get_buffer

image = QImage(64, 64, Format_RGB32)
buffer_object = get_buffer(image)
print(type(buffer_object))
```

Example using screen-grab helpers:

```python
from pyqtcompat import get_or_create_q_application, get_primary_screen_size, grab_primary_screen_pixmap

application = get_or_create_q_application()
width, height = get_primary_screen_size()
pixmap = grab_primary_screen_pixmap()
print(width, height, pixmap.width(), pixmap.height())
```

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

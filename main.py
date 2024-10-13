import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gdk

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Visual Workflow Automation Tool")
        self.set_default_size(800, 600)

        self.selected_node = None
        self.setup_css()

        # Create the main layout
        self.layout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.set_child(self.layout)

        # Add the node library panel
        self.node_library = self.create_node_library()
        self.layout.append(self.node_library)

        # Add the workflow canvas
        self.canvas = self.create_canvas()
        self.layout.append(self.canvas)

    def setup_css(self):
        self.css_provider = Gtk.CssProvider()
        css = """
        #node-button {
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            padding: 10px;
        }
        #node-button:selected {
            border: 2px solid yellow;
        }
        """
        self.css_provider.load_from_data(css.encode('utf-8'))
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            self.css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def create_node_library(self):
        # (Code as shown in Step 1)
        # ...

    def create_canvas(self):
        # (Code as shown in Step 2)
        # ...

    def on_canvas_drag_data_received(self, widget, drag_context, x, y, data, info, time):
        # (Code as shown in Step 3)
        # ...

    def on_node_drag_begin(self, gesture, node_widget):
        # (Code as shown in Step 3)
        # ...

    def on_node_drag_update(self, gesture, offset_x, offset_y, node_widget):
        # (Code as shown in Step 3)
        # ...

    def on_node_clicked(self, gesture, n_press, x, y, node_widget):
        # (Code as shown in Step 4)
        # ...

class WorkflowApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='com.example.WorkflowApp')

    def do_activate(self):
        win = MainWindow(self)
        win.show()

if __name__ == '__main__':
    app = WorkflowApp()
    app.run()

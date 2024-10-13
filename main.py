import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gdk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Visual Workflow Automation Tool")
        self.set_default_size(800, 600)

        # Create the main layout
        self.layout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.set_child(self.layout)

        # Add the node library panel
        self.node_library = self.create_node_library()
        self.layout.append(self.node_library)

        # Add the workflow canvas
        self.canvas = self.create_canvas()
        self.layout.append(self.canvas)

    def create_node_library(self):
        # Placeholder for node library UI
        panel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        panel.set_size_request(200, -1)
        label = Gtk.Label(label="Node Library")
        panel.append(label)
        # Add node items here
        return panel

    def create_canvas(self):
        # Placeholder for canvas UI
        canvas = Gtk.DrawingArea()
        canvas.set_content_width(600)
        canvas.set_content_height(600)
        canvas.set_draw_func(self.draw_canvas)
        return canvas

    def draw_canvas(self, area, ctx, width, height):
        # Drawing code for the canvas
        ctx.set_source_rgb(1, 1, 1)  # White background
        ctx.paint()


class WorkflowApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='com.example.WorkflowApp')

    def do_activate(self):
        win = MainWindow(self)
        win.show()


if __name__ == '__main__':
    app = WorkflowApp()
    app.run()
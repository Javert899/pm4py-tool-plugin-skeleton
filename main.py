import pluginpackageRENAME
import preload
import os


if __name__ == "__main__":
    preload.preload()
    app = pluginpackageRENAME.app
    app.static_folder = os.path.join(os.getcwd(), "html")
    app.run()

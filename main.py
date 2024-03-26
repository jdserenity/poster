import logic as l; import gui as g; import app as a;


def main():
    logic = l.Logic(); gui = g.GUI(logic); app = a.App(gui)

    app.run()


if __name__ == "__main__":
    main()
